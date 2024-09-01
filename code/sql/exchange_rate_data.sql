CREATE TABLE IF NOT EXISTS exchange_rates (
  Currency_Code 	VARCHAR(5),
  Exchange_Rate 	FLOAT(7),
  Date 				    DATE
);

COPY exchange_rates(Currency_Code, Exchange_Rate, Date)
FROM 'C:/Users/AdityaJawlekar/Documents/Xtage_Assignment/raw_data/raw_exchange_rates.csv'
DELIMITER ','
CSV HEADER;