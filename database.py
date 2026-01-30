import sqlite3

def connect_db():
    return sqlite3.connect("students.db")

def create_table():
    conn = connect_db()
    cursor = conn.cursor()
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS students (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT,
        roll_no TEXT,
        marks INTEGER,
        grade TEXT
    )
    """)
    conn.commit()
    conn.close()

create_table()