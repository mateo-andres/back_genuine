from fastapi import APIRouter, HTTPException
from config.db import db_dependency
from models.staff import Staff
from schemas import StaffBase
from config.auth import get_current_user
from fastapi import Depends

staff_router = APIRouter()

@staff_router.post("/staff" ,tags=["staff"])
async def create_staff(db: db_dependency, staff: StaffBase) -> StaffBase:
    new_staff = Staff(**staff.model_dump())
    db.add(new_staff)
    db.commit()
    db.refresh(new_staff)
    return new_staff

@staff_router.get("/staff" ,tags=["staff"])
async def get_staff(db: db_dependency, current_user=Depends(get_current_user)) -> list[StaffBase]:
    staff = db.query(Staff).filter(Staff.is_active == True).all()
    return staff

@staff_router.get("/staff/{staff_id}" ,tags=["staff"])
async def get_staff(db: db_dependency, staff_id: int) -> StaffBase:
    staff = db.query(Staff).filter(Staff.id == staff_id).first()
    if not staff:
        raise HTTPException(status_code=404, detail="Staff not found")
    return staff

@staff_router.put("/staff/{staff_id}" ,tags=["staff"])
async def update_staff(db: db_dependency, staff_id: int, staff: StaffBase) -> StaffBase:
    staff_to_update = db.query(Staff).filter(Staff.id == staff_id).first()
    if not staff_to_update:
        raise HTTPException(status_code=404, detail="Staff not found")

    staff_to_update.first_name = staff.first_name
    staff_to_update.last_name = staff.last_name
    staff_to_update.email = staff.email
    staff_to_update.department = staff.department
    db.commit()
    db.refresh(staff_to_update)
    return staff_to_update

@staff_router.delete("/staff/{staff_id}" ,tags=["staff"])
async def delete_staff(db: db_dependency, staff_id: int) -> StaffBase:
    staff_to_delete = db.query(Staff).filter(Staff.id == staff_id).first()
    if not staff_to_delete:
        raise HTTPException(status_code=404, detail="Staff not found")

    staff_to_delete.is_active = False
    db.commit()
    db.refresh(staff_to_delete)
    return staff_to_delete