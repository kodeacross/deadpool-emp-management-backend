from fastapi import APIRouter, Depends, HTTPException, Path
import requests
from src.dependencies.auth0 import AUTH0_DOMAIN, require_auth

router = APIRouter()


@router.get("/all-roles")
async def get_all_roles(token_payload: dict = Depends(require_auth)):
    """
    Fetch all users from Auth0.
    """
    try:
        if "read:roles" not in token_payload["payload"].get("scope", "").split():
            raise HTTPException(
                status_code=403,
                detail="Insufficient permissions to read users."
            )
        headers = {
            # 'sub' contains the client ID
            "Authorization": f"Bearer {token_payload['access_token']}",
            "Content-Type": "application/json",
        }
        # Make a request to Auth0 Management API
        response = requests.get(
            f"https://{AUTH0_DOMAIN}/api/v2/roles",
            headers=headers,
            timeout=12
        )
        if response.status_code == 200:
            user_data = response.json()
            return user_data
        else:
            raise HTTPException(
                status_code=response.status_code,
                detail=f"Failed to fetch user metadata: {response.text}",
            )
    except requests.exceptions.RequestException as e:
        raise HTTPException(
            status_code=500,
            detail=f"An error occurred while fetching user data: {str(e)}",
        )


@router.get("/{role_id}/users")
async def get_employee(
    role_id: str = Path(..., title="The ID of the employee"),
    token_payload: dict = Depends(require_auth),  # Inject the token payload
):
    """
    Fetch employee information from Auth0 using the employee_id.
    """
    try:
        # Validate the required scope
        if "read:users" not in token_payload["payload"].get("scope", "").split():
            raise HTTPException(
                status_code=403,
                detail="Insufficient permissions to read users."
            )
        headers = {
            # 'sub' contains the client ID
            "Authorization": f"Bearer {token_payload['access_token']}",
            "Content-Type": "application/json",
        }
        # Make a request to Auth0 Management API
        response = requests.get(
            f"https://{AUTH0_DOMAIN}/api/v2/roles/{role_id}/users",
            headers=headers,
            timeout=12
        )
        if response.status_code == 200:
            user_data = response.json()
            return user_data
        else:
            raise HTTPException(
                status_code=response.status_code,
                detail=f"Failed to fetch user metadata: {response.text}",
            )
    except requests.exceptions.RequestException as e:
        raise HTTPException(
            status_code=500,
            detail=f"An error occurred while fetching user data: {str(e)}",
        )


@router.get("/{employee_id}/roles")
async def get_employee_roles(
    employee_id: str = Path(..., title="The ID of the employee"),
    token_payload: dict = Depends(require_auth),
):
    """
    Fetch employee roles from Auth0 using the employee_id.
    """
    try:
        # Validate the required scope
        print(token_payload["payload"].get("scope", ""))
        print(f"https://{AUTH0_DOMAIN}/api/v2/users/{employee_id}/roles")
        if "read:users" not in token_payload["payload"].get("scope", "").split():
            raise HTTPException(
                status_code=403,
                detail="Insufficient permissions to read users."
            )
        headers = {
            # 'sub' contains the client ID
            "Authorization": f"Bearer {token_payload['access_token']}",
            "Content-Type": "application/json",
        }
        # Make a request to Auth0 Management API
        response = requests.get(
            f"https://{AUTH0_DOMAIN}/api/v2/users/{employee_id}/roles",
            headers=headers,
            timeout=12
        )
        if response.status_code == 200:
            user_data = response.json()
            return user_data
        else:
            raise HTTPException(
                status_code=response.status_code,
                detail=f"Failed to fetch user metadata: {response.text}",
            )
    except requests.exceptions.RequestException as e:
        raise HTTPException(
            status_code=500,
            detail=f"An error occurred while fetching user data: {str(e)}",
        )
