from cassandra.cluster import Cluster
from cassandra.auth import PlainTextAuthProvider
from confluent_kafka import Consumer, KafkaError
import json

cassandra_cluster = Cluster (
    ['127.0.0.1'],
    port=9042
)
session = cassandra_cluster.connect('sale_monitoring')

kafka_conf = {
    'bootstrap.servers': 'localhost:9093',
    'group_id': 'sale_group',
    'auto.offset.reset': 'earliest'   
}

consumer = Consumer(kafka_conf)

consumer.subcribe('sale')


### Execute Cassandra queries in this section ###

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
    
    ## Project into cassandra the event data ##
    

except KeyboardInterrupt:
    pass

finally:
    consumer.close()
    cassandra_cluster.shutdown()
    