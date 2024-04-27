import json
from confluent_kafka import Producer
import mysql.connector
from mysql.connector import Error
import random
from datetime import datetime
from faker import Faker
import time

fake = Faker()

def acked(err, msg):
    if err is not None:
        print("Failed to deliver message: %s: %s" % (str(msg), str(err)))
    else:
        print("Message produced: %s" % (str(msg)))

def buildConnection():
    connection = mysql.connector.connect ( host='localhost', database='toyota_dealer', user='root', password='root')
    return connection


def mysql_conn_func(car_id, cust_id):
    try:

       connection = buildConnection() 
       cursor = connection.cursor()
        
       cars_query = "SELECT car_year, car_make, car_model, color FROM car_list WHERE car_id = %s"
           
       cursor.execute(cars_query, (car_id,))
        
       car_info_row= cursor.fetchone()

       cust_query = "SELECT cust_fname, cust_lname FROM customers WHERE cust_id = %s"
       
       cursor.execute(cust_query, (cust_id,))
       
       cust_info_row = cursor.fetchone()
       
       price_range_query = "SELECT min_price, max_price FROM car_list WHERE car_id = %s"
       
       cursor.execute(price_range_query, (car_id,))
       
       price_range = cursor.fetchone()
       
       return car_info_row, cust_info_row, price_range
   
    except mysql.connector.Error as err:
        print("MySQL Error: ", err)
    finally:
        if connection.is_connected():
            cursor.close()
            connection.close()
    

def get_purchase_info():
    try:
        conf = {
            "bootstrap.servers" : "localhost:9093"
         }
        
        producer = Producer(**conf)
        
        connection = buildConnection() 
        cursor = connection.cursor()
        
        
        
        if connection.is_connected():
            db_Info = connection.get_server_info()
            print("Connected to MySQL Server version ", db_Info)

            cursor = connection.cursor()
            purchase_id = random.randint(1,2000)
            car_id = random.randint(1,20)
            cust_id = random.randint(1,20)
            
            car_info, cust_info, price_range = mysql_conn_func(car_id,cust_id)
            
            car_info = mysql_conn_func(car_id,cust_id)[0]
            cust_info = mysql_conn_func(car_id,cust_id)[1]
            price_range = mysql_conn_func(car_id,cust_id)[2]
            car_year = car_info[0]
            car_make = car_info[1]
            car_model = car_info[2]
            color = car_info[3]
           
            cust_fname = cust_info[0]
            cust_lname= cust_info[1]
            purchase_price = round((random.uniform(price_range[0],price_range[1])),2)
            purchase_date = fake.date_time().isoformat()
            cust_wholename = cust_fname + " " + cust_lname
            
            
            car_db_query = """INSERT INTO car_purchases 
                              (purchase_id,car_id,car_year,car_make,car_model,color
                                  ,cust_id,cust_wholename,purchase_price,purchase_date
                               ) VALUES 
                               (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"""
            
            purchase_info = (purchase_id,car_id,car_year,car_make,car_model,color,cust_id,cust_wholename,purchase_price,purchase_date)
            cursor.execute(car_db_query, purchase_info)
            
            purchase_event = {
                'purchase_id': purchase_id,
                'car_id': car_id,
                'car_year': car_year,
                'car_make': car_make,
                'car_model': car_model,
                'color': color,
                'cust_id': cust_id,
                'cust_wholename' : cust_wholename,
                'purchase_price': purchase_price,
                'purchase_date': purchase_date     
            }
            
            
            event_json = json.dumps(purchase_event) # serialize the data to an event.
            connection.commit()
            producer.produce("car_db", event_json.encode('utf-8'), callback=acked)
            
            producer.flush()
            
            print("Event pushed to topic 'car_purchase'.")
            print(f"{cust_wholename} purchased a {color} {car_make} {car_model} for ${purchase_price} on {purchase_date}.")
            
    except Error as e:
        print("Error while connecting to MySQL", e)
    finally:
        if (connection.is_connected()):
            cursor.close()
            connection.close()
            
            
def main():
    while True:
        get_purchase_info()
        time.sleep(1)  # Pause for 1 second before the next insert

if __name__ == '__main__':
    main()

            





