from functools import lru_cache
from pathlib import Path

from dotenv import load_dotenv
from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    """Конфигурация проекта"""

    project_name: str = "movies"

    public_key: str

    redis_host: str = "127.0.0.1"
    redis_port: int = 6379
    redis_user: str = "app"
    redis_password: str
    cache_expire_in_seconds: int = 300

    elastic_host: str = "127.0.0.1"
    elastic_port: int = 9200

    page_size: int = 10
    page_number: int = 1

    request_limit_per_minute: int = 20

    model_config = SettingsConfigDict(
        env_file=Path(__file__).resolve().parent.parent.parent / ".env", extra='ignore'
    )


@lru_cache
def get_settings():
    load_dotenv()
    return Settings()


config = get_settings()
