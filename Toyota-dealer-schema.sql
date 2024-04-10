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
mileage    int NOT NULL,
color     varchar(35) NOT NULL,
dealer_id int NOT NULL,
title_type varchar(15)
);

INSERT INTO car_list (car_year, car_make, car_model, min_price, max_price, mileage, color, dealer_id, title_type) 
VALUES (2018, 'Toyota', 'Corolla', 12000.00, 15000.00, 30000, 'Blue', 101, 'Clear');

INSERT INTO car_list (car_year, car_make, car_model, min_price, max_price, mileage, color, dealer_id, title_type) 
VALUES (2020, 'Toyota', 'Camry', 25000.00, 30000.00, 0, 'White', 102, 'Reconstructed');

INSERT INTO car_list (car_year, car_make, car_model, min_price, max_price, mileage, color, dealer_id, title_type) 
VALUES (2017, 'Toyota', 'Rav4', 18000.00, 22000.00, 35000, 'Silver', 103, 'Clear');

INSERT INTO car_list (car_year, car_make, car_model, min_price, max_price, mileage, color, dealer_id, title_type) 
VALUES (2019, 'Toyota', 'Highlander', 28000.00, 32000.00, 25000, 'Black', 104, 'Clear');

INSERT INTO car_list (car_year, car_make, car_model, min_price, max_price, mileage, color, dealer_id, title_type) 
VALUES (2021, 'Toyota', 'Sienna', 35000.00, 40000.00, 0, 'Red', 105, 'Reconstructed');

INSERT INTO car_list (car_year, car_make, car_model, min_price, max_price, mileage, color, dealer_id, title_type) 
VALUES (2016, 'Toyota', 'Prius', 15000.00, 18000.00, 40000, 'Green', 106, 'Clear');

INSERT INTO car_list (car_year, car_make, car_model, min_price, max_price, mileage, color, dealer_id, title_type) 
VALUES (2022, 'Toyota', 'Tacoma', 30000.00, 35000.00, 0, 'Gray', 107, 'Clear');

INSERT INTO car_list (car_year, car_make, car_model, min_price, max_price, mileage, color, dealer_id, title_type) 
VALUES (2015, 'Toyota', 'Yaris', 10000.00, 13000.00, 45000, 'Yellow', 108, 'Reconstructed');

INSERT INTO car_list (car_year, car_make, car_model, min_price, max_price, mileage, color, dealer_id, title_type) 
VALUES (2023, 'Toyota', 'Avalon', 40000.00, 45000.00, 0, 'Black', 109, 'Clear');

INSERT INTO car_list (car_year, car_make, car_model, min_price, max_price, mileage, color, dealer_id, title_type) 
VALUES (2014, 'Toyota', 'Camry', 12000.00, 15000.00, 50000, 'Silver', 110, 'Clear');



CREATE TABLE IF NOT EXISTS trade_history (
car_id int NOT NULL,
trade_date date,
trade_status varchar(50),
seller_id int,
buyer_id int,
car_detail json    -- maybe include car year, model, price, milage, etc.
);


CREATE TABLE IF NOT EXISTS customers (
cust_id int NOT NULL,
car_id int NOT NULL,
car_purchase_date DATE,
cust_fname varchar(35),
cust_lname varchar(35)
);

-- we can use search details to calculate search count.

CREATE TABLE IF NOT EXISTS search_details (
search_id int NOT NULL,
car_id int NOT NULL,
cust_id int NOT NULL,
search_type varchar(50)
);