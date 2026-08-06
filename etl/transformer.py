from etl.logger import logger
import pandas as pd

def transform_data(df):
    """
    Cleans and transforms the employee data.
    """

    print("\nStarting Data Transformation...")
    logger.info("Data transformation started.")

    # Remove duplicate rows
    before_duplicates = len(df)
    df = df.drop_duplicates()
    after_duplicates = len(df)

    logger.info(
        f"Duplicates removed: {before_duplicates - after_duplicates}"
    )

    # Remove rows with missing values
    before_missing = len(df)
    df = df.dropna()
    after_missing = len(df)

    logger.info(
        f"Missing values removed: {before_missing - after_missing}"
    )

    # Convert column names to lowercase
    df.columns = df.columns.str.lower()
    logger.info("Column names converted to lowercase.")

    # Replace spaces with underscores
    df.columns = df.columns.str.replace(" ", "_")
    logger.info("Spaces replaced with underscores in column names.")

    # Convert Salary into numeric datatype
    df["salary"] = pd.to_numeric(df["salary"])
    logger.info("Salary column converted to numeric datatype.")

    # Convert Joining Date into datetime datatype
    df["joining_date"] = pd.to_datetime(df["joining_date"])
    logger.info("Joining date converted to datetime format.")

    # Create Annual Salary column
    df["annual_salary"] = df["salary"] * 12
    logger.info("Annual salary column created.")

    print("✅ Data transformed successfully!")
    logger.info("Data transformation completed successfully.")

    return df