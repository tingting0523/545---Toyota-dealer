CREATE KEYSPACE IF NOT EXISTS car_purchase_prices
WITH replication = {
    'class': 'SimpleStrategy', 
    'replication_factor': 1 };

USE car_purchase_prices;


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



CREATE TABLE IF NOT EXISTS car_purchase_prices.car_info (
    car_id int,
    car_year int,
    car_make text,
    car_model text,
    min_price double,
    max_price double,
    milage    int,
    color     text,
    rating int,
    num_of_owners int,
    repair_num int,
    accident_num int,
    PRIMARY KEY (car_id)
);


CREATE TABLE IF NOT EXISTS car_purchase_prices.car_stats (
    sale_date DATE,
    car_id int,
    car_make text,
    car_model text,
    avg_price DOUBLE,
    mileage int,
    color text,
    location_town text,
    location_state text,
    sales_count int,
    PRIMARY KEY (sale_date,car_id)
);

CREATE TABLE IF NOT EXISTS car_purchase_prices.car_accident_history (
accident_id int PRIMARY KEY,
car_id int,
accident_date date
);

-- SELECT keyspace_name, table_name FROM system_schema.tables WHERE keyspace_name = 'car_purchase_prices';