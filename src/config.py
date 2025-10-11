from pydantic_settings import BaseSettings,SettingsConfigDict
import os 
from dotenv import load_dotenv
load_dotenv(dotenv_path=os.path.join(os.path.dirname(__file__), ".env"))
class Settings(BaseSettings):
    DB_USER:str
    DB_PASSWORD:str 
    DB_HOST:str 
    DB_PORT:str
    DB_NAME:str
    MAIL_FROM:str 
    MAIL_USERNAME:str
    MAIL_PASS:str 
    MAIL_FROM_NAME:str 
    MAIL_SERVER:str 
    MAIL_PORT:int
    HOST_REDIS:str 
    PORT_REDIS:int 
    DB_REDIS:int 
    PASSWORD_REDIS:str
    JWT_SECRET:str
    JWT_ALGORITHM:str
    REDIS_BLACKLIST_PREFIX:str
    model_config = SettingsConfigDict(
        env_file=".env",
        extra="ignore"
    )
Config = Settings()
