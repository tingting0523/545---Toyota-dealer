import json
from confluent_kafka import Producer
import mysql.connector
from mysql.connector import Error
import random
from datetime import datetime
import time


def acked(err, msg):
    if err is not None:
        print("Failed to deliver message: %s: %s" % (str(msg), str(err)))
    else:
        print("Message produced: %s" % (str(msg)))

def buildConnection():
    connection = mysql.connector.connect ( host='localhost', database='toyota_dealer', user='root', password='root')
    return connection

def mysql_conn_func():
    try:
       connection = buildConnection()
       cursor = connection.cursor(dictionary=True)
       
       
       ### function logic ### 
    
    except mysql.connector.Error as err:
        print("MySQL Error: ", err)
    finally:
        if connection.is_connected():
            cursor.close()
            connection.close()

def kafka_conn_func():
    try:
        # Kafka configuration
        conf = {
            'bootstrap.servers': "localhost:9093",  
        }
       
        producer = Producer(**conf)
    
        connection = buildConnection()
        if connection.is_connected():
            db_Info = connection.get_server_info()
            print("Connected to MySQL Server version ", db_Info)
           
            cursor = connection.cursor()
            
             ### function logic ### 
             
             
        event_json = json.dumps(car_repairs) # serialize the data to an event.
        connection.commit()
        producer.produce("toyota_dealer", event_json.encode('utf-8'), callback=acked)
        
    except Error as e:
        print("Error while connecting to MySQL", e)
    finally:
        if (connection.is_connected()):
            cursor.close()
            connection.close()
        
if __name__ == '__main__':
    main()
        
            





