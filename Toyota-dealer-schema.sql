DROP SCHEMA IF EXISTS toyota_dealer;

CREATE SCHEMA IF NOT EXISTS toyota_dealer;

USE toyota_dealer;

Drop table if exists car_list;
CREATE TABLE IF NOT EXISTS car_list (
car_id int NOT NULL AUTO_INCREMENT PRIMARY KEY,
car_year int NOT NULL,
car_make varchar(35) NOT NULL,
car_model varchar(35) NOT NULL,
min_price double(18,2) Not NULL,
max_price double(18,2) Not NULL,
milage    int NOT NULL,
color     varchar(35) NOT NULL,
dealer_id int NOT NULL,
title_type varchar(15),
rating    int
);




Drop table if exists trade_history;
CREATE TABLE IF NOT EXISTS trade_history (
car_id int NOT NULL,
trade_date date,
trade_status varchar(50),
seller_id int,
buyer_id int,
car_detail json    -- maybe include car year, model, price, milage, etc.
);

Drop table if exists customers;
CREATE TABLE IF NOT EXISTS customers (
cust_id int NOT NULL,
car_id int NOT NULL,
car_purchase_date DATE,
cust_fname varchar(35),
cust_lname varchar(35)
);

-- we can use search details to calculate search count.
Drop table if exists search_details;
CREATE TABLE IF NOT EXISTS search_details (
search_id int NOT NULL,
car_id int NOT NULL,
cust_id int NOT NULL,
search_type varchar(50)
);