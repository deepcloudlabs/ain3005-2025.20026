from typing import Optional

from flask import Flask, jsonify, request
from flask_cors import CORS
from flask_pydantic_openapi import FlaskPydanticOpenapi, Response, Request
from flask_socketio import SocketIO
from pydantic import BaseModel, Field, ConfigDict
from pymongo import MongoClient


# region Model -> Entity
class Employee(BaseModel):
    identity: str = Field(
        ...,
        min_length=11,
        max_length=11,
        description="Employee identity number",
        json_schema_extra={"example": "11111111110"},
    )
    fullname: str = Field(
        ...,
        min_length=3,
        description="Full name of employee",
        json_schema_extra={"example": "jack bauer"}
    )
    salary: float = Field(
        ...,
        ge=25000,
        description="Salary of employee",
        json_schema_extra={"example": 100_000.0}
    )
    iban: str = Field(
        ...,
        min_length=5,
        description="IBAN of Bank account",
        json_schema_extra={"example": "TR12345"},
    )
    department: str = Field(
        ...,
        min_length=1,
        description="Department of employee",
        json_schema_extra={"example": "SALES"},
    )
    birth_year: int = Field(
        ...,
        le=2008,
        description="Year of birth of employee",
        json_schema_extra={"example": 1986},
    )
    photo: Optional[str] = Field(
        default="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",
        description="Photo of employee",
        json_schema_extra={
            "example": "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"},
    )
    full_time: bool = Field(
        default=True,
        description="True if full-time, False otherwise",
    )

class EmployeeUpdate(BaseModel):
    model_config = ConfigDict(extra="forbid")

    fullname: Optional[str] = Field(default=None, min_length=1)
    iban: Optional[str] = Field(default=None, min_length=1)
    salary: Optional[float] = Field(default=None, ge=0)
    department: Optional[str] = Field(default=None, min_length=1)
    fulltime: Optional[bool] = None
    photo: Optional[str] = None


class StatusMessage(BaseModel):
    status: str = Field(..., description="Status of the operation")
    message: Optional[str] = Field(
        default=None,
        description="Optional human-readable detail about the status"
    )


# endregion

mongo_client = MongoClient("mongodb://localhost:27017")
hrdb = mongo_client["hrdb"]
employees_collection = hrdb["employees"]

hr_rest_api = Flask(__name__)
hr_rest_api.config["DEBUG"] = True
cors = CORS(hr_rest_api)
socketio = SocketIO(hr_rest_api, cors_allowed_origins="*")

api = FlaskPydanticOpenapi(
    "hr-api",
    title="HR REST API",
    version="0.0.1"
)


@hr_rest_api.route("/hr/api/v1/employees/<identity>", methods=['GET'])
@api.validate(
    resp=Response(HTTP_200=Employee, HTTP_404=StatusMessage),
    tags=["employees"]
)
def get_employees_by_identity(identity: str):
    """
    Get a single employee by identity.
    """
    employee = employees_collection.find_one({"identity": identity}, {"_id": 0})
    if not employee:
        return (
            jsonify(
                StatusMessage(
                    status="not_found",
                    message=f"Employee with identity {identity} not found"
                ).model_dump()
            ),
            404,
        )
    return jsonify(employee)

@hr_rest_api.route("/hr/api/v1/employees", methods=['GET'])
@api.validate(
    resp=Response(HTTP_200=None),
    tags=["employees"]
)
def get_employees():
    """
    List all employees.
    """
    employees = list(employees_collection.find({}, {"_id": 0}))
    return jsonify(employees)


@hr_rest_api.route("/hr/api/v1/employees", methods=['POST'])
@api.validate(
    body=Request(Employee),
    resp=Response(HTTP_201=StatusMessage, HTTP_409=StatusMessage),
    tags=["employees"]
)
def hire_employee():
    """
    Hire a new employee.
    """
    global socketio

    employee = request.get_json();
    print(employee)

    employee["_id"] = employee["identity"]

    if employees_collection.find_one({"_id": employee["_id"]}):
        return (
            jsonify(
                StatusMessage(
                    status="error",
                    message=f"Employee with identity {employee['identity']} already exists"
                ).model_dump()
            ),
            409,
        )

    employees_collection.insert_one(employee)
    socketio.emit("hire", employee)

    return (
        jsonify(
            StatusMessage(
                status="ok",
                message="Employee hired"
            ).model_dump()
        ),
        201,
    )


@hr_rest_api.route("/hr/api/v1/employees/<identity>", methods=['PUT', 'PATCH'])
@api.validate(
    body=Request(EmployeeUpdate),
    resp=Response(
        HTTP_200=StatusMessage,
        HTTP_400=StatusMessage,
        HTTP_404=StatusMessage
    ),
    tags=["employees"]
)
def update_employee(identity: str):
    """
    Update an existing employee.
    """
    payload = request.get_json()
    update_data = {k: v for k, v in payload.items() if v is not None}

    if not update_data:
        return (
            jsonify(
                StatusMessage(
                    status="error",
                    message="No valid fields provided to update"
                ).model_dump()
            ),
            400,
        )

    result = employees_collection.find_one_and_update(
        {"_id": identity},
        {"$set": update_data},
        upsert=False,
    )

    if not result:
        return (
            jsonify(
                StatusMessage(
                    status="not_found",
                    message=f"Employee with identity {identity} not found"
                ).model_dump()
            ),
            404,
        )

    return jsonify(
        StatusMessage(
            status="ok",
            message="Employee updated"
        ).model_dump()
    )


@hr_rest_api.route("/hr/api/v1/employees/<identity>", methods=['DELETE'])
@api.validate(
    resp=Response(HTTP_200=Employee, HTTP_404=StatusMessage),
    tags=["employees"]
)
def fire_employee(identity: str):
    """
    Fire (delete) an employee.
    """
    global socketio

    employee = employees_collection.find_one({"identity": identity}, {"_id": 0})
    if not employee:
        return (
            jsonify(
                StatusMessage(
                    status="not_found",
                    message=f"Employee with identity {identity} not found"
                ).model_dump()
            ),
            404,
        )

    employees_collection.delete_one({"identity": identity})
    socketio.emit("fire", employee)
    return jsonify(employee)


if __name__ == "__main__":
    api.register(hr_rest_api)
    socketio.run(hr_rest_api, port=7001)

