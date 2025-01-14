from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    # ENV
    environment: str
    # AUTH0
    next_public_auth0_domain: str
    next_public_auth0_client_id: str
    next_public_auth0_client_secret: str
    next_public_audience: str
    # FAST API
    next_public_api_url: str
    next_public_redirect_uri: str
    next_public_api_public_key: str
    # SUPABASE
    next_public_supabase_url: str
    next_public_supabase_key: str

    class Config:
        env_file = ".env"


settings = Settings()
