import csv
import json
from typing import List, Dict
from kafka import KafkaProducer
from kafka.errors import KafkaTimeoutError
from time import sleep
from schema import Ride


class JsonProducer(KafkaProducer):
    def __init__(self, props: Dict):
        self.producer = KafkaProducer(**props)

    @staticmethod
    def read_records(resource_path: str):
        records = []
        with open(resource_path, 'r') as f:
            reader = csv.reader(f)
            header = next(reader)  # skip the header row
            for row in reader:
                records.append(Ride(arr=row))
        return records

    def publish_rides(self, topic: str, messages: List[Ride]):
        for ride in messages:
            try:
                record = self.producer.send(topic=topic, key=ride.customer_id, value=ride)
                #print('Record {} successfully produced at offset {}'.format(ride.customer_id, record.get().offset))
                print(ride)
            except KafkaTimeoutError as e:
                print(e.__str__())
            sleep(10)


if __name__ == '__main__':
    # Config Should match with the KafkaProducer expectation
    config = {
        'bootstrap_servers': ['localhost:9092'],
        'key_serializer': lambda key: str(key).encode(),
        'value_serializer': lambda x: json.dumps(x.__dict__, default=str).encode('utf-8')
    }
    producer = JsonProducer(props=config)
    rides = producer.read_records(resource_path="acc_records.csv")
    producer.publish_rides(topic="test_topic", messages=rides)