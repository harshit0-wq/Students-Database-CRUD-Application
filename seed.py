from app.database import init_db, get_connection

SAMPLES=[
("Aarav Kumar","2005-03-18","aarav@example.com","+919876543210","B.Sc. Computer Science","Patna, Bihar","2024-07-15"),
("Ananya Singh","2006-11-02","ananya@example.com","+919123456780","BCA","Siwan, Bihar","2025-07-10"),
]
init_db()
with get_connection() as conn:
    conn.executemany("""INSERT OR IGNORE INTO students
    (name,date_of_birth,email,phone,course,address,enrollment_date) VALUES (?,?,?,?,?,?,?)""",SAMPLES)
    conn.commit()
print("Dummy students added.")
