from fastapi import APIRouter
from config.db import db_dependency
from models.staff import Staff, DepartmentEnum
from models.students import Student

metrics_router = APIRouter()

@metrics_router.get("/metrics", tags=["metrics"])
async def get_metrics(db: db_dependency):
    staff = db.query(Staff).order_by(Staff.hire_date.desc()).first()
    student = db.query(Student).order_by(Student.registration_date.desc()).first()
    metrics = {
      "total_students": db.query(Student).count(),
      "total_staff": db.query(Staff).filter(Staff.is_active == True).count(),
      "total_teachers": db.query(Staff).filter(Staff.department == DepartmentEnum.teaching, Staff.is_active == True).count(),
      "total_marketing": db.query(Staff).filter(Staff.department == DepartmentEnum.marketing, Staff.is_active == True).count(),
      "total_commercial": db.query(Staff).filter(Staff.department == DepartmentEnum.commercial, Staff.is_active == True).count(),
      "last_staff_hire": staff,
      "last_student_registration": student,
    }
    return metrics