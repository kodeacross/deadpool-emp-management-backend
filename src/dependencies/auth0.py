from fastapi import Depends
import jwt
from fastapi.security import HTTPBearer
from decouple import config
from src.custom_exceptions import UnableCredentialsException, BadCredentialsException

AUTH0_DOMAIN = config("NEXT_PUBLIC_AUTH0_DOMAIN")
API_AUDIENCE = config("NEXT_PUBLIC_AUDIENCE")
JWKS_URL = f"https://{AUTH0_DOMAIN}/.well-known/jwks.json"
ALGORITHMS = ["RS256"]
token_auth_scheme = HTTPBearer()


def verify_jwt(token: str):
    """Verify the JWT using JWKS."""
    try:
        jwks_client = jwt.PyJWKClient(JWKS_URL)
        jwt_signing_key = jwks_client.get_signing_key_from_jwt(
            token
        ).key

        payload = jwt.decode(
            token,
            jwt_signing_key,
            algorithms=ALGORITHMS,
            audience=API_AUDIENCE,
            issuer=f"https://{AUTH0_DOMAIN}/",
        )

    except jwt.exceptions.PyJWKClientError:
        raise UnableCredentialsException
    except jwt.exceptions.InvalidTokenError:
        raise BadCredentialsException
    return {"payload": payload, "access_token": token}


def require_auth(token: str = Depends(token_auth_scheme)):
    """Require and validate the Auth0 access token."""
    return verify_jwt(token.credentials)
