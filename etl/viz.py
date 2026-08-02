from etl.logger import logger
import os
import matplotlib.pyplot as plt


def create_visualizations(df):
    """
    Creates charts from the employee dataset.
    """

    print("\nCreating Visualizations...")

    # Create reports folder if it doesn't exist
    os.makedirs("reports", exist_ok=True)

    # -----------------------------
    # 1. Department-wise Employee Count
    # -----------------------------
    dept_count = df["department"].value_counts()

    plt.figure(figsize=(6,4))
    plt.bar(dept_count.index, dept_count.values)
    plt.title("Employees by Department")
    plt.xlabel("Department")
    plt.ylabel("Employees")
    plt.tight_layout()
    plt.savefig("reports/department_count.png")
    plt.close()

    # -----------------------------
    # 2. Salary Bar Chart
    # -----------------------------
    plt.figure(figsize=(7,4))
    plt.bar(df["name"], df["salary"])
    plt.title("Employee Salary")
    plt.xlabel("Employee")
    plt.ylabel("Salary")
    plt.tight_layout()
    plt.savefig("reports/salary_chart.png")
    plt.close()

    # -----------------------------
    # 3. Department Pie Chart
    # -----------------------------
    plt.figure(figsize=(5,5))
    plt.pie(
        dept_count.values,
        labels=dept_count.index,
        autopct="%1.1f%%"
    )
    plt.title("Department Distribution")
    plt.savefig("reports/department_pie.png")
    plt.close()

    # -----------------------------
    # 4. Annual Salary Line Chart
    # -----------------------------
    plt.figure(figsize=(7,4))
    plt.plot(df["name"], df["annual_salary"], marker="o")
    plt.title("Annual Salary")
    plt.xlabel("Employee")
    plt.ylabel("Annual Salary")
    plt.tight_layout()
    plt.savefig("reports/annual_salary.png")
    plt.close()

    print("✅ Charts saved inside 'reports' folder.")
    logger.info("Charts generated successfully.")