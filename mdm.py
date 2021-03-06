import sqlite3

###     Legend

# e- stands for energy
# s- stands for size
# g- stands for gloom
# m- stands for mystery
# d- stands for danger

# -t stands for target
# -x stands for maximum
# -n stands for minimum
# -w stands for weight

class MusicDataManager:
    def __init__(self, dbfile):
        try:
            self._database = sqlite3.connect(dbfile)
            self._cursor = self._database.cursor()
        except sqlite3.Error as error:
            print(error)
    def __del__(self):
        self._database.close()

    def clean(self):
        try:
            self._cursor.execute("""DROP TABLE IF EXISTS music""")
            self._cursor.execute("""
                CREATE TABLE music (
                id INTEGER PRIMARY KEY,
                path TEXT NOT NULL,
                e INTEGER NOT NULL,
                s INTEGER NOT NULL,
                g INTEGER NOT NULL,
                m INTEGER NOT NULL,
                d INTEGER NOT NULL,
                fix INTEGER
                )
            """)
            self._database.commit()
        except sqlite3.Error as e:
            print(e)

    def add(self, path, e, s, g, m, d):
        try:
            self._cursor.execute("""
                INSERT INTO music
                (path, e, s, g, m, d, fix)
                VALUES
                (?, ?, ?, ?, ?, ?, 0)""",
                (path, e, s, g, m, d)
            )
            self._database.commit()
        except sqlite3.Error as e:
            print(e)

    def delete(self, id):
        try:
            self._cursor.execute("""
                DELETE FROM music
                WHERE id = ?""",
                (id, )
            )
        except sqlite3.Error as e:
            print(e)

    def update(self, id, e, s, g, m, d):
        try:
            self._cursor.execute("""
                UPDATE music
                SET e = ?, s = ?, g = ?, m = ?, d = ?, fix = 0
                WHERE id = ?""",
                (e, s, g, m, d, id)
            )
            self._database.commit()
        except sqlite3.Error as e:
            print(e)

    def mark(self, id):
        try:
            self._cursor.execute("""
                UPDATE music
                SET fix = 1
                WHERE id = ?""",
                (id, )
            )
            self._database.commit()
        except sqlite3.Error as e:
            print(e)

    def marked(self):
        try:
            self._cursor.execute("""
                SELECT *
                FROM music
                WHERE fix = 1
            """)
            return self._cursor.fetchall()
        except sqlite3.Error as e:
            print(e)

    def queue(self, et, en, ex, ew, st, sn, sx, sw, gt, gn, gx, gw, mt, mn, mx, mw, dt, dn, dx, dw, amount):
        try:
            self._cursor.execute("""
                SELECT *
                FROM music
                WHERE
                e >= ? AND e <= ? AND
                s >= ? AND s <= ? AND
                g >= ? AND g <= ? AND
                m >= ? AND m <= ? AND
                d >= ? AND d <= ?
                ORDER BY
                (e - ?)*(e - ?)*? +
                (s - ?)*(s - ?)*? +
                (g - ?)*(g - ?)*? +
                (m - ?)*(m - ?)*? +
                (d - ?)*(d - ?)*?; """,
                (en, ex, sn, sx, gn, gx, mn, mx, dn, dx,
                et, et, ew, st, st, sw, gt, gt, gw, mt, mt, mw, dt, dt, dw)
            )
            return self._cursor.fetchmany(amount)
        except sqlite3.Error as e:
            print(e)
