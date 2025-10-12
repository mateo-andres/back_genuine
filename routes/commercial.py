from fastapi import APIRouter
from config.db import db_dependency
from models.staff import Staff, DepartmentEnum
from schemas import StaffBase

commercial_router = APIRouter()

@commercial_router.get("/staff/commercial", tags=["commercial"])
async def get_commercial(db: db_dependency) -> list[StaffBase]:
    commercial = db.query(Staff).filter(Staff.department == DepartmentEnum.commercial, Staff.is_active == True).all()
    return commercial