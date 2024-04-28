from cassandra.cluster import Cluster
from cassandra.auth import PlainTextAuthProvider
from confluent_kafka import Consumer, KafkaError
import json

cassandra_cluster = Cluster (
    ['127.0.0.1'],
    port=9042
)
session = cassandra_cluster.connect('car_purchase_prices')

kafka_conf = {
    'bootstrap.servers': 'localhost:9093',
    'group.id': 'sale_group',
    'auto.offset.reset': 'earliest'   
}

consumer = Consumer(kafka_conf)

topics = ['car_db']
consumer.subscribe(topics)

def car_sale_into_cassandra(event_data):
    
    cql = """
            INSERT INTO car_purchases (purchase_id,car_id,car_year,car_make,car_model,color
                                  ,cust_id,cust_fullname,purchase_price)
                                  VALUES (%s,%s, %s, %s, %s, %s, %s, %s, %s);
          """

    session.execute(cql, (event_data['purchase_id'],event_data['car_id'],event_data['car_year'],
                          event_data['car_make'], event_data['car_model'],event_data['color'],
                          event_data['cust_id'], event_data['cust_fullname'],
                          event_data['purchase_price']))
    
    
def maint_data_into_cassandra(event_data):
    
    cql = """
                INSERT INTO car_maint_history (mech_id, car_id, cust_id, cust_fname, cust_lname, maint_date, maint_desc, 
                                    car_year, car_make, car_model, maint_cost)
                                    VALUES(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)
          """
          
    session.execute(cql, (event_data['mech_id'], (event_data['car_id']), (event_data['cust_id']),  
                           event_data['cust_fname'], event_data['cust_lname'], event_data['maint_date'], 
                           event_data['maint_desc'], event_data['car_year'], event_data['car_make'], 
                           event_data['car_model'], event_data['maint_cost'])) 
    
def accident_into_cassandra(event_data):
    
    cql = """
            INSERT INTO car_accident_history (accident_id,car_id,accident_date)
            VALUES(%s,%s,%s);
          """
    
    session.execute(cql, (event_data['accident_id'], event_data['car_id'],event_data['accident_date']))
    

try:
    while True:
        msg = consumer.poll(timeout=1.0)
        if msg is None: 
            continue
        if msg.error():
            if msg.error().code() == KafkaError._PARTITION_EOF:
                continue
            else:
                print(msg.error())
                break
    
        event_data = json.loads(msg.value().decode('utf-8'))
        
        car_sale_into_cassandra(event_data)
        maint_data_into_cassandra(event_data)
        accident_into_cassandra(event_data)
except KeyboardInterrupt: 
    pass
finally:
    consumer.close()
    cassandra_cluster.shutdown()


    