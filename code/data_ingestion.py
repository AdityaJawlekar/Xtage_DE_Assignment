import pandas as pd
import requests
import psycopg2 as pg


# Ingesting sales data from flat files
file_path = (
    r"C:/Users/AdityaJawlekar/Documents/Xtage_Assignment/data_source/sales_data.csv"
)

sales_df = pd.read_csv(file_path)

## Saving raw data in csv file
sales_df.to_csv(
    "C:/Users/AdityaJawlekar/Documents/Xtage_Assignment/raw_data/raw_sales_data.csv",
    encoding="utf-8",
    index=False,
    header=True,
)
print("raw sales data saved into local")


# Ingesting data from external API
try:
    external_api = "https://c6dea896-c8a9-465a-a817-c607cab7881e.mock.pstmn.io"
    external_response = requests.get(external_api)

    if external_response.status_code == 200:
        data = external_response.json()
        external_data_df = pd.DataFrame(data)
        raw_external_api_df = external_data_df.copy()

        ## Saving raw data in csv file
        raw_external_api_df.to_csv(
            "C:/Users/AdityaJawlekar/Documents/Xtage_Assignment/raw_data/raw_exchange_rates.csv",
            encoding="utf-8",
            index=False,
            header=True,
        )
        print("raw exchange rates data saved into local")
    else:
        print("Error while getting response from external API")
except:
    print("Error while connecting to external API")


# Ingesting data from internal API
try:
    internal_api = "https://eaaaf97e-4b0e-474c-8ac8-cbdf8d9d173e.mock.pstmn.io"
    internal_response = requests.get(internal_api)

    if internal_response.status_code == 200:
        data = internal_response.json()
        internal_data_df = pd.DataFrame(data)
        raw_internal_api_df = internal_data_df.copy()

        ## Saving raw data in csv file
        raw_internal_api_df.to_csv(
            "C:/Users/AdityaJawlekar/Documents/Xtage_Assignment/raw_data/raw_customer_data.csv",
            encoding="utf-8",
            index=False,
            header=True,
        )
        print("raw customer data saved into local")
    else:
        print("Error while getting response from internal API")
except:
    print("Error while connecting to internal API")

# Ingesting data frpm Postgressql database

## Establishing the connection
conn = pg.connect(
    database="postgres",
    user="postgres",  # enter username
    password="password",  # enter password
    host="localhost",
    port="5432",
)

## Reading data from products tables
products_query = """SELECT * from products"""
product_df = pd.read_sql(products_query, conn)

## Saving raw data in csv file
product_df.to_csv(
    "C:/Users/AdityaJawlekar/Documents/Xtage_Assignment/raw_data/raw_products_data.csv",
    encoding="utf-8",
    index=False,
    header=True,
)
print("raw products data saved into local")

## Reading data from transactions tables
transactions_query = """select * from transactions"""
transaction_df = pd.read_sql(transactions_query, conn)
raw_transaction_df = transaction_df.copy()

## Saving raw data in csv file
raw_transaction_df.to_csv(
    "C:/Users/AdityaJawlekar/Documents/Xtage_Assignment/raw_data/raw_transactions_data.csv",
    encoding="utf-8",
    index=False,
    header=True,
)
print("raw transactions data saved into local")
