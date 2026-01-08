import sqlite3


class Database:
    def __init__(self):
        self.conn = sqlite3.connect("students.db")
        self.cursor = self.conn.cursor()
        self.create_table()

    def create_table(self):
        self.cursor.execute("""
            CREATE TABLE IF NOT EXISTS students (
                name TEXT PRIMARY KEY,
                score REAL
            )
        """)
        self.conn.commit()

    def add_student(self, name, score):
        self.cursor.execute(
            "INSERT OR REPLACE INTO students VALUES (?, ?)",
            (name, score)
        )
        self.conn.commit()

    def delete_student(self, name):
        self.cursor.execute("DELETE FROM students WHERE name = ?", (name,))
        self.conn.commit()

    def fetch_all(self):
        self.cursor.execute("SELECT * FROM students")
        return dict(self.cursor.fetchall())
