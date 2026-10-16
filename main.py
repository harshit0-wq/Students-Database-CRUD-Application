from contextlib import asynccontextmanager
from fastapi import FastAPI, Query, Response, status
from .database import init_db
from .schemas import Student, StudentCreate, StudentUpdate
from . import crud

@asynccontextmanager
async def lifespan(app: FastAPI):
    init_db(); yield

app=FastAPI(title="Students Database CRUD API", version="1.0.0", lifespan=lifespan)

@app.get("/", tags=["Health"])
def root():
    return {"message":"Student CRUD API is running", "docs":"/docs"}

@app.post("/students", response_model=Student, status_code=status.HTTP_201_CREATED, tags=["Students"])
def create_student(student:StudentCreate):
    return crud.create_student(student)

@app.get("/students", response_model=list[Student], tags=["Students"])
def list_students(name:str|None=Query(None), course:str|None=Query(None)):
    return crud.list_students(name, course)

@app.get("/students/{student_id}", response_model=Student, tags=["Students"])
def get_student(student_id:int):
    return crud.get_student(student_id)

@app.patch("/students/{student_id}", response_model=Student, tags=["Students"])
def update_student(student_id:int, student:StudentUpdate):
    return crud.update_student(student_id, student)

@app.delete("/students/{student_id}", status_code=status.HTTP_204_NO_CONTENT, tags=["Students"])
def delete_student(student_id:int):
    crud.delete_student(student_id)
    return Response(status_code=status.HTTP_204_NO_CONTENT)
