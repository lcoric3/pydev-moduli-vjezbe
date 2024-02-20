import sqlite3


class FilmDateBase:
    def __init__(self, db_file):

        self.conn = sqlite3.connect(db_file)
        self.cursor = self.conn.cursor()

        self.cursor.execute("""
            CREATE TABLE IF NOT EXISTS filmovi(
                id INTEGER PRIMATY KEY AUTOINCREMENT,
                naslov TEXT,
                godina INTEGER,
                redatelj TEXT
                )
                """)
        self.conn.commit()

    def dodaj_film(self, naslov, godina, redatelj):
        self.cursor.execute("""
            INSERT INTO filmovi(naslov, godina, redatelj)
            VALUES (?, ?, ?)
        """, (naslov, godina, redatelj))
        self.conn.commit()
        return self.cursor.lastrowid
    
    def ukloni_film(self, film_id):
        self.cursor.execute("""
            DELETE FROM filmovi 
            WHERE id = ?
        """, (film_id,))
        self.conn.commit()
    
    def azuriraj_film(self, film_id, naslov, godina, redatelj):
        self.cursor.execute("""
            UPDATE filmovi
            SET naslov = ?, godina = ?, redatelj = ?
            WHERE id = ?
        """, (naslov, godina, redatelj, film_id))
        self.conn.commit()

    def zatvori_bazu(self):
        self.conn.close()
                            




              
                            
                            
                            
                            
                           

                            





