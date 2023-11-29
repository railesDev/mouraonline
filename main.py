import sys
import asyncio
import logging
import sqlite3
import psycopg2
import dboper

import handlers
import bot

logging.basicConfig(level=logging.INFO)


# Connect to the SQLite database and create tables if they don't exist
# conn = sqlite3.connect('users.db')
conn = psycopg2.connect(
    dbname="users",
    user="postgres",
    password="passmr",
    host="158.160.134.127",
    port = 5432
)
c = conn.cursor()
dboper.create_users(conn, c)
dboper.create_reactions(conn, c)



async def main():
    await bot.dp.start_polling(bot.moura)


if __name__ == '__main__':
    logging.basicConfig(level=logging.INFO, stream=sys.stdout)
    try:
        asyncio.run(main())
    except (KeyboardInterrupt, SystemExit):
        logging.info("Bot stopped!")
