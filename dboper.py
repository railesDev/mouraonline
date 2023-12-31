import random


def create_users(conn, c):
    c.execute('''CREATE TABLE IF NOT EXISTS users
                 (id BIGSERIAL PRIMARY KEY, gender integer, campus text, program text, course text, frd_goal boolean, dts_goal boolean, ntw_goal boolean, gender_goals integer, photo_id text, ad_text text)''')
    conn.commit()


def create_reactions(conn, c):
    c.execute('''CREATE TABLE IF NOT EXISTS reactions
                 (id BIGSERIAL PRIMARY KEY, match_id bigint, reaction integer)''')
    conn.commit()


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
    WHERE reactions.match_id = users.id AND reactions.id = %s
    )
    AND users.id NOT IN (SELECT reactions.match_id FROM reactions WHERE reactions.id = users.id) 
    LIMIT 10''', (user_data[0], user_data[1], user_data[2], user_data[2], user_data[3], user_data[4], user_data[5], user_data[0],))
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
    c.execute(f'''
    INSERT INTO reactions (id, match_id, reaction)
    VALUES (%s, %s, %s)
    ON CONFLICT DO NOTHING
    ''', (id_, match_id_, reaction))
    conn.commit()


def update_reaction(conn, c, id_, reaction):
    c.execute(f'''
    UPDATE reactions
    SET reaction = %s
    WHERE reaction != 2 AND id = %s
    ''', (reaction, id_))
    c.execute(f'''
    UPDATE reactions
    SET reaction = %s
    WHERE reaction != 2 AND match_id = %s
    ''', (reaction, id_))
    conn.commit()


def find_like(conn, c, id_):
    c.execute('''
                SELECT id
                FROM reactions
                WHERE match_id = %s AND reaction = 1
                LIMIT 1
                ''', (id_,))
    return c.fetchone()

