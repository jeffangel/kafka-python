import os
import sys
import logging

from dotenv import load_dotenv
from kafka import KafkaConsumer

load_dotenv()
kafka_server = os.getenv('KAFKA_SERVER')
kafka_port = os.getenv('KAFKA_PORT')
topic = os.getenv('KAFKA_TOPIC_NAME')
group_id = os.getenv('KAFKA_GROUP_ID')

bootstrap_servers = [f'{kafka_server}:{kafka_port}']
logging.basicConfig(level = logging.INFO)

# Create Consumer instance
consumer = KafkaConsumer(
    topic,
    bootstrap_servers=bootstrap_servers,
    group_id=group_id,
    auto_offset_reset='earliest'
)

try:
    for message in consumer:
        #print(f"Data: {message.value.decode('utf-8')} from {message.topic}")
        logging.info(f"Data: {message.value.decode('utf-8')} from {message.topic}")
        #sys.stdout.flush()
except KeyboardInterrupt:
    pass
finally:
    consumer.close()
