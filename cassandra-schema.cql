CREATE KEYSPACE IF NOT EXISTS car_purchase_prices
WITH replication = {
    'class': 'SimpleStrategy', 
    'replication_factor': 1 };

USE sale_monitoring;


CREATE TABLE IF NOT EXISTS car_purchases (
purchase_id int PRIMARY KEY not NULL,
car_id int NOT NULL,
car_year int NOT NULL,
car_make varchar(35) NOT NULL,
car_model varchar(35) NOT NULL,
-- mileage    int NOT NULL,
color     varchar(35) NOT NULL,
cust_id int NOT NULL,
cust_wholename varchar(80),
purchase_price double(18.2).
purchase_date DATE NOT NULL
);



CREATE TABLE IF NOT EXISTS car_info (
    car_id int,
    car_year int,
    car_make text,
    car_model text,
    min_price double(7,2) ,
    max_price double(7,2) ,
    milage    int,
    color     text,
    rating int,
    num_of_owners int,
    PRIMARY KEY (car_id)
) WITH CLUSTERING ORDER BY (car_year DESC);


CREATE TABLE IF NOT EXISTS car_stats (
    sale_date DATE,
    car_id int,
    car_make text,
    car_model text,
    avg_price DOUBLE(7,2)
    mileage int,
    color text,
    location_town text,
    location_state text,
    sales_count int
) WITH CLUSTERING ORDER BY (car_year DESC);


CREATE TABLE IF NOT EXISTS statistical_analysis (
    sale_date date,
    car_id text,
    car_year int,
    car_make text,
    car_model text, 
    avg_price DOUBLE,
    mileage int, 
    color text,
    sales_count int
)

