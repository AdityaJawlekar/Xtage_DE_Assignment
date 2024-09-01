import pandas as pd

# Reading sales raw data
raw_sales_path = (
    "C:/Users/AdityaJawlekar/Documents/Xtage_Assignment/raw_data/raw_sales_data.csv"
)
raw_sales_df = pd.read_csv(raw_sales_path)


## Define a function to handle multiple date formats
def parse_dates(date_str):
    """This fuctions take different date format and convert into
    fix yyyy-mm-dd format

    Args:
        date_str (string): date string

    Returns:
        date string: final date into yyyy-mm-dd format
    """
    for fmt in ("%m/%d/%Y", "%m-%d-%Y", "%Y-%m-%d", "%Y-%d-%m", "%d-%m-%Y", "%d/%m/%Y"):
        try:
            return pd.to_datetime(date_str, format=fmt)
        except ValueError:
            continue
    return pd.NaT


## Fill negative and NA values by 0
raw_sales_df["Price"] = raw_sales_df["Price"].where(raw_sales_df["Price"] >= 0, 0)
raw_sales_df["Quantity"] = raw_sales_df["Quantity"].where(
    raw_sales_df["Quantity"] >= 0, 0
)
raw_sales_df["Transaction_Date"] = raw_sales_df["Transaction_Date"].fillna(
    ("1900-01-01")
)
raw_sales_df.Transaction_Date = raw_sales_df.Transaction_Date.apply(parse_dates)
raw_sales_df.Transaction_Date = pd.to_datetime(raw_sales_df["Transaction_Date"])

## Saving final data in csv file
raw_sales_df.to_csv(
    "C:/Users/AdityaJawlekar/Documents/Xtage_Assignment/final_data/final_sales_data.csv",
    encoding="utf-8",
    index=False,
    header=True,
)
print("Final sales data saved into local")

# Reading exchange rates raw data
raw_exchange_rate_path = (
    "C:/Users/AdityaJawlekar/Documents/Xtage_Assignment/raw_data/raw_exchange_rates.csv"
)
raw_exchange_rate_data = pd.read_csv(raw_exchange_rate_path)

## Fill negative and NA values by 0
raw_exchange_rate_data["Exchange_Rate"] = raw_exchange_rate_data["Exchange_Rate"].where(
    raw_exchange_rate_data["Exchange_Rate"] >= 0, 0
)

## Saving final data in csv file
raw_exchange_rate_data.to_csv(
    "C:/Users/AdityaJawlekar/Documents/Xtage_Assignment/final_data/final_exchange_rates.csv",
    encoding="utf-8",
    index=False,
    header=True,
)
print("Final exchange rates saved into local")

# Reading customer raw data
raw_customer_data_path = (
    "C:/Users/AdityaJawlekar/Documents/Xtage_Assignment/raw_data/raw_customer_data.csv"
)
raw_customer_data = pd.read_csv(raw_customer_data_path)

## Fill NA values by 0
raw_customer_data["Age"] = raw_customer_data["Age"].where(
    raw_customer_data["Age"] == 0, 0
)
raw_customer_data["Age"] = raw_customer_data["Age"].astype(int)
raw_customer_data["Date_Joined"] = pd.to_datetime(raw_customer_data["Date_Joined"])
raw_customer_data["Date_Joined"] = raw_customer_data["Date_Joined"].fillna(
    ("1900-01-01")
)

## Saving final data in csv file
raw_customer_data.to_csv(
    "C:/Users/AdityaJawlekar/Documents/Xtage_Assignment/final_data/final_customer_data.csv",
    encoding="utf-8",
    index=False,
    header=True,
)
print("Final customer data saved into local")

# Reading products raw data
raw_products_path = (
    "C:/Users/AdityaJawlekar/Documents/Xtage_Assignment/raw_data/raw_products_data.csv"
)
raw_products_data = pd.read_csv(raw_products_path)

## Saving final data in csv file
raw_products_data.to_csv(
    "C:/Users/AdityaJawlekar/Documents/Xtage_Assignment/final_data/final_product_data.csv",
    encoding="utf-8",
    index=False,
    header=True,
)
print("Final product data saved into local")

# Reading transactions raw data
raw_transactions_path = "C:/Users/AdityaJawlekar/Documents/Xtage_Assignment/raw_data/raw_transactions_data.csv"
raw_transactions_data = pd.read_csv(raw_transactions_path)

## Fill negative and NA values
raw_transactions_data["total_amount"] = raw_transactions_data["total_amount"].where(
    raw_transactions_data["total_amount"] >= 0, 0
)
raw_transactions_data["transaction_date"] = pd.to_datetime(
    raw_transactions_data["transaction_date"]
)
raw_transactions_data["transaction_date"] = raw_transactions_data[
    "transaction_date"
].fillna(("1900-01-01"))

## Saving final data in csv file
raw_transactions_data.to_csv(
    "C:/Users/AdityaJawlekar/Documents/Xtage_Assignment/final_data/final_transactions_data.csv",
    encoding="utf-8",
    index=False,
    header=True,
)
print("Final transactions data saved into local")
