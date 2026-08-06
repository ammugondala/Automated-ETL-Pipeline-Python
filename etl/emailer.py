import os
import smtplib
from email.message import EmailMessage
from dotenv import load_dotenv

from etl.config import REPORT_FOLDER
from etl.logger import logger

load_dotenv()

EMAIL = os.getenv("EMAIL")
PASSWORD = os.getenv("PASSWORD")
RECEIVER = os.getenv("RECEIVER")


def send_email():
    """
    Sends the ETL report through Gmail.
    """

    msg = EmailMessage()

    msg["Subject"] = "ETL Pipeline Report"
    msg["From"] = EMAIL
    msg["To"] = RECEIVER

    msg.set_content("""
Hello,

Your ETL Pipeline has completed successfully.

The reports are attached.

Regards,
Amrutha Varshini
""")

    try:
        excel_path = os.path.join(REPORT_FOLDER, "Employee_Report.xlsx")

        with open(excel_path, "rb") as f:
            msg.add_attachment(
                f.read(),
                maintype="application",
                subtype="octet-stream",
                filename="Employee_Report.xlsx"
            )

        chart_path = os.path.join(REPORT_FOLDER, "salary_chart.png")

        with open(chart_path, "rb") as f:
            msg.add_attachment(
                f.read(),
                maintype="image",
                subtype="png",
                filename="salary_chart.png"
            )

        with smtplib.SMTP_SSL("smtp.gmail.com", 465) as smtp:
            smtp.login(EMAIL, PASSWORD)
            smtp.send_message(msg)

        print("✅ Email sent successfully!")
        logger.info("Email sent successfully.")

    except Exception as e:
        print(f"❌ Failed to send email: {e}")
        logger.error(f"Email sending failed: {e}")