import os
from pydantic import BaseSettings

class Settings(BaseSettings):
	DATABASE_URL: str = "sqlite:///./tasks.db"

settings = Settings()
