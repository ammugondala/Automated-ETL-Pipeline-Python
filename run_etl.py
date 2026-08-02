from etl.azure_sql_reader import read_from_azure_sql
from etl.config import READ_FROM_AZURE_SQL
from etl.azure_loader import upload_to_blob
from etl.html_report import generate_html_report
from etl.config import EMAIL, PASSWORD
from etl.config import CSV_PATH
from etl.emailer import send_email
from etl.excel_report import create_excel_report
from etl.logger import logger
from etl.viz import create_visualizations
from etl.extractor import extract_data
from etl.transformer import transform_data
from etl.loader import load_data

print("========== ETL PIPELINE ==========\n")
logger.info("ETL Pipeline Started")

# Extract
# Extract
if READ_FROM_AZURE_SQL:
    df = read_from_azure_sql()
else:
    df = extract_data(CSV_PATH)
# Transform
df = transform_data(df)

# Load
load_data(df)
create_visualizations(df)
generate_html_report(df)
create_excel_report(df)
upload_to_blob("reports/Employee_Report.xlsx")
send_email()

print("\n========== FINAL DATA ==========\n")
print(df)
logger.info("ETL Pipeline Completed")