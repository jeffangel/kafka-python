import os
import logging
import time

from dotenv import load_dotenv
from faker import Faker
from kafka import KafkaProducer

load_dotenv()
kafka_server = os.getenv('KAFKA_SERVER')
kafka_port = os.getenv('KAFKA_PORT')
topic = os.getenv('KAFKA_TOPIC_NAME')

bootstrap_servers = [f'{kafka_server}:{kafka_port}']
producer = KafkaProducer(bootstrap_servers=bootstrap_servers)
logging.basicConfig(level = logging.INFO)
fake = Faker()
i = 0

def mock_alert(id):
    return {"Id": id, "Name": fake.name(), "Message": fake.text(), "Date": fake.date(), "Phone": fake.phone_number() }

while True:
    msg = mock_alert(i)
    producer.send(topic, str(msg).encode('utf-8'))
    producer.flush()
    logging.info(f"Data {i}")
    time.sleep(3)
    i+=1
