import json

import uvicorn
from fastapi import FastAPI
from pydantic import BaseModel
from pymongo import MongoClient

app = FastAPI()

app.port = 7100

mongo_client = MongoClient('mongodb://localhost:27017')
hrdb = mongo_client["hrdb"]
employees_collection = hrdb["employees"]

class Employee(BaseModel):
    _id: str = ""
    identity: str | None = None
    fullname: str | None = None
    salary: float = 100_000
    iban: str | None = "TR1"
    fulltime: bool | None = False
    photo: str | None = None
    department: str | None = None


@app.get("/hr/api/v1/employees/{identity}")
async def get_employees(identity: str):
    return employees_collection.find_one({"_id": identity})


@app.get("/hr/api/v1/employees")
async def get_employees(skip: int, limit: int):
    return json.dumps([emp for emp in employees_collection.find({},{"_id": False})])


@app.delete("/hr/api/v1/employees/{identity}")
def fire_employee(identity: str):
    employee = employees_collection.find_one({"identity": identity})
    employees_collection.delete_one({"identity": identity})
    return employee

@app.post("/hr/api/v1/employees")
def hire_employee(employee: Employee):
    employee._id = employee.identity
    employees_collection.insert_one(employee.__dict__)
    return {"status": "ok"}

uvicorn.run(app, port=8100, host='0.0.0.0')
