import pandas as pd

def data_quality_check(df):
    print("\n========== DATA QUALITY REPORT ==========")

    # Total records
    print(f"Total Records: {len(df)}")

    # Missing values
    print("\nMissing Values:")
    print(df.isnull().sum())

    # Duplicate records
    duplicates = df.duplicated().sum()
    print(f"\nDuplicate Records: {duplicates}")

    # Data types
    print("\nData Types:")
    print(df.dtypes)

    print("\n✅ Data Quality Check Completed Successfully")