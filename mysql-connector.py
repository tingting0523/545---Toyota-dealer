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
        
        
# mysql error message ##

# except mysql.connector.Error as err:
#         print("MySQL Error: ", err)
#     finally:
#         if connection.is_connected():
#             cursor.close()
#             connection.close()


#create mysql & Kafka connections

#   conf = {
#             'bootstrap.servers': "localhost:9093",  # Change this to your Kafka server configuration
#         }
#         # Create Producer instance
#         producer = Producer(**conf)
#         # Connect to the MySQL database
#         connection = buildConnection()
#         if connection.is_connected():
#             db_Info = connection.get_server_info()
#             print("Connected to MySQL Server version ", db_Info)

#             cursor = connection.cursor()



# if __name__ == '__main__':
#     main()