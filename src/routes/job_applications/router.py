from fastapi import APIRouter, HTTPException, Path

router = APIRouter()


@router.get("/")
async def get_job_applications():
    return {"message": "List of leaves"}


@router.get("/{leave_id}")
async def get_leave(leave_id: int = Path(..., title="The ID of the leave")):
    return {"message": f"Leave with ID {leave_id}"}
