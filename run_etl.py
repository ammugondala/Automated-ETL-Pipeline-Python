import time

from etl.quality_check import data_quality_check
from etl.azure_sql_reader import read_from_azure_sql
from etl.azure_loader import upload_to_blob
from etl.extractor import extract_data
from etl.transformer import transform_data
from etl.loader import load_data
from etl.viz import create_visualizations
from etl.html_report import generate_html_report
from etl.excel_report import create_excel_report
from etl.emailer import send_email
from etl.logger import logger

from etl.config import (
    CSV_PATH,
    READ_FROM_AZURE_SQL,
    REPORT_FOLDER
)

import os


def main():
    """
    Main ETL Pipeline
    """

    start_time = time.time()

    print("=" * 50)
    print("🚀 ETL PIPELINE STARTED")
    print("=" * 50)

    logger.info("ETL Pipeline Started")

    # -----------------------------
    # Extract
    # -----------------------------
    print("\n📥 Extracting Data...")

    if READ_FROM_AZURE_SQL:
        df = read_from_azure_sql()
    else:
        df = extract_data(CSV_PATH)

    # -----------------------------
    # Data Quality Check
    # -----------------------------
    data_quality_check(df)

    # -----------------------------
    # Transform
    # -----------------------------
    print("\n🔄 Transforming Data...")
    df = transform_data(df)

    # -----------------------------
    # Load
    # -----------------------------
    print("\n💾 Loading Data...")
    load_data(df)

    # -----------------------------
    # Reports
    # -----------------------------
    print("\n📊 Creating Visualizations...")
    create_visualizations(df)

    print("\n📝 Generating HTML Report...")
    generate_html_report(df)

    print("\n📄 Generating Excel Report...")
    create_excel_report(df)

    # -----------------------------
    # Azure Upload
    # -----------------------------
    upload_to_blob(
        os.path.join(REPORT_FOLDER, "Employee_Report.xlsx")
    )

    # -----------------------------
    # Email
    # -----------------------------
    print("\n📧 Sending Email...")
    send_email()

    # -----------------------------
    # Finished
    # -----------------------------
    end_time = time.time()

    print("\n" + "=" * 50)
    print("✅ ETL PIPELINE COMPLETED")
    print("=" * 50)

    print(df)

    print(f"\n⏱ Execution Time: {end_time - start_time:.2f} seconds")

    logger.info("ETL Pipeline Completed")


if __name__ == "__main__":
    main()