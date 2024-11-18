from fastapi import APIRouter, HTTPException, Path

router = APIRouter()


@router.get("/{leave_id}")
async def get_leave(leave_id: int = Path(..., title="The ID of the leave")):
    return {"message": f"Leave with ID {leave_id}"}


@router.patch("/{leave_id}")
async def update_leave(leave_id: int = Path(..., title="The ID of the leave")):
    return {"message": f"Leave with ID {leave_id}"}
