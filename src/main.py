# from src.routes.token.router import router as token_router
from src.routes.job_applications.router import router as job_applications_router
from src.routes.leaves.router import router as leaves_router
from src.routes.employees.router import router as employees_router
from src.routes.roles.router import router as roles_Router
from src.dependencies.auth0 import require_auth
from fastapi import Depends, FastAPI
from dotenv import load_dotenv

load_dotenv(dotenv_path=".env", override=True)


# Load .env.local for development
# if os.getenv("ENVIRONMENT") == "dev":


app = FastAPI(
    title="KodeAcross HR Management",
    version="1.0",
    description="A simple API server for HR Management",
)

# app.include_router(
#     token_router,
#     prefix="/token",
#     tags=["Token"],
# )
app.include_router(
    employees_router,
    prefix="/employee",
    tags=["Employee"],
    dependencies=[Depends(require_auth)]
)
app.include_router(
    roles_Router,
    prefix="/roles",
    tags=["Roles"],
    dependencies=[Depends(require_auth)]
)
app.include_router(
    leaves_router,
    prefix="/leaves",
    tags=["Leaves"],
    dependencies=[Depends(require_auth)]
)

app.include_router(
    job_applications_router,
    prefix="/job_applications",
    tags=["Job Applications"],
    dependencies=[Depends(require_auth)]
)
