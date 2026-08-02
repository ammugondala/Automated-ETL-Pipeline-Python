import pandas as pd
from sqlalchemy import create_engine
from urllib.parse import quote_plus

from etl.config import (
    READ_FROM_AZURE_SQL,
    AZURE_SQL_SERVER,
    AZURE_SQL_DATABASE,
    AZURE_SQL_USERNAME,
    AZURE_SQL_PASSWORD,
    AZURE_SQL_TABLE,
    AZURE_SQL_DRIVER,
)

def read_from_azure_sql():
    if not READ_FROM_AZURE_SQL:
        print("Azure SQL reading disabled.")
        return None

    try:
        connection_string = (
            f"DRIVER={{{AZURE_SQL_DRIVER}}};"
            f"SERVER={AZURE_SQL_SERVER};"
            f"DATABASE={AZURE_SQL_DATABASE};"
            f"UID={AZURE_SQL_USERNAME};"
            f"PWD={AZURE_SQL_PASSWORD};"
        )

        engine = create_engine(
            "mssql+pyodbc:///?odbc_connect=%s"
            % quote_plus(connection_string)
        )

        query = f"SELECT * FROM {AZURE_SQL_TABLE}"

        df = pd.read_sql(query, engine)

        print("✅ Data read successfully from Azure SQL!")

        return df

    except Exception as e:
        print("Azure SQL Error:", e)
        return None