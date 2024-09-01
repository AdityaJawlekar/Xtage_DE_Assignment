CREATE TABLE IF NOT EXISTS sales_data(
  Transaction_ID 	  INT,
  Product_ID 		    INT REFERENCES products_data(Product_ID),
  Quantity 			    INT,
  Price 			      FLOAT(5),
  Transaction_Date 	DATE,
  PRIMARY KEY 		  (Transaction_ID)
);

COPY sales_data(Transaction_ID, Product_ID, Quantity, Price, Transaction_Date)
FROM 'C:/Users/AdityaJawlekar/Documents/Xtage_Assignment/final_data/final_sales_data.csv'
DELIMITER ','
CSV HEADER;