from fastapi import Depends, FastAPI
from src.routes.employees.router import router as employees_router
from src.routes.leaves.router import router as leaves_router
from src.routes.job_applications.router import router as job_applications_router

app = FastAPI(
    title="KodeAcross HR Management",
    version="1.0",
    description="A simple API server for HR Management",
)

app.include_router(
    employees_router,
    prefix="/employees",
    tags=["Employees"],
    # dependencies=[Depends(auth.require_user)],
)

app.include_router(
    leaves_router,
    prefix="/leaves",
    tags=["Leaves"],
    # dependencies=[Depends(auth.require_user)],
)

app.include_router(
    job_applications_router,
    prefix="/job_applications",
    tags=["Job Applications"],
    # dependencies=[Depends(auth.require_user)],
)
