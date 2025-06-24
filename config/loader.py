from pydantic import AnyHttpUrl, SecretStr
from pydantic_settings import BaseSettings

class BotSettings(BaseSettings):
    TELEGRAM_BOT_TOKEN: SecretStr
    API_URL: AnyHttpUrl
    CHAT_ID: int

    class Config:
        env_file = ".env"
        env_file_encoding = "utf-8"

settings = BotSettings()
