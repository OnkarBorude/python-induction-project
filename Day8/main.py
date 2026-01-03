"""
Docstring for Day8.main
"""
from fastapi import FastAPI, Depends
from sqlalchemy.orm import Session
from database_op import Base, engine, get_db
from schemas import EmployeesResponse, EmployeesCreate
from typing import List


from models import Employees

Base.metadata.create_all(bind=engine)
app=FastAPI()
@app.get("/")
def home():
    """
    Docstring for home
    """
    return {"messege": "working fastapi+db properly"}


@app.post("/add-employee")
def add_employee(name: str, salary: int, db: Session = Depends(get_db)):
    emp = Employees(name=name, salary=salary)
    db.add(emp)
    db.commit()
    db.refresh(emp)
    return {"status": "success", "data": {"id": emp.id, "name": emp.name, "salary": emp.salary}}

@app.get("/employees/", response_model=List[EmployeesResponse])
def get_employees(db: Session = Depends(get_db)):
    return db.query(Employees).all()

@app.get("/employeesid/{emp_id}", response_model=EmployeesResponse)
def get_employee(emp_id: int, db: Session = Depends(get_db)):
    emp = db.query(Employees).filter(Employees.id == emp_id).first()
    if not emp:
        raise HTTPException(status_code=404, detail="Employee not found")
    return emp


@app.put("/employees/{emp_id}", response_model=EmployeesResponse)
def update_employee(emp_id: int, emp_data: EmployeesCreate, db: Session = Depends(get_db)):
    emp = db.query(Employees).filter(Employees.id == emp_id).first()
    if not emp:
        raise HTTPException(status_code=404, detail="Employee not found")
    emp.name = emp_data.name
    emp.salary = emp_data.salary
    db.commit()
    db.refresh(emp)
    return emp



@app.delete("/employees/{emp_id}", response_model=dict)
def delete_employee(emp_id: int, db: Session = Depends(get_db)):
    emp = db.query(Employees).filter(Employees.id == emp_id).first()
    if not emp:
        raise HTTPException(status_code=404, detail="Employee not found")
    db.delete(emp)
    db.commit()
    return {"status": "success", "message": f"Employee {emp_id} deleted"}