import sqlite3

###     Legend

# e- stands for energy
# s- stands for size
# g- stands for gloom
# m- stands for mystery
# d- stands for danger

# -t stands for target

db = sqlite3.connect('music.db')
c = db.cursor()

def clean():
    c.execute("""DROP TABLE IF EXISTS music""")
    c.execute("""
        CREATE TABLE music (
        id INTEGER PRIMARY KEY,
        path TEXT NOT NULL,
        length INTEGER,
        e INTEGER NOT NULL,
        s INTEGER NOT NULL,
        g INTEGER NOT NULL,
        m INTEGER NOT NULL,
        d INTEGER NOT NULL,
        fix INTEGER
        )
    """)

def close():
    db.close()



def add(path, length, e, s, g, m, d):
    c.execute("""
        INSERT INTO music
        (path, length, e, s, g, m, d, fix)
        values
        (?, ?, ?, ?, ?, ?, ?, 0)""",
        (path, length, e, s, g, m, d)
    )

def defaultq(et, st, gt, mt, dt, amount):
    c.execute("""
        SELECT rowid, path, length
        FROM music
        ORDER BY (e - ?)*(e - ?) + (s - ?)*(s - ?) + (g - ?)*(g - ?) + (m - ?)*(m - ?) + (d - ?)*(d - ?); """,
        (et, et, st, st, gt, gt, mt, mt, dt, dt)
    )
    return c.fetchmany(amount)
