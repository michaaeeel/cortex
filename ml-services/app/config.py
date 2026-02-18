from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    log_level: str = "INFO"
    model_path: str = "./models"
    anthropic_api_key: str = ""
    llm_model: str = "claude-sonnet-4-5-20250929"
    internal_api_key: str = ""

    class Config:
        env_prefix = "ML_"


settings = Settings()
