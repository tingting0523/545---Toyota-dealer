import random
import mysql_connection


def accident_data_sel(cur_obj,car_id):
    accident_sel_query = """SELECT accident_date 
                            FROM car_accident_history 
                            WHERE car_id = %s"""
   
    
    cur_obj.execute(accident_sel_query, (car_id,))
    
    accidents_fetch = cur_obj.fetchone()
    
    accident_info = {
        'accident_date': accidents_fetch[0]
    }
    
    return accident_info


def accident_data_insert():
    
    connection = mysql_connection.buildConnection() 
    cursor = connection.cursor(buffered=True)
    
    car_id = random.randint(1,5)
    
    acc_info = accident_data_sel(cursor,car_id)
    
    accident_date = acc_info['accident_date']
    
    acc_data_query = """INSERT INTO car_accident_history (car_id, accident_date)
                        VALUES (%s,%s)"""
                        
    acc_info = (car_id,accident_date)
    
    cursor.execute(acc_data_query,acc_info)

    acc_data = {
       'car_id': str(car_id),
       'accident_date': str(accident_date)
    }
    
    return acc_data
    