import random
from faker import Faker
import mysql_connection

fake = Faker()

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
    
            connection = mysql_connection.buildConnection() 
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