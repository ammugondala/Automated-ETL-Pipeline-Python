import os
import smtplib
from email.message import EmailMessage
from dotenv import load_dotenv

# Load variables from .env
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

    # Attach Excel Report
    with open("reports/Employee_Report.xlsx", "rb") as f:
        msg.add_attachment(
            f.read(),
            maintype="application",
            subtype="octet-stream",
            filename="Employee_Report.xlsx"
        )

    # Attach Salary Chart
    with open("reports/salary_chart.png", "rb") as f:
        msg.add_attachment(
            f.read(),
            maintype="image",
            subtype="png",
            filename="salary_chart.png"
        )

    # Connect to Gmail
    with smtplib.SMTP_SSL("smtp.gmail.com", 465) as smtp:
        smtp.login(EMAIL, PASSWORD)
        smtp.send_message(msg)

    print("✅ Email sent successfully!")