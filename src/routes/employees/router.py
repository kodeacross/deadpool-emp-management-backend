from fastapi import APIRouter, Depends, HTTPException, Path, Request
import requests
from src.dependencies.auth0 import AUTH0_DOMAIN,  require_auth

router = APIRouter()


@router.get("/all")
async def get_all_users(token_payload: dict = Depends(require_auth)):
    """
    Fetch all users from Auth0.
    """
    try:
        # return token_payload
        if "read:users" not in token_payload["payload"].get("scope", "").split() and "read:user_idp_tokens" not in token_payload["payload"].get("scope", "").split():
            raise HTTPException(
                status_code=403,
                detail="Insufficient permissions to read users."
            )
        headers = {
            "Authorization": f"Bearer {token_payload['access_token']}",
            "Content-Type": "application/json",
        }
        # Make a request to Auth0 Management API
        response = requests.get(
            f"https://{AUTH0_DOMAIN}/api/v2/users",
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


@ router.get("/{employee_id}")
async def get_employee(
    employee_id: str = Path(..., title="The ID of the employee"),
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
            f"https://{AUTH0_DOMAIN}/api/v2/users/{employee_id}",
            headers=headers,
            timeout=12
        )
        if response.status_code == 200:
            user_data = response.json()
            user_metadata = user_data.get("user_metadata", {})
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
