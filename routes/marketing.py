from fastapi import APIRouter
from config.db import db_dependency
from models.staff import Staff, DepartmentEnum
from schemas import StaffBase

marketing_router = APIRouter()

@marketing_router.get("/staff/marketing", tags=["marketing"])
async def get_marketing(db: db_dependency) -> list[StaffBase]:
    marketing = db.query(Staff).filter(Staff.department == DepartmentEnum.marketing, Staff.is_active == True).all()
    return marketing