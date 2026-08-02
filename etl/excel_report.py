import os
from openpyxl import Workbook
from etl.logger import logger

def create_excel_report(df):
    """
    Creates an Excel report from the transformed DataFrame.
    """

    os.makedirs("reports", exist_ok=True)

    wb = Workbook()
    ws = wb.active
    ws.title = "Employee Report"

    # Write column headers
    ws.append(list(df.columns))

    # Write data rows
    for row in df.itertuples(index=False):
        ws.append(list(row))

    excel_path = "reports/Employee_Report.xlsx"
    wb.save(excel_path)

    print("✅ Excel report created successfully!")
    logger.info("Excel report created successfully.")