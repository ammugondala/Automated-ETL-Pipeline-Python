from etl.extractor import extract
from etl.transformer import transform


def main():

    csv_path = "data/dummy_data.csv"

    # Extract
    df = extract(csv_path)

    if df is not None:

        # Transform
        df = transform(df)

        print("\n===== Transformed Data =====\n")
        print(df)


if __name__ == "__main__":
    main()