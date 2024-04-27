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


def sale_data_sel(cur_obj, car_id, cust_id):
       cars_query = "SELECT car_year, car_make, car_model, color FROM car_list WHERE car_id = %s"
           
       cur_obj.execute(cars_query, (car_id,))
        
       car_info_fetch = cur_obj.fetchone()

       cust_query = "SELECT cust_fname, cust_lname FROM customers WHERE cust_id = %s"
       
       cur_obj.execute(cust_query, (cust_id,))
       
       cust_info_fetch = cur_obj.fetchone()
       
       price_range_query = "SELECT min_price, max_price FROM car_list WHERE car_id = %s"
       
       cur_obj.execute(price_range_query, (car_id,))
       
       price_range_fetch = cur_obj.fetchone()
       
       
       car_info = {
           'car_year': car_info_fetch[0],
           'car_make': car_info_fetch[1],
           'car_model': car_info_fetch[2],
           'color': car_info_fetch[3]
       }
       
       cust_info = {
           'cust_fname': cust_info_fetch[0],
           'cust_lname': cust_info_fetch[1]
       }
       
       price_range = {
           'min_price': price_range_fetch[0],
           'max_price': price_range_fetch[1]
       }
       
       
       return car_info, cust_info, price_range
   
def sale_data_insert():
    car_id = random.randint(1,20)
    cust_id = random.randint(1,20)
    
    connection = buildConnection() 
    cursor = connection.cursor()
    
    car_info, cust_info, price_range = sale_data_sel(cursor,car_id,cust_id)
    
    car_year = car_info['car_year']
    car_make = car_info['car_make']
    car_model = car_info['car_model']
    color = car_info['color']
    
    cust_fname = cust_info['cust_fname']
    cust_lname= cust_info['cust_lname']
    sale_price = round((random.uniform(price_range['min_price'],price_range['max_price'])),2)
    sale_date = str(fake.date_between(start_date='-2y', end_date='-1y'))
    cust_fullname = cust_fname + " " + cust_lname
    
    
    sale_ins_query = """INSERT INTO car_purchases 
                        (car_id, car_year, car_make, car_model, color, 
                        cust_id, cust_fullname, sale_price, 
                        sale_date) VALUES 
                        (%s,%s,%s,%s,%s,%s,%s,%s,%s)"""
    
    purchase_info = (car_id,car_year,car_make,car_model,color,cust_id,cust_fullname,sale_price,sale_date)
    cursor.execute(sale_ins_query, purchase_info)
    
    sale_data = {
        'car_id': car_id,
        'car_year': car_year,
        'car_make': car_make,
        'car_model': car_model,
        'color': color,
        'cust_id': cust_id,
        'cust_fullname' : cust_fullname,
        'sale_price': sale_price,
        'sale_date': sale_date     
    }
    
    return sale_data   

def maint_data_sel(cur_obj,car_id):
    cust_sel_query = "SELECT cust_id, cust_fname, cust_lname FROM customers WHERE car_id = %s"
    cur_obj.execute(cust_sel_query, (car_id,))
    cust_list_fetch = cur_obj.fetchone()
    
    maint_sel_query = """SELECT mech_id, maint_desc, car_year, car_make, car_model 
                            FROM car_maint_events 
                            WHERE car_id = %s"""
    cur_obj.execute(maint_sel_query, (car_id,))
    maint_info_fetch = cur_obj.fetchone()
    
    cust_list = {
        'cust_id': cust_list_fetch[0],
        'cust_fname': cust_list_fetch[1],
        'cust_lname': cust_list_fetch[2]
    }
    
    maint_info = {
        'mechanic_id': maint_info_fetch[0],
        'maint_descrip': maint_info_fetch[1],
        'car_year': maint_info_fetch[2],
        'car_make': maint_info_fetch[3],
        'car_model': maint_info_fetch[4]
    }
    
    return cust_list, maint_info
       
    
        
def maint_data_insert():
    
            connection = buildConnection() 
            cursor = connection.cursor(buffered=True)
           
            car_id = random.randint(5,10)
            cust_info, maint_info = maint_data_sel(cursor,car_id)

            cust_id = cust_info['cust_id']
            cust_fname = cust_info['cust_fname']
            cust_lname = cust_info['cust_lname']
            mech_id = maint_info['mechanic_id']
            maint_desc = maint_info['maint_descrip']
            car_year = maint_info['car_year']
            car_make = maint_info['car_make']
            car_model = maint_info['car_model']
            
            maint_cost = random.randint(20,150)
            maint_date = str(fake.date_between(start_date='+1y', end_date='+2y'))

            car_maint_query = """INSERT INTO car_maint_history
                                    (mech_id, car_id, cust_id, cust_fname, cust_lname, maint_date, maint_desc, 
                                    car_year, car_make, car_model, maint_cost)
                                    VALUES(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"""
                                    
            maint_info = (mech_id, car_id, cust_id, cust_fname, cust_lname, maint_date, 
                          maint_desc, car_year, car_make,car_model, maint_cost)
            cursor.execute(car_maint_query,maint_info)
     
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
        
def sale_data_prt():
    sale_data = sale_data_insert()
    return (f"{sale_data['cust_fullname']} purchased a {sale_data['color']} "
                 f"{sale_data['car_year']} {sale_data['car_make']} {sale_data['car_model']}"
                 f" for ${sale_data['sale_price']} on {sale_data['sale_date']}.")  
    
def maint_data_prt():
    maint_data = maint_data_insert()
    return (f"On {maint_data['maint_date']} the mechanic will {maint_data['maint_desc']} on {maint_data['cust_fname']} {maint_data['cust_lname']}'s "
                  f"{maint_data['car_year']} {maint_data['car_make']} {maint_data['car_model']} "
                  f"for ${maint_data['maint_cost']}")  
        
            
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
        sale_ins = sale_data_insert()
        maint_ins = maint_data_insert()
        
        event_data_serialize(sale_ins,sale_data_prt())
        time.sleep(1)  # Pause for 1 second before the next insert
        event_data_serialize(maint_ins,maint_data_prt())
        time.sleep(1)
        
       

if __name__ == '__main__':
    main()

            





