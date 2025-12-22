import Card from "./common/card";
import {useEmployees, useHrDispatcher, useSortDirections} from "../providers/hr-provider";
import Button from "./common/button";
import {useCallback, useEffect, useMemo} from "react";
import Photo from "./common/photo";
import callApi, {API_OPTIONS} from "../utils/api-utils";
import {ActionTypes} from "../reducers/hr-reducer";
import Badge from "./common/badge";

export default function EmployeesCard() {
    const employees = useEmployees();
    const hrDispatcher = useHrDispatcher();
    const sortDirections = useSortDirections();

    const handleError = useCallback(err => {
        hrDispatcher({type: ActionTypes.ON_ERROR, value: err});
    }, [hrDispatcher]);

    const fireEmployeeAtRow = useCallback((identityNo) => {
        callApi(`/${identityNo}`, API_OPTIONS.DELETE)
            .then(employee => {
                hrDispatcher({type: ActionTypes.ON_EMPLOYEE_FIRED_ON_ROW, value: employee})
            })
            .catch(handleError);
    }, [hrDispatcher, handleError]);

    const copyRow = useCallback(employee => {
        hrDispatcher({type: ActionTypes.ON_ROW_CLICKED, value: employee});
    }, [hrDispatcher]);

    const tableRows = useMemo(() => {
        console.log("Rendering rows...");
        return employees.map((employee, index) => (
                <tr key={employee.identity}
                    onClick={(_) => copyRow(employee)}>
                    <td>{index + 1}</td>
                    <td><Photo readOnly={true} value={'data:image/jpeg;base64,'.concat(employee.photo)}/></td>
                    <td>{employee.identity}</td>
                    <td>{employee.fullname}</td>
                    <td>{employee.salary}</td>
                    <td>{employee.iban}</td>
                    <td>{employee.birth_year}</td>
                    <td><Badge color={"bg-warning"} displayOnly={true} value={employee.department}/></td>
                    <td><Badge color={"bg-primary"} displayOnly={true}
                               value={employee.fulltime ? 'FULL-TIME' : 'PART-TIME'}/></td>
                    <td><Button color={"btn-danger"}
                                click={() => fireEmployeeAtRow(employee.identity)}
                                label={"Fire Employee"}/></td>
                </tr>
            )
        );
    }, [employees, copyRow, fireEmployeeAtRow]);
    const sortBy = useCallback(column => {
        hrDispatcher({type: ActionTypes.ON_SORTED, value: column});
    }, [hrDispatcher]);
    const retrieveEmployees = useCallback(async () => {
        console.log("retrieveEmployees() is created!")
        callApi("", API_OPTIONS.GET)
            .then(employees => {
                hrDispatcher({type: ActionTypes.ON_EMPLOYEES_RETRIEVED, value: employees})
            })
            .catch(handleError);
    }, [hrDispatcher, handleError]);

    useEffect(() => {
        const controller = new AbortController();
        const signal = controller.signal;
        fetch(`http://localhost:7001/hr/api/v1/employees`, {
            method: "GET",
            signal,
            headers: {"Accept": "application/json"}
        })
            .then(res => res.json())
            .then(employees => {
                hrDispatcher({type: ActionTypes.ON_EMPLOYEES_RETRIEVED, value: employees});
            }).catch(err => {
                if (err.name !== "AbortError") {
                    handleError(err);
                }
            }
        );
        return () => {
            controller.abort();
        }
    }, [hrDispatcher, handleError]);
    return (
        <Card title={"Employees"}>
            <Button color={"btn-success"}
                    click={retrieveEmployees}
                    label={"Retrieve Employees"}></Button>
            <table className={"table table-bordered table-responsive table-hover table-striped"}>
                <thead>
                <tr>
                    <th>No</th>
                    <th>Photo</th>
                    <th>Identity</th>
                    <th>Full Name</th>
                    <th><Button color={"btn-success"}
                                click={() => sortBy("salary")}
                                label={"Salary"}/></th>
                    <th>IBAN</th>
                    <th><Button color={"btn-primary"}
                                click={() => sortBy("birth_year")}
                                label={"Birth Year"}/></th>
                    <th>Department</th>
                    <th>Full-time?</th>
                    <th>Operations</th>
                </tr>
                </thead>
                <tbody>
                {
                    tableRows
                }
                </tbody>
            </table>
        </Card>
    );
}
