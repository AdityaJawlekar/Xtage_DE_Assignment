CREATE TABLE IF NOT EXISTS customers_data (
  Customer_ID 		INT,
  Customer_Name 	VARCHAR(50),
  Age 				    INT,
  Gender 			    VARCHAR(10),
  Location 			  VARCHAR(50),
  Date_Joined 		DATE,
  PRIMARY KEY 		(Customer_ID)
);

COPY customers_data(Customer_ID, Customer_Name, Age, Gender, Location, Date_Joined)
FROM 'C:/Users/AdityaJawlekar/Documents/Xtage_Assignment/final_data/final_customer_data.csv'
DELIMITER ','
CSV HEADER;