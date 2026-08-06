import os
from openpyxl import Workbook
from etl.logger import logger
from etl.config import REPORT_FOLDER

def create_excel_report(df):
    """
    Creates an Excel report from the transformed DataFrame.
    """

    os.makedirs(REPORT_FOLDER, exist_ok=True)
    wb = Workbook()
    ws = wb.active
    ws.title = "Employee Report"

    # Write column headers
    ws.append(list(df.columns))

    # Write data rows
    for row in df.itertuples(index=False):
        ws.append(list(row))

    excel_path = os.path.join(REPORT_FOLDER, "Employee_Report.xlsx")
    wb.save(excel_path)

    print("✅ Excel report created successfully!")
    logger.info("Excel report created successfully.")