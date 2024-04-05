CREATE KEYSPACE IF NOT EXISTS sale_monitoring
WITH replication = {
    'class': 'SimpleStrategy', 
    'replication_factor': 1 };

USE sale_monitoring;

CREATE TABLE IF NOT EXISTS readings (
    car_id int,
    car_year int,
    car_make text,
    car_model text,
    min_price double(18,2) ,
    max_price double(18,2) ,
    milage    int,
    color     text,
    location_town text ,
    location_state text,
    rating int,
    repair_num int,
    search_count int,
    trade_history list,
    PRIMARY KEY (car_id)
) WITH CLUSTERING ORDER BY (car_year DESC);
