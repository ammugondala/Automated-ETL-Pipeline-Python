import pandas as pd


def extract(csv_path):
    """
    Reads a CSV file and returns a DataFrame.
    """

    try:
        df = pd.read_csv(csv_path)
        print("✅ CSV loaded successfully.")
        return df

    except FileNotFoundError:
        print("❌ CSV file not found.")
        return None

    except Exception as e:
        print("❌ Error:", e)
        return None