import sqlite3


class FilmDateBase:
    def __init__(self, db_file):

        self.conn = sqlite3.connect(db_file)
        self.cursor = self.conn.cursor()

        self.cursor.execute