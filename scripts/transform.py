import pandas as pd

def transform_data(df):
    # Remove duplicates
    df = df.drop_duplicates()

    # Convert date columns
    date_cols = [
        'order_purchase_timestamp',
        'order_approved_at',
        'order_delivered_carrier_date',
        'order_delivered_customer_date',
        'order_estimated_delivery_date'
    ]

    for col in date_cols:
        if col in df.columns:
            df[col] = pd.to_datetime(df[col], errors='coerce')

    # Handle missing values
    df = df.ffill()

    # ✅ SAVE CLEANED DATA
    df.to_csv("data/cleaned_data.csv", index=False)

    print("Data transformed successfully")

    return df