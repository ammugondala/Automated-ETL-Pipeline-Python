import os
from etl.config import REPORT_FOLDER

def generate_html_report(df):
    """
    Generates an HTML report for employee data.
    """

    os.makedirs(REPORT_FOLDER, exist_ok=True)
    total = len(df)
    avg_salary = df["salary"].mean()
    max_salary = df["salary"].max()
    min_salary = df["salary"].min()

    dept_table = (
    df["department"]
    .value_counts()
    .to_frame(name="Count")
    .to_html()
)
    html = f"""
    <html>
    <head>
        <title>Employee ETL Report</title>

        <style>

        body {{
            font-family: Arial;
            margin:40px;
            background:#f4f4f4;
        }}

        h1 {{
            color:darkblue;
        }}

        table {{
            border-collapse:collapse;
            width:50%;
        }}

        th,td {{
            border:1px solid black;
            padding:8px;
        }}

        img {{
            width:500px;
            margin-top:20px;
        }}

        </style>

    </head>

    <body>

    <h1>Employee ETL Report</h1>

    <h2>Summary</h2>

    <ul>

        <li>Total Employees : {total}</li>

        <li>Average Salary : {avg_salary:.2f}</li>

        <li>Highest Salary : {max_salary}</li>

        <li>Lowest Salary : {min_salary}</li>

    </ul>

    <h2>Department Distribution</h2>

    {dept_table}

    <h2>Charts</h2>

    <img src="salary_chart.png">

    <img src="department_count.png">

    <img src="department_pie.png">

    </body>

    </html>
    """

    html_path = os.path.join(REPORT_FOLDER, "report.html")

    with open(html_path, "w", encoding="utf-8") as file:
        file.write(html)

    print("✅ HTML Report Generated Successfully!")