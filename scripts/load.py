import mysql.connector

def load_data(df):
    conn = mysql.connector.connect(
        host="localhost",
        user="root",
        password="root123",
        database="etl_project"
    )
    cursor = conn.cursor()

    query = """
            INSERT INTO orders (order_id, \
                                customer_id, \
                                order_status, \
                                order_purchase_timestamp, \
                                order_approved_at, \
                                order_delivered_carrier_date, \
                                order_delivered_customer_date, \
                                order_estimated_delivery_date)
            VALUES (%s, %s, %s, %s, %s, %s, %s, %s) \
            """

    data = df[[
        'order_id',
        'customer_id',
        'order_status',
        'order_purchase_timestamp',
        'order_approved_at',
        'order_delivered_carrier_date',
        'order_delivered_customer_date',
        'order_estimated_delivery_date'
    ]].values.tolist()

    cursor.executemany(query, data)

    conn.commit()
    conn.close()

    print("Data loaded into MySQL")