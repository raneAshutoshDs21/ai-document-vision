import os
from dotenv import load_dotenv

load_dotenv()

class Settings:
    # App
    APP_ENV = os.getenv("APP_ENV", "development")

    # Azure Document Intelligence
    DOC_INTELLIGENCE_ENDPOINT = os.getenv("DOC_INTELLIGENCE_ENDPOINT")
    DOC_INTELLIGENCE_KEY = os.getenv("DOC_INTELLIGENCE_KEY")

    # Azure Vision
    VISION_ENDPOINT = os.getenv("VISION_ENDPOINT")
    VISION_KEY = os.getenv("VISION_KEY")

    # Azure OpenAI
    AZURE_OPENAI_ENDPOINT = os.getenv("AZURE_OPENAI_ENDPOINT")
    AZURE_OPENAI_API_KEY = os.getenv("AZURE_OPENAI_API_KEY")
    AZURE_OPENAI_DEPLOYMENT_NAME = os.getenv("AZURE_OPENAI_DEPLOYMENT_NAME")

    # Blob Storage
    AZURE_STORAGE_CONNECTION_STRING = os.getenv("AZURE_STORAGE_CONNECTION_STRING")
    BLOB_CONTAINER_RAW = os.getenv("BLOB_CONTAINER_RAW")
    BLOB_CONTAINER_PROCESSED = os.getenv("BLOB_CONTAINER_PROCESSED")


settings = Settings()
