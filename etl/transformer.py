from etl.logger import logger
import pandas as pd

def transform_data(df):
    """
    Cleans and transforms the employee data.
    """

    print("\nStarting Data Transformation...")

    # Remove duplicate rows
    df = df.drop_duplicates()

    # Remove rows with missing values
    df = df.dropna()

    # Convert column names to lowercase
    df.columns = df.columns.str.lower()

    # Replace spaces with underscores
    df.columns = df.columns.str.replace(" ", "_")

    # Convert Salary into numeric datatype
    df["salary"] = pd.to_numeric(df["salary"])

    # Convert Joining Date into datetime datatype
    df["joining_date"] = pd.to_datetime(df["joining_date"])

    # Create Annual Salary column
    df["annual_salary"] = df["salary"] * 12

    print("✅ Data transformed successfully!")
    logger.info("Data transformed successfully.")

    return df