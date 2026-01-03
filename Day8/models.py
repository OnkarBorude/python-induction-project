"""
Docstring for Day8.models
"""
from sqlalchemy import Column, Integer, String
from database_op import Base


class Employees(Base):
    __tablename__ = "employees"

    id=Column(Integer, primary_key=True, index=True)
    name= Column(String(50))
    salary=Column(Integer)
