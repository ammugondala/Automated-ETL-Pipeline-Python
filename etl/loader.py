from etl.logger import logger
import sqlite3

def load_data(df):
    """
    Load transformed data into SQLite database
    """

    conn = sqlite3.connect("employee.db")

    df.to_sql(
        "employees",
        conn,
        if_exists="replace",
        index=False
    )

    conn.close()

    print("\n✅ Data loaded successfully into SQLite database!")
    logger.info("Data loaded successfully into SQLite database.")