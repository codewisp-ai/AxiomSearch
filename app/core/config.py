from pydantic_settings import BaseSettings, SettingsConfigDict

class Settings(BaseSettings):
    # App Config
    PORT: int = 8000
    HOST: str = "0.0.0.0"
    
    # API Keys (Pydantic will automatically validate their presence)
    GOOGLE_API_KEY: str
    TAVILY_API_KEY: str

    # Direct Pydantic to read from the local .env file
    model_config = SettingsConfigDict(
        env_file=".env", 
        env_file_encoding="utf-8",
        extra="ignore" # Prevents crashing if extra variables exist in .env
    )

# Instantiate a global settings object to import across modules
try:
    settings = Settings()
except Exception as e:
    print("\n❌ CONFIGURATION ERROR: Missing required environment variables in your .env file.")
    print("Please ensure GOOGLE_API_KEY and TAVILY_API_KEY are properly configured.\n")
    raise e