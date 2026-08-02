from dotenv import load_dotenv
import os

# Load values from .env file
load_dotenv()

# Store values in Python variables
CSV_PATH = os.getenv("CSV_PATH")
DB_NAME = os.getenv("DB_NAME")
REPORT_FOLDER = os.getenv("REPORT_FOLDER")
LOG_FOLDER = os.getenv("LOG_FOLDER")
EMAIL = os.getenv("EMAIL")
PASSWORD = os.getenv("PASSWORD")
UPLOAD_TO_AZURE = os.getenv("UPLOAD_TO_AZURE", "false").lower() == "true"

AZURE_STORAGE_CONNECTION_STRING = os.getenv("AZURE_STORAGE_CONNECTION_STRING")

AZURE_CONTAINER_NAME = os.getenv("AZURE_CONTAINER_NAME")

AZURE_BLOB_NAME = os.getenv("AZURE_BLOB_NAME")
READ_FROM_AZURE_SQL = os.getenv("READ_FROM_AZURE_SQL", "false").lower() == "true"

AZURE_SQL_SERVER = os.getenv("AZURE_SQL_SERVER")
AZURE_SQL_DATABASE = os.getenv("AZURE_SQL_DATABASE")
AZURE_SQL_USERNAME = os.getenv("AZURE_SQL_USERNAME")
AZURE_SQL_PASSWORD = os.getenv("AZURE_SQL_PASSWORD")
AZURE_SQL_TABLE = os.getenv("AZURE_SQL_TABLE")
AZURE_SQL_DRIVER = os.getenv("AZURE_SQL_DRIVER")