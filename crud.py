import sqlite3
from fastapi import HTTPException
from .database import get_connection
from .schemas import StudentCreate, StudentUpdate

def _row(row):
    return dict(row) if row else None

def create_student(data: StudentCreate):
    values=data.model_dump(mode="json")
    try:
        with get_connection() as conn:
            cur=conn.execute("""INSERT INTO students
            (name,date_of_birth,email,phone,course,address,enrollment_date)
            VALUES (:name,:date_of_birth,:email,:phone,:course,:address,:enrollment_date)""", values)
            conn.commit()
            return get_student(cur.lastrowid)
    except sqlite3.IntegrityError as e:
        if "UNIQUE" in str(e):
            raise HTTPException(409, "Email already exists")
        raise HTTPException(400, "Could not create student")

def list_students(name=None, course=None):
    sql="SELECT * FROM students WHERE 1=1"; params=[]
    if name:
        sql += " AND name LIKE ?"; params.append(f"%{name}%")
    if course:
        sql += " AND course LIKE ?"; params.append(f"%{course}%")
    sql += " ORDER BY student_id"
    with get_connection() as conn:
        return [dict(r) for r in conn.execute(sql, params).fetchall()]

def get_student(student_id:int):
    with get_connection() as conn:
        row=conn.execute("SELECT * FROM students WHERE student_id=?",(student_id,)).fetchone()
    if not row: raise HTTPException(404, "Student not found")
    return _row(row)

def update_student(student_id:int, data:StudentUpdate):
    current=get_student(student_id)
    changes=data.model_dump(exclude_unset=True, mode="json")
    merged={**current, **changes}
    if not merged.get("email") and not merged.get("phone"):
        raise HTTPException(422, "At least one contact field (email or phone) is required")
    if not changes: return current
    assignment=", ".join(f"{k}=?" for k in changes)
    try:
        with get_connection() as conn:
            conn.execute(f"UPDATE students SET {assignment} WHERE student_id=?", [*changes.values(),student_id])
            conn.commit()
    except sqlite3.IntegrityError:
        raise HTTPException(409, "Email already exists")
    return get_student(student_id)

def delete_student(student_id:int):
    get_student(student_id)
    with get_connection() as conn:
        conn.execute("DELETE FROM students WHERE student_id=?",(student_id,)); conn.commit()
