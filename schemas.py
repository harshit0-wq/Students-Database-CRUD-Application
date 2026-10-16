from datetime import date
from pydantic import BaseModel, EmailStr, Field, model_validator

class StudentBase(BaseModel):
    name: str = Field(min_length=2, max_length=100)
    date_of_birth: date
    email: EmailStr | None = None
    phone: str | None = Field(default=None, min_length=7, max_length=20, pattern=r"^[0-9+() -]+$")
    course: str | None = Field(default=None, max_length=100)
    address: str | None = Field(default=None, max_length=250)
    enrollment_date: date | None = None

    @model_validator(mode="after")
    def contact_required(self):
        if not self.email and not self.phone:
            raise ValueError("At least one contact field (email or phone) is required")
        return self

class StudentCreate(StudentBase):
    pass

class StudentUpdate(BaseModel):
    name: str | None = Field(default=None, min_length=2, max_length=100)
    date_of_birth: date | None = None
    email: EmailStr | None = None
    phone: str | None = Field(default=None, min_length=7, max_length=20, pattern=r"^[0-9+() -]+$")
    course: str | None = Field(default=None, max_length=100)
    address: str | None = Field(default=None, max_length=250)
    enrollment_date: date | None = None

class Student(StudentBase):
    student_id: int
