#projects/sendme-test-db/topics/kafka-tryout
import csv
from time import sleep
import json
from google.cloud import pubsub_v1

def publish_messages(project_id: str, topic_id: str) -> None:
    """Publishes multiple messages to a Pub/Sub topic."""

    # project_id = "your-project-id"
    # topic_id = "your-topic-id"

    publisher = pubsub_v1.PublisherClient()
    # The `topic_path` method creates a fully qualified identifier
    # in the form `projects/{project_id}/topics/{topic_id}`
    topic_path = publisher.topic_path(project_id, topic_id)

    #Read data from a csv file
    with open('../assests/acc_records.csv', 'r') as file:
        data_rows = csv.reader(file)
        header = next(data_rows)

        for row in data_rows:
            #this is used to serialize the data and turn it into bytes
            data = json.dumps(row).encode('utf-8')
            #print(type(data)) --> This is a byte object
            # When you publish a message, the client returns a future.
            future = publisher.publish(topic_path, data)
            print(future.result())
            #sleep(5)

    print(f"Published messages to {topic_path}.")

if __name__ == '__main__':
    publish_messages('sendme-test-db', 'kafka-test')