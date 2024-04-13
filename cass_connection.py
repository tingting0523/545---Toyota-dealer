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
    'group_id': 'sale_group',
    'auto.offset.reset': 'earliest'   
}

consumer = Consumer(kafka_conf)

consumer.subcribe('car_trades')

def project_into_cassandra(event_data):
    
    cql = """
            INSERT INTO car_purchases (car_id,car_year,car_make,car_model, color,
                                          cust_id, cust_wholename, purchase_price, purchase_date)
          """
    

    session.execute(cql, (event_data['car_id'], event_data['car_year'],event_data['car_make'],
                          event_data['car_model'], event_data['color'],event_data['cust_id'],
                          event_data['cust_name'], event_data['purchase_price'],
                          event_data['purchase_date']))
    
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
        
        project_into_cassandra(event_data)
except KeyboardInterrupt: 
    pass
finally:
    consumer.close()
    cassandra_cluster.shutdown()


    