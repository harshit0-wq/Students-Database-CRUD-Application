# EWB Internship Project - Students Database CRUD API

A complete backend assignment using **Python + FastAPI + SQLite**. It implements Create, Read, Update and Delete operations, validation, filtering, persistent storage, error handling, tests and Swagger API documentation.

> Uses only dummy records. Do not store real student personal information in a public repository.

## Project structure

```text
EWB_Student_CRUD_Project/
├── app/
│   ├── __init__.py
│   ├── main.py
│   ├── crud.py
│   ├── database.py
│   └── schemas.py
├── tests/test_api.py
├── seed.py
├── requirements.txt
├── .gitignore
└── README.md
```

## Setup

Requires Python 3.10+.

```bash
python -m venv .venv
# Windows: .venv\Scripts\activate
# macOS/Linux: source .venv/bin/activate
pip install -r requirements.txt
```

## Run

```bash
uvicorn app.main:app --reload
```

Open `http://127.0.0.1:8000/docs` for interactive Swagger UI. SQLite creates `students.db` automatically.

Optional dummy data:
```bash
python seed.py
```

## API
- `POST /students` - create a student
- `GET /students` - list all; optional `?name=` and `?course=` filters
- `GET /students/{student_id}` - retrieve one
- `PATCH /students/{student_id}` - update supplied fields
- `DELETE /students/{student_id}` - delete one

### Create example
```json
{
  "name": "Aarav Kumar",
  "date_of_birth": "2005-03-18",
  "email": "aarav@example.com",
  "phone": "+919876543210",
  "course": "B.Sc. Computer Science",
  "address": "Patna, Bihar",
  "enrollment_date": "2024-07-15"
}
```

### cURL examples
```bash
curl -X POST http://127.0.0.1:8000/students -H "Content-Type: application/json" -d '{"name":"Aarav Kumar","date_of_birth":"2005-03-18","email":"aarav@example.com"}'
curl http://127.0.0.1:8000/students
curl http://127.0.0.1:8000/students/1
curl -X PATCH http://127.0.0.1:8000/students/1 -H "Content-Type: application/json" -d '{"course":"BCA"}'
curl -X DELETE http://127.0.0.1:8000/students/1
```

## Tests
```bash
pytest -q
```

## Error handling and validation
- Unknown student ID returns HTTP 404.
- Duplicate email returns HTTP 409.
- Pydantic validates dates, email format, field lengths and phone characters.
- At least one contact method (email or phone) is required.
- SQL values are parameterized.

## GitHub submission
```bash
git init
git add .
git commit -m "Complete EWB student CRUD assignment"
git branch -M main
git remote add origin https://github.com/YOUR_USERNAME/ewb-student-crud.git
git push -u origin main
```

Then submit the repository link through the channel announced by the EWB trainer.

## Demonstration talking points
1. `FastAPI` routes receive and validate requests through Pydantic models.
2. `crud.py` contains database operations, keeping route code small.
3. `database.py` owns SQLite connection and schema creation.
4. SQLite persists data in `students.db`.
5. Swagger at `/docs` makes the CRUD flow easy to demonstrate.
6. Parameterized SQL prevents request values from being concatenated into SQL.

## Assignment coverage
This project covers all mandatory requirements: student ID, name, DOB, contact information, optional course/address/enrollment date, complete CRUD, SQLite persistence, validation, missing-record handling, organized source code and reproducible documentation. The Ollama AI extension is intentionally omitted because it is optional.
