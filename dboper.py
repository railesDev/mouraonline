import random
import logging

def reset_interactive(conn, c):
    c.execute("DELETE FROM resps")
    c.execute("DELETE FROM questions")
    # c.execute("UPDATE questions SET used = 0")
    conn.commit()

def fill_questions_table(conn, c, file_path):
    with open(file_path, 'r') as file:
        for line in file:
            question = line.strip()
            c.execute("INSERT INTO questions (question, used) VALUES (%s, 0)", (question,))
    conn.commit()


def is_cheater(conn, c, user_id):
    c.execute("SELECT 1 FROM resps WHERE user_id = %s", (user_id,))
    return c.fetchone() is not None


def get_question(conn, c, user_id, username):
    c.execute("SELECT id, question FROM questions WHERE used = 0 OR (used = 1 AND NOT EXISTS (SELECT 1 FROM resps WHERE q_id = questions.id AND user_id = %s)) ORDER BY used DESC, id LIMIT 1", (user_id,))
    result = c.fetchone()
    if result:
        q_id, question = result
        c.execute("UPDATE questions SET used = used + 1 WHERE id = %s", (q_id,))
        c.execute("INSERT INTO resps (user_id, username, q_id, ans) VALUES (%s, %s, %s, %s)", (user_id, username, q_id, '-'))
        conn.commit()
        return question
    else:
        return None

def update_answer(conn, c, user_id, ans):
    c.execute("UPDATE resps SET ans = %s WHERE user_id = %s AND q_id IN (SELECT id FROM questions WHERE used = 1 OR used = 2)", (ans, user_id))
    conn.commit()

def search_pair(conn, c, user_id):
    c.execute("SELECT q_id FROM resps WHERE user_id = %s", (user_id,))
    q_id = c.fetchone()[0]
    c.execute("SELECT username, ans FROM resps WHERE %s IN (SELECT id FROM questions WHERE used = 2) AND user_id != %s", (q_id, user_id,))
    result = c.fetchone()
    if result is not None:
        if result[1]:
            return result
    else:
        return None

def check_outsider(conn, c):
    c.execute("SELECT id FROM questions WHERE used != 2 AND used != 0 LIMIT 1")
    question_id = c.fetchone()
    if question_id:
        c.execute("SELECT user_id FROM resps WHERE q_id = %s", (question_id[0],))
        user_id = c.fetchone()
        c.execute("UPDATE questions SET used = 2 WHERE used != 2")
        conn.commit()
        return user_id[0]
    else:
        return None


def get_all_ids(conn, c):
    c.execute('''SELECT id FROM users''')
    return [user_id[0] for user_id in c.fetchall()]


def create_users(conn, c):
    c.execute('''CREATE TABLE IF NOT EXISTS users
                 (id BIGSERIAL PRIMARY KEY, gender integer, campus text, program text, course text, frd_goal boolean, dts_goal boolean, ntw_goal boolean, gender_goals integer, photo_id text, ad_text text)''')
    conn.commit()


def create_reactions(conn, c):
    c.execute('''CREATE SEQUENCE IF NOT EXISTS reactions_id_seq;
                 CREATE TABLE IF NOT EXISTS reactions
                 (reactions_id BIGSERIAL PRIMARY KEY, id bigint, match_id bigint, reaction integer)''')
    conn.commit()


def create_blacklist(conn, c):
    c.execute('''CREATE SEQUENCE IF NOT EXISTS blacklist_id_seq;
                 CREATE TABLE IF NOT EXISTS blacklist
                 (id BIGSERIAL PRIMARY KEY, user_id bigint)''')
    conn.commit()


def create_firewall(conn, c):
    c.execute('''CREATE TABLE IF NOT EXISTS firewall
                 (user_id BIGSERIAL PRIMARY KEY, secret text)''')
    conn.commit()


def create_questions(conn, c):
    c.execute('''CREATE TABLE IF NOT EXISTS questions
                 (id BIGSERIAL PRIMARY KEY, question text, used integer)''')
    conn.commit()


def create_resps(conn, c):
    c.execute('''CREATE TABLE IF NOT EXISTS resps
                 (user_id BIGSERIAL PRIMARY KEY, username text, q_id BIGSERIAL, ans text)''')
    conn.commit()


def save_code(conn, c, id_, code_):
    c.execute('''
    INSERT INTO firewall (user_id, secret)
    VALUES (%s, %s)
    ON CONFLICT (user_id) DO UPDATE
    SET secret = EXCLUDED.secret;''', (id_, code_))
    conn.commit()


def extract_code(conn, c, id_):
    c.execute('''
    SELECT secret
    FROM firewall
    WHERE user_id = %s
    ''', (id_,))
    return c.fetchone()


def blacklist_user(conn, c, id_):
    c.execute("""
            INSERT INTO blacklist (id, user_id)
            SELECT nextval('blacklist_id_seq'), %s
            WHERE NOT EXISTS (SELECT 1 FROM blacklist WHERE user_id = %s);
        """, (id_, id_,))
    c.execute('''DELETE FROM users WHERE id = %s''', (id_,))
    c.execute('''DELETE FROM reactions WHERE id = %s''', (id_,))
    c.execute('''DELETE FROM reactions WHERE match_id = %s''', (id_,))
    conn.commit()

def unblacklist_user(conn, c, id_):
    c.execute('''DELETE FROM blacklist WHERE user_id = %s''', (id_,))
    conn.commit()


def check_blacklist(conn, c, id_):
    c.execute('''
                SELECT id, user_id
                FROM blacklist
                WHERE user_id = %s
            ''', (id_,))
    return (c.fetchone() is not None)


def user_exists(c, id_):
    c.execute('''SELECT * FROM users WHERE id = %s''', (id_,))
    res = c.fetchone()
    code = -1
    # code stands to check whether bot was just rebooted or user returns
    # we need to check gender code at least - if it is 2, we need to reregister him
    # otherwise we just take him to settings
    if res:
        code = (int(res[1]) == 2)
    return [(res if res else None), code]


def erase_user(conn, c, id_):
    c.execute('''DELETE FROM users WHERE id = %s''', (id_,))
    c.execute('''DELETE FROM reactions WHERE id = %s''', (id_,))
    c.execute('''DELETE FROM reactions WHERE match_id = %s''', (id_,))
    conn.commit()


def deactivate_user(conn, c, id_):
    c.execute("""
            UPDATE users
            SET gender = %s, gender_goals = %s, ad_text = %s
            WHERE id = %s
        """, (2, 3, '-', id_,))
    c.execute('''DELETE FROM reactions WHERE id = %s''', (id_,))
    c.execute('''DELETE FROM reactions WHERE match_id = %s''', (id_,))
    conn.commit()


def save_user(conn, c, data):
    c.execute('''
    INSERT INTO users (id, gender, campus, program, course, frd_goal, dts_goal, 
        ntw_goal, gender_goals, photo_id, ad_text) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
        ON CONFLICT (id) 
        DO UPDATE SET 
        gender = EXCLUDED.gender, 
        campus = EXCLUDED.campus, 
        program = EXCLUDED.program, 
        course = EXCLUDED.course, 
        frd_goal = EXCLUDED.frd_goal, 
        dts_goal = EXCLUDED.dts_goal, 
        ntw_goal = EXCLUDED.ntw_goal, 
        gender_goals = EXCLUDED.gender_goals, 
        photo_id = EXCLUDED.photo_id, 
        ad_text = EXCLUDED.ad_text''', data)
    conn.commit()


def extract_user(conn, c, id_):
    c.execute('''
                SELECT id, gender, gender_goals, frd_goal, dts_goal, ntw_goal
                FROM users
                WHERE id = %s
                LIMIT 1
            ''', (id_,))
    return c.fetchone()


def extract_ad(conn, c, id_):
    c.execute('''
                SELECT id, gender, campus, program, course, frd_goal, dts_goal, ntw_goal, gender_goals, photo_id, ad_text
                FROM users
                WHERE id = %s
                LIMIT 1
            ''', (id_,))
    return c.fetchone()

def find_match(conn, c, user_data):
    c.execute('''
    SELECT users.id
    FROM users
    WHERE (
    users.id != %s
    AND
    (users.gender_goals = %s OR users.gender_goals = 2) AND (users.gender = %s OR %s = 2) AND (users.frd_goal = %s OR users.dts_goal = %s OR users.ntw_goal = %s)
    )
    AND NOT EXISTS (
    SELECT 1
    FROM reactions
    WHERE ((reactions.match_id = users.id AND reactions.id = %s) OR (reactions.match_id = %s AND reactions.id = users.id)) AND (reactions.reaction = 2 OR reactions.reaction = 1 OR reactions.reaction = 0)
    )
    AND users.id NOT IN (SELECT reactions.match_id FROM reactions WHERE reactions.id = users.id)
    LIMIT 10''', (user_data[0], user_data[1], user_data[2], user_data[2], user_data[3], user_data[4], user_data[5], user_data[0], user_data[0]))
    res = c.fetchall()
    return random.choice(res) if res else None


def get_match_data(conn, c, match_id):
    c.execute('''
    SELECT *
    FROM users
    WHERE id = %s
    LIMIT 1
    ''', (match_id,))
    match_data = c.fetchone()
    return match_data


def react(conn, c, id_, match_id_, reaction):
    c.execute("SELECT EXISTS(SELECT 1 FROM reactions WHERE id = %s AND match_id = %s);", (id_, match_id_))
    exists = c.fetchone()[0]

    # If the row exists and the reaction is different, update it
    if exists:
        c.execute("""
            UPDATE reactions
            SET reaction = %s
            WHERE id = %s AND match_id = %s AND reaction != %s AND reaction != 2;
        """, (reaction, id_, match_id_, reaction))
        '''
        c.execute("""
            UPDATE reactions
            SET reaction = %s
            WHERE id = %s AND match_id = %s AND reaction != %s AND reaction != 2;
        """, (reaction, match_id_, id_, reaction))
        '''
    else:
        # If the row does not exist, insert a new row
        c.execute("""
            INSERT INTO reactions (reactions_id, id, match_id, reaction)
            SELECT nextval('reactions_id_seq'), %s, %s, %s
            WHERE NOT EXISTS (SELECT 1 FROM reactions WHERE id = %s AND match_id = %s);
        """, (id_, match_id_, reaction, id_, match_id_))
        '''
        c.execute("""
            INSERT INTO reactions (reactions_id, id, match_id, reaction)
            SELECT nextval('reactions_id_seq'), %s, %s, %s
            WHERE NOT EXISTS (SELECT 1 FROM reactions WHERE id = %s AND match_id = %s);
        """, (match_id_, id_, reaction, match_id_, id_))
        '''

    conn.commit()


    '''
    c.execute(f
    INSERT INTO reactions (reactions_id, id, match_id, reaction)
    VALUES (nextval('reactions_id_seq'), %s, %s, %s)
    ON CONFLICT (id, match_id) DO UPDATE
    SET reaction = EXCLUDED.reaction
    WHERE reactions.reaction != EXCLUDED.reaction
    , (id_, match_id_, reaction))
    ##########
    c.execute(f
    INSERT INTO reactions (reactions_id, id, match_id, reaction)
    VALUES (nextval('reactions_id_seq'), %s, %s, %s)
    ON CONFLICT (id, match_id) DO UPDATE
    SET reaction = EXCLUDED.reaction
    WHERE reactions.reaction != EXCLUDED.reaction
    , (match_id_, id_, reaction))
    ##########
    conn.commit()
    '''


def update_reaction(conn, c, id_, match_id_, reaction):
    c.execute(f'''
    UPDATE reactions
    SET reaction = %s
    WHERE reaction != 2 AND id = %s AND match_id = %s
    ''', (reaction, id_, match_id_))
    c.execute(f'''
    UPDATE reactions
    SET reaction = %s
    WHERE reaction != 2 AND match_id = %s AND id = %s
    ''', (reaction, id_, match_id_))
    conn.commit()


def find_like(conn, c, id_):
    c.execute('''
                SELECT id
                FROM reactions
                WHERE match_id = %s AND reaction = 1
                LIMIT 1
                ''', (id_,))
    return c.fetchone()


def admin(conn, c):
    c.execute('''DROP TABLE users; CREATE TABLE IF NOT EXISTS users
                 (id BIGSERIAL PRIMARY KEY, gender integer, campus text, program text, course text, frd_goal boolean, dts_goal boolean, ntw_goal boolean, gender_goals integer, photo_id text, ad_text text)''')
    conn.commit()
    c.execute('''DROP TABLE reactions; DROP SEQUENCE IF EXISTS reactions_id_seq CASCADE; CREATE SEQUENCE reactions_id_seq;
                 CREATE TABLE IF NOT EXISTS reactions
                 (reactions_id BIGSERIAL PRIMARY KEY, id bigint, match_id bigint, reaction integer)''')
    conn.commit()

def restart_reactions(conn, c):
    c.execute('''DROP TABLE reactions; DROP SEQUENCE IF EXISTS reactions_id_seq CASCADE; CREATE SEQUENCE reactions_id_seq;
                 CREATE TABLE IF NOT EXISTS reactions
                 (reactions_id BIGSERIAL PRIMARY KEY, id bigint, match_id bigint, reaction integer)''')
    conn.commit()

def admin_displ_re(conn, c):
    c.execute("SELECT * FROM reactions")
    rows = c.fetchall()
    return rows

def admin_displ_users(conn, c):
    c.execute("SELECT * FROM users")
    rows = c.fetchall()
    return rows

def admin_displ_blacklist(conn, c):
    c.execute("SELECT * FROM blacklist")
    rows = c.fetchall()
    return rows

'''
    c.execute(
    SELECT users.id
    FROM users
    LEFT JOIN reactions ON (users.id = reactions.id AND users.id != %s AND (reactions.reaction != 0 AND reactions.reaction != 1 AND reactions.reaction != 2))
    WHERE (
    (users.gender_goals = %s OR users.gender_goals = 2) AND (users.gender = %s OR %s = 2) AND (users.frd_goal = %s OR users.dts_goal = %s OR users.ntw_goal = %s)
    )
    AND users.id NOT IN (SELECT reactions.match_id FROM reactions WHERE reactions.id = users.id) 
    LIMIT 10
    , (user_data[0], user_data[1], user_data[2], user_data[2], user_data[3], user_data[4], user_data[5],))
'''
