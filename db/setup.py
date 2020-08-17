import sqlite3


def create_table():
    conn = sqlite3.connect("pianos.db")
    c = conn.cursor()
    c.execute('''CREATE TABLE pianos
                 (title varchar, image_url text, description text, price varchar, length varchar)''')
    c.close()

def print_table_piano():
    conn = sqlite3.connect("pianos.db")
    c = conn.cursor()
    print("Printing rows......")
    for row in c.execute("select * from pianos"):
        print(row)
    c.close()

create_table()