CREATE KEYSPACE IF NOT EXISTS car_db
WITH replication = {
    'class': 'SimpleStrategy', 
    'replication_factor': 3 };

USE car_db;


CREATE TABLE IF NOT EXISTS car_info (
    car_id int,
    car_year int,
    car_make text,
    car_model text,
    min_price double,
    max_price double,
    milage    int,
    color     text
    PRIMARY KEY ((car_id), car_year)
) WITH CLUSTERING ORDER BY (car_year desc);

CREATE TABLE IF NOT EXISTS car_purchases (
    purchase_id INT,
    car_id INT,
    car_year INT,
    car_make TEXT,
    car_model TEXT,
    color TEXT,
    cust_id INT,
    cust_fullname TEXT,
    sale_price DOUBLE,
    sale_date DATE,
    PRIMARY KEY ((purchase_id), sale_date)
) WITH CLUSTERING ORDER BY (sale_date desc);



CREATE TABLE IF NOT EXISTS car_maint_history(
    maint_id int,
    mech_id int,
    car_id int,
    cust_id int,
    cust_fullname text,
    maint_date date,
    maint_desc text,
    car_year int,
    car_make text,
    car_model text,
    maint_cost int,
    PRIMARY KEY ((maint_id), maint_date)  
) WITH CLUSTERING ORDER BY (maint_date desc);



CREATE TABLE IF NOT EXISTS car_accident_history (
accident_id int PRIMARY KEY,
car_id int,
accident_date date
PRIMARY KEY ((accident_id), accident_date)
) WITH CLUSTERING ORDER BY (accident_date desc);

