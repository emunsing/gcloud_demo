from pydantic_settings import BaseSettings
from functools import lru_cache
import os

class Settings(BaseSettings):
    # Database settings
    SQL_USER: str
    SQL_PW: str
    SQL_DB_NAME: str
    SQL_DB_HOST: str
    SQL_DB_PORT: str

    # Google Cloud settings
    PROJECT_NAME: str = ""
    REGION: str = "us-west1"
    CONNECTION_NAME: str = ""
    IS_CLOUD_RUN: bool = False

    # API settings
    API_VERSION: str = "v1"
    DEBUG: bool = False

    @property
    def DB_URL(self) -> str:
        # Check if running in Cloud Run
        if self.IS_CLOUD_RUN:
            db_socket_dir = os.getenv("DB_SOCKET_DIR", "/cloudsql")
            return (
                f"postgresql://{self.SQL_USER}:{self.SQL_PW}@/"
                f"{self.SQL_DB_NAME}?host={db_socket_dir}/{self.INSTANCE_CONNECTION_NAME}"
            )
        else:
            return (
                f"postgresql://{self.SQL_USER}:{self.SQL_PW}@"
                f"{self.SQL_DB_HOST}:{self.SQL_DB_PORT}/{self.SQL_DB_NAME}"
            )

    class Config:
        env_file = f".env.{os.getenv('ENV', 'dev')}"
        extra = "ignore"


@lru_cache()
def get_settings() -> Settings:
    return Settings()

settings = get_settings()