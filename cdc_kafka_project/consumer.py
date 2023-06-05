from kafka import KafkaConsumer
import json
import os
#from socket import gethostbyname, gethostname

# Set the broker address
host = os.getenv('HOST_IP')
print(host)
bootstrap_servers = f'{host}:9092'

# Create a KafkaConsumer instance
consumer = KafkaConsumer(
    bootstrap_servers=bootstrap_servers,
    group_id='nodejs-consumer',
    auto_offset_reset='earliest',
    enable_auto_commit=True,
    value_deserializer=lambda x: json.loads(x.decode('utf-8'))
)

# Subscribe to the topic
consumer.subscribe(topics=['debezium.public.transactions'])
#consumer.subscribe(topics = ["debezium.public.transactions"])

# Start consuming messages
try:
    for msg in consumer:
        print(msg)
        # value = msg.value
        # key = msg.key
        # print(value['payload'])

except KeyboardInterrupt:
    pass

finally:
    consumer.close()
