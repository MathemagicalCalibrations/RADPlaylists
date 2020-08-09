import sqlite3

###     Legend

# e- stands for energy
# s- stands for size
# g- stands for gloom
# m- stands for mystery
# d- stands for danger

# -t stands for target

class MusicDataManager:
    def __init__(self, dbfile):
        try:
            self.db = sqlite3.connect(dbfile)
            self.c = self.db.cursor()
        except sqlite3.Error as error:
            print(error)
    def __del__(self):
        self.db.close()

    def clean(self):
        self.c.execute("""DROP TABLE IF EXISTS music""")
        self.c.execute("""
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

    def add(self, path, length, e, s, g, m, d):
        self.c.execute("""
            INSERT INTO music
            (path, length, e, s, g, m, d, fix)
            values
            (?, ?, ?, ?, ?, ?, ?, 0)""",
            (path, length, e, s, g, m, d)
        )

    def defaultq(self, et, st, gt, mt, dt, amount):
        self.c.execute("""
            SELECT rowid, path, length
            FROM music
            ORDER BY (e - ?)*(e - ?) + (s - ?)*(s - ?) + (g - ?)*(g - ?) + (m - ?)*(m - ?) + (d - ?)*(d - ?); """,
            (et, et, st, st, gt, gt, mt, mt, dt, dt)
        )
        return self.c.fetchmany(amount)
