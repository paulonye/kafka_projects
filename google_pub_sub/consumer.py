import json
from time import sleep
from google.cloud import pubsub_v1
from typing import Optional
from sheet_connect import append_new_data
from push import push_error

def receive_messages(
    project_id: str, subscription_id: str, timeout: Optional[float] = None
) -> None:
    """Receives messages from a pull subscription."""
    
    from concurrent.futures import TimeoutError

    # TODO(developer)
    # project_id = "your-project-id"
    # subscription_id = "your-subscription-id"
    # Number of seconds the subscriber should listen for messages
    # timeout = 5.0

    subscriber = pubsub_v1.SubscriberClient()
    # The `subscription_path` method creates a fully qualified identifier
    # in the form `projects/{project_id}/subscriptions/{subscription_id}`
    subscription_path = subscriber.subscription_path(project_id, subscription_id)

    def callback(message: pubsub_v1.subscriber.message.Message) -> None:
        #print(f"Received {message}.")
        message.ack()
        message = message.data.decode('utf-8')
        data = json.loads(message)
        append_new_data([data],'trans','test_sheet')
        print(data)
        #sleep(3)


    streaming_pull_future = subscriber.subscribe(subscription_path, callback=callback)
    print(f"Listening for messages on {subscription_path}..\n")

    # Wrap subscriber in a 'with' block to automatically call close() when done.
    with subscriber:
        breakpoint()
        try:
            # When `timeout` is not set, result() will block indefinitely,
            # unless an exception is encountered first.
            streaming_pull_future.result(timeout=timeout)
        except TimeoutError as e:
            streaming_pull_future.cancel()  # Trigger the shutdown.
            streaming_pull_future.result()  # Block until the shutdown is complete.
        except Exception as e:
            push_error("broken pipleine")


if __name__ == '__main__':
    receive_messages('sendme-test-db', 'mySub')
    #push_error('failed pipeline')