import sqlite3 as sq


async def db_start():
    global db, cur

    db = sq.connect("sqlite.db")
    cur = db.cursor()

    cur.execute("CREATE TABLE IF NOT EXISTS users("
                "id INT PRIMARY KEY, "
                "username TEXT, "
                "first_name TEXT, "
                "last_name TEXT)")
    db.commit()


async def add_user(user_id, user_username, user_first_name, user_last_name):
    user = cur.execute(f"SELECT 1 FROM users WHERE id == {user_id}").fetchone()
    if not user:
        cur.execute("INSERT INTO users VALUES(?, ?, ?, ?)", (user_id, user_username, user_first_name, user_last_name))
        db.commit()