from fastapi import APIRouter, HTTPException, Path

router = APIRouter()


@router.get("/")
async def get_employees():
    return {"message": "List of employees"}


@router.patch("/{employee_id}")
async def update_employee(employee_id: int = Path(..., title="The ID of the employee")):
    return {"message": f"Employee with ID {employee_id} updated"}
