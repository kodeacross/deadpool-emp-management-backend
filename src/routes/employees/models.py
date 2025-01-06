from typing import List, Optional
from pydantic import BaseModel


class AddressModel(BaseModel):
    """
    A model for address
    """
    street: Optional[str] = None
    city: Optional[str] = None
    state: Optional[str] = None
    zip_code: Optional[str] = None
    country: Optional[str] = None


class CompanyModel(BaseModel):
    """
    A model for company details.
    """
    company_name: Optional[str] = None


class WorkHistory(BaseModel):
    """
    A model for work history
    """
    company: Optional[CompanyModel] = None
    position: Optional[str] = None
    start_date: Optional[str] = None
    end_date: Optional[str] = None
    department: Optional[str] = None
    title: Optional[str] = None
    salary: Optional[int] = None


class EmployeesMetadataModel(BaseModel):
    """
    A model for employees metadata.
    """
    last_name: Optional[str] = None
    first_name: Optional[str] = None
    middle_name: Optional[str] = None
    address: Optional[AddressModel] = None
    contact_number: Optional[str] = None
    department: Optional[str] = None
    dob: Optional[str] = None
    marital_status: Optional[str] = None


class EmployeeModel(BaseModel):
    """
    A model for employees auth0 data.
    """
    user_id: str
    email: str
    email_verified: bool
    last_password_reset: Optional[str] = None
    user_metadata: EmployeesMetadataModel
    updated_at: str
    created_at: str
    picture: str


class EmployeeDatabaseModel(BaseModel):
    """
    A model for employee data stored in the database.
    """
    id: str
    auth0_id: str
    email: str
    roles: List[str]


class EmployeeResponse(BaseModel):
    """
    A model for employee response.
    """
    employee: EmployeeModel
    work_history: Optional[WorkHistory] = None


class EmployeeUpdateRequest(BaseModel):
    """
    A model for employee update request.
    """
    last_name: Optional[str] = None
    first_name: Optional[str] = None
    middle_name: Optional[str] = None
    address: Optional[AddressModel] = None
    contact_number: Optional[str] = None
    email: Optional[str] = None
    dob: Optional[str] = None
    marital_status: Optional[str] = None
    work_history: Optional[WorkHistory] = None
