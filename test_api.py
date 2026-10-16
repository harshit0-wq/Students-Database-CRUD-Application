from pathlib import Path
from fastapi.testclient import TestClient
from app.main import app
from app.database import init_db, DB_PATH

def setup_function():
    if DB_PATH.exists(): DB_PATH.unlink()
    init_db()

def test_crud_flow():
    with TestClient(app) as client:
        payload={"name":"Test Student","date_of_birth":"2005-01-01","email":"test@example.com","course":"B.Sc."}
        r=client.post("/students",json=payload); assert r.status_code==201
        sid=r.json()["student_id"]
        assert client.get(f"/students/{sid}").status_code==200
        r=client.patch(f"/students/{sid}",json={"course":"BCA"}); assert r.json()["course"]=="BCA"
        assert client.get("/students?course=BCA").json()[0]["student_id"]==sid
        assert client.delete(f"/students/{sid}").status_code==204
        assert client.get(f"/students/{sid}").status_code==404
