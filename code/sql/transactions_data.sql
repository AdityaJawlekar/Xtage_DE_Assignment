CREATE TABLE IF NOT EXISTS transactions_data (
  Transaction_ID 	  INT,
  Product_ID 		    INT REFERENCES products_data(Product_ID),
  Customer_ID 		  INT REFERENCES customers_data(Customer_ID),
  Quantity 			    INT,
  Transaction_Date 	DATE,
  Total_Amount 		  FLOAT(10),
  PRIMARY KEY 		  (Transaction_ID)
);

COPY transactions_data(Transaction_ID, Product_ID, Customer_ID, Quantity, Transaction_Date, Total_Amount)
FROM 'C:/Users/AdityaJawlekar/Documents/Xtage_Assignment/final_data/final_transactions_data.csv'
DELIMITER ','
CSV HEADER;