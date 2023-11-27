import psycopg2

conn = psycopg2.connect(
    dbname="users",
    user="railes",
    password="solviturambulando",
    host="localhost",
    port = 5432
)
c = conn.cursor()
c.execute(f'DELETE FROM users')
c.execute(f'DELETE FROM reactions')
conn.commit()
conn.close()
