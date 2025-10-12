from sqlalchemy import Column, Integer, String, Date, Boolean, Enum, func
from config.db import Base
import enum


class DepartmentEnum(str, enum.Enum):
    teaching = "teaching"
    commercial = "commercial"
    marketing = "marketing"


class Staff(Base):
    __tablename__ = "staff"
    
    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    first_name = Column(String(100), nullable=False)
    last_name = Column(String(100), nullable=False)
    email = Column(String(255), unique=True, nullable=False, index=True)
    department = Column(Enum(DepartmentEnum), nullable=False)
    hire_date = Column(Date, default=func.now(), nullable=False)
    is_active = Column(Boolean, default=True, nullable=False)