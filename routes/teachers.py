from fastapi import APIRouter
from config.db import db_dependency
from models.staff import Staff, DepartmentEnum
from schemas import StaffBase

teachers_router = APIRouter()

@teachers_router.get("/staff/teachers", tags=["teachers"])
async def get_teachers(db: db_dependency):
    teachers = db.query(Staff).filter(Staff.department == DepartmentEnum.teaching, Staff.is_active == True).all()
    return teachers