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



def car_purchase_event(cur_obj, car_id, cust_id):
       cars_query = "SELECT car_year, car_make, car_model, color FROM car_list WHERE car_id = %s"
           
       cur_obj.execute(cars_query, (car_id,))
        
       car_info_row= cur_obj.fetchone()

       cust_query = "SELECT cust_fname, cust_lname FROM customers WHERE cust_id = %s"
       
       cur_obj.execute(cust_query, (cust_id,))
       
       cust_info_row = cur_obj.fetchone()
       
       price_range_query = "SELECT min_price, max_price FROM car_list WHERE car_id = %s"
       
       cur_obj.execute(price_range_query, (car_id,))
       
       price_range = cur_obj.fetchone()
       
       return car_info_row, cust_info_row, price_range

def car_servicing_event(cur_obj,car_id):
    cust_sel_query = "SELECT cust_id, cust_fname, cust_lname FROM customers WHERE car_id = %s"
    cur_obj.execute(cust_sel_query, (car_id,))
    cust_list = cur_obj.fetchone()
    
    maint_sel_query = """SELECT mech_id, maint_desc, car_year, car_make, car_model 
                            FROM car_maint_events 
                            WHERE car_id = %s"""
    cur_obj.execute(maint_sel_query, (car_id,))
    servicing_info = cur_obj.fetchone()
    
    return cust_list, servicing_info
       
def sale_data_insert(cur_obj):
    car_id = random.randint(1,20)
    cust_id = random.randint(1,20)
    
    car_info = car_purchase_event(cur_obj, car_id,cust_id)[0]
    cust_info = car_purchase_event(cur_obj, car_id,cust_id)[1]
    price_range = car_purchase_event(cur_obj, car_id,cust_id)[2]
    car_year = car_info[0]
    car_make = car_info[1]
    car_model = car_info[2]
    color = car_info[3]
    
    cust_fname = cust_info[0]
    cust_lname= cust_info[1]
    sale_price = round((random.uniform(price_range[0],price_range[1])),2)
    sale_date = fake.date_time().isoformat()
    cust_wholename = cust_fname + " " + cust_lname
    
    
    car_db_query = """INSERT INTO car_purchases 
                        (car_id, car_year, car_make, car_model, color, 
                        cust_id, cust_wholename, sale_price, 
                        sale_date) VALUES 
                        (%s,%s,%s,%s,%s,%s,%s,%s,%s)"""
    
    purchase_info = (car_id,car_year,car_make,car_model,color,cust_id,cust_wholename,sale_price,sale_date)
    cur_obj.execute(car_db_query, purchase_info)
    
    sale_data = {
        'car_id': car_id,
        'car_year': car_year,
        'car_make': car_make,
        'car_model': car_model,
        'color': color,
        'cust_id': cust_id,
        'cust_wholename' : cust_wholename,
        'sale_price': sale_price,
        'sale_date': sale_date     
    }
    
    return sale_data       


        
def maint_data_insert(cur_obj):
           
            car_id = random.randint(6,15)
            cust_info, maint_info = car_servicing_event(cur_obj,car_id)
            cust_info = car_servicing_event(cur_obj,car_id)[0]
            maint_info = car_servicing_event(cur_obj,car_id)[1]
            cust_id = cust_info[0]
            cust_fname = cust_info[1]
            cust_lname = cust_info[2]
            mech_id = maint_info[0]
            maint_desc = maint_info[1]
            car_year = maint_info[2]
            car_make = maint_info[3]
            car_model = maint_info[4]
            
            maint_cost = random.randint(20,150)
            maint_date = fake.date_time().isoformat()

            car_maint_query = """INSERT INTO car_maint_history
                                    (mech_id, car_id, cust_id, cust_fname, cust_lname, maint_date, maint_desc, 
                                    car_year, car_make, car_model, maint_cost)
                                    VALUES(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"""
                                    
            maint_info = (mech_id, car_id, cust_id, cust_fname, cust_lname, maint_date, 
                          maint_desc, car_year, car_make,car_model, maint_cost)
            cur_obj.execute(car_maint_query,maint_info)
            #refactor ids in event
            maint_data = {
                'mech_id': mech_id,
                'car_id': car_id,
                'cust_id': cust_id,
                'cust_fname': cust_fname,
                'cust_lname': cust_lname,
                'maint_date': maint_date,
                'maint_desc': maint_desc,
                'car_year': car_year,
                'car_make': car_make,
                'car_model': car_model,
                'maint_cost': maint_cost
            }
            
            return maint_data
        

        
            
def sale_data_serialize():
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
                              (car_id, car_year, car_make, car_model, color, 
                               cust_id, cust_wholename, purchase_price, 
                               purchase_date) VALUES 
                               (%s,%s,%s,%s,%s,%s,%s,%s,%s)"""
            
            purchase_info = (car_id,car_year,car_make,car_model,color,cust_id,cust_wholename,purchase_price,purchase_date)
            cursor.execute(car_db_query, purchase_info)
            
            purchase_event = {
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
            
            
            event_json = json.dumps(maint_data) # serialize the data to an event.
            connection.commit()
            producer.produce("car_db", event_json.encode('utf-8'), callback=acked)
            producer.flush()
            
            print(f"On {maint_data['maint_date']} the mechanic will {maint_data['maint_desc']} on {maint_data['cust_fname']} {maint_data['cust_lname']}'s "
                  f"{maint_data['car_year']} {maint_data['car_make']} {maint_data['car_model']} "
                  f"for ${maint_data['maint_cost']}")
            
    except Error as e:
        print("Error while connecting to MySQL", e)
    finally:
        if (connection.is_connected()):
            cursor.close()
            connection.close()       
        
def main():
    while True:
        sale_data_serialize()
        time.sleep(1)  # Pause for 1 second before the next insert
        maint_data_serialize()
        time.sleep(1)
        
       

if __name__ == '__main__':
    main()

            





