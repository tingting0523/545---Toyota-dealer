import random
from faker import Faker
import mysql_connection

fake = Faker()



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
    
    connection = mysql_connection.buildConnection()
    cursor = connection.cursor()
    
    car_info, cust_info, price_range = sale_data_sel(cursor,car_id,cust_id)
    
    car_year = car_info['car_year']
    car_make = car_info['car_make']
    car_model = car_info['car_model']
    color = car_info['color']
    
    cust_fname = cust_info['cust_fname']
    cust_lname= cust_info['cust_lname']
    sale_price = format(random.uniform(price_range['min_price'],price_range['max_price']),'.2f')
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