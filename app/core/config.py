from pydantic_settings import BaseSettings
from typing import Optional

class Settings(BaseSettings):
    PROJECT_NAME: str = "Task Manager API"
    VERSION: str = "1.0.0"
    API_V1_STR: str = "/api/v1"
    
    # JWT
    SECRET_KEY: str = "your-secret-key-here"  # Em produção, use uma chave segura
    ALGORITHM: str = "HS256"
    ACCESS_TOKEN_EXPIRE_MINUTES: int = 30
    
    # Database
    DATABASE_URL: str = "postgresql://postgres:postgres@db:5432/taskmanager"
    
    class Config:
        case_sensitive = True

settings = Settings() 