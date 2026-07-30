from pydantic import BaseModel, EmailStr, Field


class StudentBase(BaseModel):
    name: str = Field(min_length=2, max_length=50)
    age: int = Field(ge=18, le=60)
    course: str = Field(min_length=2, max_length=50)
    email: EmailStr


class StudentCreate(StudentBase):
    pass


class StudentUpdate(StudentBase):
    pass


class StudentResponse(StudentBase):
    id: int

    class Config:
        from_attributes = True