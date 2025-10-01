from pydantic_settings import BaseSettings, SettingsConfigDict
from pathlib import Path

_ENV_PATH = Path(__file__).resolve().parents[2] / ".env"  # src/.env

class EmailConfig(BaseSettings):
    MAIL_USERNAME: str
    MAIL_PASS: str
    MAIL_FROM: str
    MAIL_PORT: int = 587
    MAIL_SERVER: str = "smtp.gmail.com"
    MAIL_FROM_NAME: str = "Hospital"
    MAIL_USE_TLS: bool = True

    model_config = SettingsConfigDict(
        env_file=_ENV_PATH,
        env_file_encoding="utf-8",
        case_sensitive=True,
        extra="ignore"
    )
email_settings = EmailConfig()