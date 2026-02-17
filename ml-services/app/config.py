from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    log_level: str = "INFO"
    model_path: str = "./models"

    class Config:
        env_prefix = "ML_"


settings = Settings()
