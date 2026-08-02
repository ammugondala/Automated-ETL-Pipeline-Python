import pandas as pd

def extract_data(csv_path):
    """
    Reads data from the CSV file.
    """

    try:
        df = pd.read_csv(csv_path)
        print("✅ CSV loaded successfully.")
        return df

    except FileNotFoundError:
        print("❌ CSV file not found!")
        return None

    except Exception as e:
        print(f"❌ Error while reading CSV: {e}")
        return None