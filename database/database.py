import os
import sqlite3

class DatabaseManager:
    def __init__(self, database_path=os.path.join(os.getcwd(), 'database\coords_images.db')):
        self.database_path = database_path
        self.con = None
        self.cursor = None

    def connect(self):
        if not os.path.exists(self.database_path):
            print(f"Creating SQLite file at: {self.database_path}")
            open(self.database_path, 'a').close()
        self.con = sqlite3.connect(self.database_path)
        self.cursor = self.con.cursor()      

    def close(self):
        if self.con:
            self.con.close()

    def setup(self):
        self.connect()

        self.cursor.execute("""
            CREATE TABLE IF NOT EXISTS CoordsImages(
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                coords TEXT UNIQUE,
                image BLOB NOT NULL
            )
        """)
        self.con.commit()

    def insert_data(self, coords: tuple, image: bytes):
        coords_str = str(coords) 
        try:
            self.cursor.execute("INSERT INTO CoordsImages (coords, image) VALUES (?, ?)", (coords_str, image))
            self.con.commit()
            print("Data inserted successfully.")
        except sqlite3.Error as e:
            print(f"Error inserting data into the database: {e}")
