CREATE KEYSPACE IF NOT EXISTS trades_and_servicing
WITH replication = {
    'class': 'SimpleStrategy', 
    'replication_factor': 1 };

USE sale_monitoring;

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
