import psycopg2

conn = psycopg2.connect(
    dbname="users",
    user="postgres",
    password="passmr",
    host="158.160.134.127",
    port = 5432
)
c = conn.cursor()
c.execute(f'DELETE FROM users')
c.execute(f'DELETE FROM reactions')
conn.commit()
conn.close()
