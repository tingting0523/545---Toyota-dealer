DROP SCHEMA IF EXISTS toyota_dealer;

CREATE SCHEMA toyota_dealer;

USE toyota_dealer;

CREATE TABLE  car_list (
car_id int PRIMARY KEY,
car_year int,
car_make varchar(35),
car_model varchar(35),
min_price double(18,2),
max_price double(18,2),
mileage    int,
color     varchar(35),
dealer_id int,
title_type varchar(35)
);

INSERT INTO car_list (car_id, car_year, car_make, car_model, min_price, max_price, mileage, color, dealer_id, title_type) 
VALUES 
(1, 2018, 'Toyota', 'Corolla', 12000.00, 15000.00, 30000, 'Blue', 101, 'Clear'),
(2, 2020, 'Toyota', 'Camry', 25000.00, 30000.00, 0, 'White', 102, 'Reconstructed'),
(3, 2017, 'Toyota', 'Rav4', 18000.00, 22000.00, 35000, 'Silver', 103, 'Clear'),
(4, 2019, 'Toyota', 'Highlander', 28000.00, 32000.00, 25000, 'Black', 104, 'Clear'),
(5, 2021, 'Toyota', 'Sienna', 35000.00, 40000.00, 0, 'Red', 105, 'Reconstructed'),
(6, 2016, 'Toyota', 'Prius', 15000.00, 18000.00, 40000, 'Green', 106, 'Clear'),
(7, 2022, 'Toyota', 'Tacoma', 30000.00, 35000.00, 0, 'Gray', 107, 'Clear'),
(8, 2015, 'Toyota', 'Yaris', 10000.00, 13000.00, 45000, 'Yellow', 108, 'Reconstructed'),
(9, 2023, 'Toyota', 'Avalon', 40000.00, 45000.00, 0, 'Black', 109, 'Clear'),
(10, 2014, 'Toyota', 'Camry', 12000.00, 15000.00, 50000, 'Silver', 110, 'Clear'),
(11, 2019, 'Toyota', 'Corolla', 14000.00, 17000.00, 25000, 'Black', 111, 'Clear'),
(12, 2020, 'Toyota', 'Camry', 26000.00, 31000.00, 15000, 'Silver', 112, 'Reconstructed'),
(13, 2018, 'Toyota', 'Rav4', 20000.00, 24000.00, 30000, 'Blue', 113, 'Clear'),
(14, 2017, 'Toyota', 'Highlander', 30000.00, 35000.00, 20000, 'White', 114, 'Clear'),
(15, 2022, 'Toyota', 'Sienna', 38000.00, 42000.00, 5000, 'Red', 115, 'Reconstructed'),
(16, 2015, 'Toyota', 'Tacoma', 25000.00, 30000.00, 70000, 'Gray', 116, 'Clear'),
(17, 2023, 'Toyota', 'Yaris', 12000.00, 15000.00, 10000, 'Black', 117, 'Clear'),
(18, 2016, 'Toyota', 'Avalon', 35000.00, 40000.00, 40000, 'Silver', 118, 'Reconstructed'),
(19, 2021, 'Toyota', 'Corolla', 16000.00, 19000.00, 20000, 'Blue', 119, 'Clear'),
(20, 2014, 'Toyota', 'Camry', 13000.00, 16000.00, 80000, 'Red', 120, 'Reconstructed');


CREATE TABLE  customers (
cust_id int,
cust_fname varchar(35),
cust_lname varchar(35)
);


INSERT INTO customers (cust_id, cust_fname, cust_lname) 
VALUES 
(1, 'John', 'Doe'),
(2, 'Alice', 'Smith'),
(3, 'Michael', 'Johnson'),
(4, 'Emily', 'Brown'),
(5, 'James', 'Wilson'),
(6, 'Sophia', 'Martinez'),
(7, 'Daniel', 'Anderson'),
(8, 'Olivia', 'Taylor'),
(9, 'Matthew', 'Thomas'),
(10, 'Emma', 'Jackson'),
(11, 'David', 'White'),
(12, 'Ava', 'Harris'),
(13, 'Liam', 'Martin'),
(14, 'Isabella', 'Thompson'),
(15, 'Mason', 'Garcia'),
(16, 'Sophia', 'Martinez'),
(17, 'Ethan', 'Jones'),
(18, 'Amelia', 'Clark'),
(19, 'Logan', 'Lewis'),
(20, 'Evelyn', 'Lee');


CREATE TABLE  car_purchases (
purchase_id int auto_increment PRIMARY KEY,
car_id int,
car_year int,
car_make varchar(35),
car_model varchar(35) ,
mileage    int,
color     varchar(35),
cust_id int,
cust_wholename varchar(81),
purchase_price double (18,2),
purchase_date DATE
);



-- we can use search details to calculate search count.

