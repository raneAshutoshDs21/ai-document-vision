from azure.storage.blob import BlobServiceClient
from config import settings
import uuid

class BlobStorageService:
    def __init__(self):
        self.client = BlobServiceClient.from_connection_string(
            settings.AZURE_STORAGE_CONNECTION_STRING
        )

    def upload_file(self, file_bytes: bytes, filename: str) -> str:
        container = self.client.get_container_client(settings.BLOB_CONTAINER_RAW)
        blob_name = f"{uuid.uuid4()}_{filename}"

        blob_client = container.get_blob_client(blob_name)
        blob_client.upload_blob(file_bytes, overwrite=True)

        return blob_client.url
