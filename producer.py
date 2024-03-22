from kafka import KafkaProducer
from faker import Faker
import json
from time import sleep

producer = KafkaProducer(bootstrap_servers=['localhost:9092'])
fake_data = Faker()


for _ in range(1000):
    data = {
        'First name': fake_data.first_name(),
        'City': fake_data.city(),
        'Country': fake_data.country()}
    payload = json.dumps(data).encode('utf-8')

    result = producer.send('test', value=payload)
    print(result)
    sleep(1)
