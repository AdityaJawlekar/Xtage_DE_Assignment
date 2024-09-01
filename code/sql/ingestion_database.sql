CREATE TABLE if not exists products (
  Product_ID      INT,
  Product_Name    VARCHAR(50),
  Category        VARCHAR(50),
  Price           float(5),
  Stock_Available INT,
  PRIMARY KEY     (Product_ID)
);

COPY products(Product_ID, Product_Name, Category, Price, Stock_Available)
FROM 'C:\Users\AdityaJawlekar\Documents\Xtage_Assignment\data_source\products.csv'
DELIMITER ','
CSV HEADER;

CREATE TABLE if not exists transactions (
  Transaction_ID    INT,
  Customer_ID       INT,
  Product_ID        INT references products(Product_ID),
  Quantity          INT,
  Transaction_Date  DATE,
  Total_Amount      float(5),
  PRIMARY KEY       (Transaction_ID)
);

COPY transactions(Transaction_ID, Customer_ID, Product_ID, Quantity , Transaction_Date, Total_Amount)
FROM 'C:\Users\AdityaJawlekar\Documents\Xtage_Assignment\data_source\transactions.csv'
DELIMITER ','
CSV HEADER;