from typing import Annotated
from fastapi import Depends, HTTPException
from jose import ExpiredSignatureError, JWSError, JWTError, jws, jwt
from fastapi.security import HTTPBearer, HTTPAuthorizationCredentials
from decouple import config
from jose.exceptions import JWTClaimsError
import requests
from src.routes.token.models import UserClaims

AUTH0_DOMAIN = config("NEXT_PUBLIC_AUTH0_DOMAIN")
API_AUDIENCE = config("NEXT_PUBLIC_AUDIENCE")
JWKS_URL = f"https://{AUTH0_DOMAIN}/.well-known/jwks.json"
ALGORITHMS = ["RS256"]
token_auth_scheme = HTTPBearer()


def get_jwks():
    """Fetch JWKS from Auth0."""
    try:
        jwks_url = f"https://{AUTH0_DOMAIN}/.well-known/jwks.json"
        response = requests.get(jwks_url)
        response.raise_for_status()
        return response.json()
    except requests.RequestException as e:
        raise HTTPException(
            status_code=500, detail=f"Failed to fetch JWKS: {str(e)}"
        )


def verify_jwt(token: str):
    """Verify the JWT using JWKS."""
    jwks = get_jwks()
    unverified_header = jwt.get_unverified_header(token)

    rsa_key = {}
    for key in jwks["keys"]:
        if key["kid"] == unverified_header["kid"]:
            rsa_key = key
            break

    if not rsa_key:
        raise HTTPException(status_code=401, detail="Unable to find RSA key.")

    try:
        payload = jwt.decode(
            token,
            rsa_key,
            algorithms=ALGORITHMS,
            audience=API_AUDIENCE,
            issuer=f"https://{AUTH0_DOMAIN}/",
        )

        return {"payload": payload, "access_token": token}
    except JWTError as e:
        raise HTTPException(
            status_code=401, detail=f"Token is invalid: {str(e)}")


def require_auth(token: str = Depends(token_auth_scheme)):
    """Require and validate the Auth0 access token."""
    return verify_jwt(token.credentials)


def find_public_key(kid):
    jwks = get_jwks()["keys"]
    for key in jwks:
        if key["kid"] == kid:
            return key


def validate_token(credentials: Annotated[HTTPAuthorizationCredentials, Depends(token_auth_scheme)]):
    """Validate the token and return the user claims."""
    try:
        unverified_headers = jws.get_unverified_header(credentials.credentials)
        token_payload = jwt.decode(
            token=credentials.credentials,
            key=find_public_key(unverified_headers["kid"]),
            audience=API_AUDIENCE,
            algorithms="RS256",
        )
        return UserClaims(
            sub=token_payload["sub"], permissions=token_payload.get(
                "permissions", [])
        )
    except (
        ExpiredSignatureError,
        JWTError,
        JWTClaimsError,
        JWSError,
    ) as error:
        raise HTTPException(status_code=401, detail=str(error))
