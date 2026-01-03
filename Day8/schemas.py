"""
Docstring for Day8.schemas
"""
from pydantic import BaseModel

class EmployeesCreate(BaseModel):
    """
    Docstring for EmployeesCreate
    """
    name: str
    salary: int

class EmployeesResponse(BaseModel):
    id: int
    name: str
    salary: int

    class Config:
        orm_mode = True
