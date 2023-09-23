import sqlite3 as sq

db = sq.connect('th.db')
cur = db.cursor()


async def db_start():
    cur.execute("CREATE TABLE IF NOT EXISTS accounts("
                "id INTEGER PRIMARY KEY AUTOINCREMENT,"
                " card_id TEXT)")
    cur.execute("CREATE TABLE IF NOT EXISTS items("
                "i_id INTEGER PRIMARY KEY AUTOINCREMENT, "
                "brand TEXT, "
                "desc TEXT, "
                "price TEXT, "
                "photo TEXT, "
                "name TEXT) ")
db.commit()


