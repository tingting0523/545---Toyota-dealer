import json
from confluent_kafka import Producer
import mysql.connector
from mysql.connector import Error
from faker import Faker
import time
import sale_data as sale_data_mod
import maint_data as maint_data_mod
import accident_data as acc_data_mod

fake = Faker()


def acked(err, msg):
    if err is not None:
        print("Failed to deliver message: %s: %s" % (str(msg), str(err)))
    else:
        print("Message produced: %s" % (str(msg)))

def buildConnection():
    connection = mysql.connector.connect ( host='localhost', database='toyota_dealer', user='root', password='root')
    return connection


        
def sale_data_prt():
    sale_data = sale_data_mod.sale_data_insert()
    return (f"{sale_data['cust_fullname']} purchased a {sale_data['color']} "
                 f"{sale_data['car_year']} {sale_data['car_make']} {sale_data['car_model']}"
                 f" for ${sale_data['sale_price']} on {sale_data['sale_date']}.")  
    
def maint_data_prt():
    maint_data = maint_data_mod.maint_data_insert()
    return (f"On {maint_data['maint_date']} the mechanic will {maint_data['maint_desc']} on {maint_data['cust_fname']} {maint_data['cust_lname']}'s "
                  f"{maint_data['car_year']} {maint_data['car_make']} {maint_data['car_model']} "
                  f"for ${maint_data['maint_cost']}.")  
    
def acc_data_prt():
    acc_data = acc_data_mod.accident_data_insert()
    return (f"Car accident occurred on {acc_data['accident_date']}.")
        
            
def event_data_serialize(ins_stment,prt_statement):
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
            
            event_data = [ins_stment]
            
            event_json = json.dumps(event_data) # serialize the data to an event.
            connection.commit()
            producer.produce("car_db", event_json.encode('utf-8'), callback=acked)
            producer.flush()
            
            
            print(prt_statement)
            
                        
    except Error as e:
        print("Error while connecting to MySQL", e)
    finally:
        if (connection.is_connected()):
            cursor.close()
            connection.close()            
           
def main():
    while True:
        sale_ins = sale_data_mod.sale_data_insert()
        maint_ins = maint_data_mod.maint_data_insert()
        accident_ins = acc_data_mod.accident_data_insert()
        
        event_data_serialize(sale_ins,sale_data_prt())
        time.sleep(1)
        event_data_serialize(maint_ins,maint_data_prt())
        time.sleep(1)
        event_data_serialize(accident_ins,acc_data_prt())
        time.sleep(1)
        
       

if __name__ == '__main__':
    main()

            





