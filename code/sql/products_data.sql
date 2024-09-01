CREATE TABLE IF NOT EXISTS products_data (
  Product_ID 		    INT,
  Product_Name 		  VARCHAR(50),
  Category 			    VARCHAR(15),
  Price 			      FLOAT(5),
  Stock_Available 	INT,
  PRIMARY KEY 		  (Product_ID)
);

COPY products_data(Product_ID, Product_Name, Category, Price, Stock_Available)
FROM 'C:/Users/AdityaJawlekar/Documents/Xtage_Assignment/final_data/final_product_data.csv'
DELIMITER ','
CSV HEADER;