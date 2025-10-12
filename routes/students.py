from fastapi import APIRouter, HTTPException
from config.db import db_dependency
from models.students import Student
from schemas import StudentBase

students_router = APIRouter()

@students_router.post("/students" ,tags=["students"])
async def create_student(db: db_dependency, student: StudentBase) -> StudentBase:
    new_student = Student(**student.model_dump())
    db.add(new_student)
    db.commit()
    db.refresh(new_student)
    return new_student

@students_router.get("/students" ,tags=["students"])
async def get_students(db: db_dependency) -> list[StudentBase]:
    students = db.query(Student).filter(Student.is_active == True).all()
    return students

@students_router.get("/students/{student_id}" ,tags=["students"])
async def get_students(db: db_dependency, student_id: int) -> StudentBase:
    students = db.query(Student).filter(Student.id == student_id).first()
    if not students:
        raise HTTPException(status_code=404, detail="Student not found")
    return students

@students_router.put("/students/{student_id}" ,tags=["students"])
async def update_student(db: db_dependency, student_id: int, student: StudentBase) -> StudentBase:
    student_to_update = db.query(Student).filter(Student.id == student_id).first()
    if not student_to_update:
        raise HTTPException(status_code=404, detail="Student not found")

    student_to_update.first_name = student.first_name
    student_to_update.last_name = student.last_name
    student_to_update.email = student.email
    student_to_update.date_of_birth = student.date_of_birth
    db.commit()
    db.refresh(student_to_update)
    return student_to_update

@students_router.delete("/students/{student_id}" ,tags=["students"])
async def delete_student(db: db_dependency, student_id: int) -> StudentBase:
    student_to_delete = db.query(Student).filter(Student.id == student_id).first()
    if not student_to_delete:
        raise HTTPException(status_code=404, detail="Student not found")

    student_to_delete.is_active = False
    db.commit()
    db.refresh(student_to_delete)
    return student_to_delete