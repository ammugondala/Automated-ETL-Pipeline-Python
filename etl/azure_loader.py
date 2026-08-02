from azure.storage.blob import BlobServiceClient
from etl.config import (
    UPLOAD_TO_AZURE,
    AZURE_STORAGE_CONNECTION_STRING,
    AZURE_CONTAINER_NAME,
    AZURE_BLOB_NAME,
)

def upload_to_blob(file_path):
    if not UPLOAD_TO_AZURE:
        print("Azure upload disabled.")
        return

    try:
        blob_service = BlobServiceClient.from_connection_string(
            AZURE_STORAGE_CONNECTION_STRING
        )

        container_client = blob_service.get_container_client(
            AZURE_CONTAINER_NAME
        )

        try:
            container_client.create_container()
        except:
            pass

        blob_client = container_client.get_blob_client(
            AZURE_BLOB_NAME
        )

        with open(file_path, "rb") as data:
            blob_client.upload_blob(data, overwrite=True)

        print("✅ File uploaded to Azure Blob Storage!")

    except Exception as e:
        print("Azure Upload Error:", e)