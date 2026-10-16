import sqlite3
from pathlib import Path

DB_PATH = Path(__file__).resolve().parent.parent / "students.db"

def get_connection():
    conn = sqlite3.connect(DB_PATH, check_same_thread=False)
    conn.row_factory = sqlite3.Row
    conn.execute("PRAGMA foreign_keys = ON")
    return conn

def init_db():
    with get_connection() as conn:
        conn.execute("""
        CREATE TABLE IF NOT EXISTS students (
            student_id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            date_of_birth TEXT NOT NULL,
            email TEXT UNIQUE,
            phone TEXT,
            course TEXT,
            address TEXT,
            enrollment_date TEXT,
            CHECK (email IS NOT NULL OR phone IS NOT NULL)
        )
        """)
        conn.commit()
