from pydantic import BaseModel
from datetime import date, datetime
from models.staff import DepartmentEnum

class StudentBase (BaseModel):
    first_name: str
    last_name: str
    email: str
    date_of_birth: date
    registration_date: datetime
    is_active: bool


class StaffBase (BaseModel):
    first_name: str
    last_name: str
    email: str
    department: DepartmentEnum
    hire_date: date
    is_active: bool