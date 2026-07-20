import pandas as pd


def transform(df):
    """
    Cleans and transforms the employee data.
    """

    print("\nStarting Data Transformation...")

    # 1. Remove duplicate rows
    df = df.drop_duplicates()

    # 2. Remove rows with missing values
    df = df.dropna()

    # 3. Convert column names to lowercase
    df.columns = df.columns.str.lower()

    # 4. Replace spaces with underscores
    df.columns = df.columns.str.replace(" ", "_")

    # 5. Convert Salary into numeric datatype
    df["salary"] = pd.to_numeric(df["salary"])

    # 6. Convert Joining Date into datetime datatype
    df["joining_date"] = pd.to_datetime(df["joining_date"])

    # 7. Create Annual Salary column
    df["annual_salary"] = df["salary"] * 12

    print("✅ Data transformed successfully!")

    return df