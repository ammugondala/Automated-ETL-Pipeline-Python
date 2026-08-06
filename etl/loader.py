from etl.logger import logger
from etl.config import DB_NAME
import sqlite3


def load_data(df):
    """
    Load transformed data into SQLite database
    """

    try:
        logger.info("Database loading started.")

        conn = sqlite3.connect(DB_NAME)
        
        logger.info("SQLite database connection established.")

        df.to_sql(
            "employees",
            conn,
            if_exists="replace",
            index=False
        )

        record_count = len(df)

        logger.info(
            f"Data loaded successfully. Records inserted: {record_count}"
        )

        conn.close()

        print("\n✅ Data loaded successfully into SQLite database!")

    except Exception as e:
        logger.error(f"Error while loading data: {e}")
        print(f"❌ Error loading data: {e}")

    finally:
        try:
            conn.close()
        except:
            pass