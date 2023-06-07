# BASIC KAKKA PROJECT
> This project involnes using Kafka docker image to test run an application service. In this project, the Kafka infraustructure is hosted on a local machine using docker.

## Steps for Project
1. A kafka docker image is used to launch the kafka broker and zookerper
2. A producer client is used to generate events that will be pushed to the kafka topic in the broker.
3. A consumer client is used to read the message from the kafka topic.