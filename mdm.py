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
        try:
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
            self.db.commit()
        except sqlite3.Error as e:
            print(e)

    def add(self, path, length, e, s, g, m, d):
        try:
            self.c.execute("""
                INSERT INTO music
                (path, length, e, s, g, m, d, fix)
                VALUES
                (?, ?, ?, ?, ?, ?, ?, 0)""",
                (path, length, e, s, g, m, d)
            )
            self.db.commit()
        except sqlite3.Error as e:
            print(e)

    def delete(self, id):
        try:
            self.c.execute("""
                DELETE FROM music
                WHERE id = ?""",
                (id, )
            )
        except sqlite3.Error as e:
            print(e)

    def reeval(self, id, e, s, g, m, d):
        try:
            self.c.execute("""
                UPDATE music
                SET e = ?, s = ?, g = ?, m = ?, d = ?, fix = 0
                WHERE id = ?""",
                (e, s, g, m, d, id)
            )
            self.db.commit()
        except sqlite3.Error as e:
            print(e)

    def mark(self, id):
        try:
            self.c.execute("""
                UPDATE music
                SET fix = 1
                WHERE id = ?""",
                (id, )
            )
            self.db.commit()
        except sqlite3.Error as e:
            print(e)

    def markedq(self):
        try:
            self.c.execute("""
                SELECT *
                FROM music
                WHERE fix = 1
            """)
            return self.c.fetchall()
        except sqlite3.Error as e:
            print(e)

    def defaultq(self, et, st, gt, mt, dt, amount):
        try:
            self.c.execute("""
                SELECT rowid, path, length
                FROM music
                ORDER BY (e - ?)*(e - ?) + (s - ?)*(s - ?) + (g - ?)*(g - ?) + (m - ?)*(m - ?) + (d - ?)*(d - ?); """,
                (et, et, st, st, gt, gt, mt, mt, dt, dt)
            )
            return self.c.fetchmany(amount)
        except sqlite3.Error as e:
            print(e)
