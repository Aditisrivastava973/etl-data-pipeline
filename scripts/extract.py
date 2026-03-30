import pandas as pd

def extract_data(file_path):
    try:
        df = pd.read_csv(file_path)

        print("Data extracted successfully")
        print(df.head())

        return df

    except Exception as e:
        print("Error in extraction:", e)