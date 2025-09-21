from pydantic_settings import BaseSettings, SettingsConfigDict

# Settings class for environment configuration.
class Settings(BaseSettings):
    POSTGRES_URL :str
    DATABASE_URL: str
    TEST_POSTGRES_URL: str

    model_config=SettingsConfigDict(
        env_file="./.env",
        extra="ignore"
    )

# Create a global settings instance.
settings = Settings()