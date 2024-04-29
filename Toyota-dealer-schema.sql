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
car_id int,
cust_id int,
cust_fname varchar(35),
cust_lname varchar(35),
car_year int,
car_make varchar(35),
car_model varchar(35),
mileage    int,
color     varchar(35),
dealer_id int,
PRIMARY KEY (cust_id)
);

SELECT car_id, car_year, car_make, car_model FROM customers
ORDER by car_id asc;

INSERT INTO customers (car_id, cust_id, cust_fname, cust_lname, car_year, car_make, car_model, mileage, color, dealer_id) 
VALUES 
(5, 1, 'John', 'Doe', 2017,'Toyota','Rav4',35000,'Silver',103),
(16, 2, 'Alice', 'Smith', 2020,'Toyota','Camry',0,'White',102),
(12, 3, 'Michael', 'Johnson', 2015,'Toyota','Tacoma',70000,'Gray',116),
(7, 4, 'Emily', 'Brown', 2018,'Toyota','Corolla',30000,'Blue',101),
(1, 5, 'James', 'Wilson', 2020,'Toyota','Camry',15000,'Silver',112),
(18, 6, 'Sophia', 'Martinez', 2021,'Toyota','Sienna',0,'Red',105),
(3, 7, 'Daniel', 'Anderson', 2015,'Toyota','Yaris',45000,'Yellow',108),
(9, 8, 'Olivia', 'Taylor', 2023,'Toyota','Yaris',10000,'Black',117),
(19, 9, 'Matthew', 'Thomas', 2014,'Toyota','Camry',80000,'Red',120),
(10, 10, 'Emma', 'Jackson', 2016,'Toyota','Prius',40000,'Green',106),
(15, 11, 'David', 'White', 2023,'Toyota','Avalon',0,'Black',109),
(14, 12, 'Ava', 'Harris', 2022,'Toyota','Tacoma',0,'Gray',107),
(11, 13, 'Liam', 'Martin', 2019,'Toyota','Corolla',25000,'Black',111),
(2, 14, 'Isabella', 'Thompson', 2017,'Toyota','Highlander',20000,'White',114),
(17, 15, 'Mason', 'Garcia', 2018,'Toyota','Rav4',30000,'Blue',113),
(6, 16, 'Sophia', 'Martinez', 2021,'Toyota','Corolla',20000,'Blue',119),
(13, 17, 'Ethan', 'Jones', 2019,'Toyota','Highlander',20000,'Black',104),
(8, 18, 'Amelia', 'Clark', 2014,'Toyota','Camry',50000,'Silver',110),
(20, 19, 'Logan', 'Lewis', 2016,'Toyota','Avalon',40000,'Silver',118),
(4, 20, 'Evelyn', 'Lee', 2019,'Toyota','Highlander', 25000,'Black',104);


CREATE TABLE  car_purchases (
purchase_id int auto_increment PRIMARY KEY,
car_id int,
car_year int,
car_make varchar(35),
car_model varchar(35) ,
mileage int,
color varchar(35),
cust_id int,
cust_fullname varchar(81),
sale_price double (18,2),
sale_date DATE
);

CREATE INDEX index_car 
ON toyota_dealer.car_purchases (car_year,car_make,car_model,color);



-- we can use search details to calculate search count.

CREATE TABLE  car_repair_details (
repair_id int auto_increment PRIMARY KEY,
car_id int,
repair_date DATE,
repair_desc text
);

CREATE FULLTEXT INDEX index_repair_desc 
ON toyota_dealer.car_repair_details (repair_desc);

CREATE TABLE car_maint_events (
	 mech_id int AUTO_INCREMENT PRIMARY KEY,
     car_id int,
	 maint_desc varchar(80),
	 car_year int,
	 car_make varchar(35),
     car_model varchar(35)
);



INSERT INTO car_maint_events (car_id, maint_desc, car_year, car_make, car_model) 
VALUES 
(1, 'replace the engine oil filter', 2020, 'Toyota', 'Camry'),
(2, 'replace the windshield wipers', 2017, 'Toyota', 'Highlander'),
(3, 'replace the brake pads', 2015, 'Toyota', 'Yaris'),
(4, 'change the engine oil', 2019, 'Toyota', 'Highlander'),
(5, 'repair the left rear taillight', 2021, 'Toyota', 'Sienna'),
(6,   'replace the windshield wipers', 2016, 'Toyota', 'Prius'),
(7, 'repair the right front headlight', 2022, 'Toyota', 'Tacoma'),
(8,  'replace the engine oil filter', 2015, 'Toyota', 'Yaris'),
(8,  'repair the left rear taillight', 2015, 'Toyota', 'Yaris'),
(8,  'repair the the windshield wipers', 2015, 'Toyota', 'Yaris'),
(9, 'replace the windshield wipers', 2023, 'Toyota', 'Avalon'),
(10,  'repair the right front headlight', 2014, 'Toyota', 'Camry'),
(10, 'replace the brake pads', 2014, 'Toyota', 'Camry'),
(10,  'touch up the paint', 2014, 'Toyota', 'Camry'),
(11,  'replace the tires', 2019, 'Toyota', 'Corolla'),
(12,  'repair the right front headlight', 2020, 'Toyota', 'Camry'),
(13,  'replace the air filter', 2018, 'Toyota', 'Rav4'),
(14,  'repair the right rear taillight', 2017, 'Toyota', 'Highlander'),
(15, 'replace the windshield wipers', 2022, 'Toyota', 'Sienna'),
(16, 'replace the windshield wipers', 2015, 'Toyota', 'Tacoma'),
(17, 'replace the tires', 2018, 'Toyota', 'Rav4'),
(18, 'repair the left rear taillight', 2021, 'Toyota', 'Sienna'),
(19, 'replace the windshield wipers', 2021, 'Toyota', 'Corolla'),
(20, 'replace the tires', 2014, 'Toyota', 'Camry');





CREATE TABLE car_maint_history(
    maint_id int AUTO_INCREMENT PRIMARY KEY,
    mech_id int,
    car_id int,
    cust_id int,
    cust_fname varchar(35),
    cust_lname varchar(35),
    maint_date date,
    maint_desc varchar(80),
    car_year int,
    car_make varchar(35),
    car_model varchar(35),
    maint_cost int,
    FOREIGN KEY (car_id) REFERENCES car_list(car_id),
    FOREIGN KEY (cust_id) REFERENCES customers(cust_id)
);


CREATE TABLE IF NOT EXISTS car_accident_history (
accident_id int auto_increment PRIMARY KEY,
car_id int,
accident_date date
);

INSERT INTO car_accident_history (car_id, accident_date) 
VALUES 
(1, '2020-01-18'),
(1, '2021-03-08'),
(2, '2022-01-05'),
(2, '2023-03-17'),
(2, '2024-09-12'),
(3, '2021-08-14'),
(3, '2022-07-16'),
(4, '2023-06-19'),
(5, '2024-04-12');
