import sqlite3
import pathlib
import os

conn = sqlite3.connect(os.path.join(pathlib.Path(__file__).parent, "pianos.db"))

def insert_into_table(records):
    conn.executemany(""
                     "insert into pianos(title, image_url, description, length, price)"
                     "values (?, ?, ?, ?, ?)",
                     records)
    conn.commit()
