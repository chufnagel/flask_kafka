# Kafka and Python
Working through the [Build a Distributed Streaming System with Apache Kafka and Python](https://scotch.io/tutorials/build-a-distributed-streaming-system-with-apache-kafka-and-python) tutorial by [Mwaleh Muturi](https://scotch.io/@mwaleh)

A brief experiment with kafka-python. A short video is converted to a series of .png files, sent through Kafka, and visualized on a Flask server.

**Note:** Currently encountering issues with FFMPEG on Linux distros; can by bypassed via Docker or compiling opencv with FFMPEG.

## Requirements
* [Pipenv](https://pipenv.readthedocs.io/en/latest/)
* Python 3.4 - 3.6
* [Kafka](http://www.kafka.apache.org)

* OpenCV with FFMPEG (Linux distros only)

## Dependencies

See Pipfile for more information.
* [kafka-python](https://kafka-python.readthedocs.io/en/master/index.html)
* [opencv-python](https://pypi.org/project/opencv-python/)
* [Flask](http://flask.pocoo.org/)
* flake8

## Usage Instructions

1. `pipenv install`
1. Start local Kafka cluster in one terminal tab:

```sh
zookeeper-server-start /usr/local/etc/kafka/zookeeper.properties & kafka-server-start /usr/local/etc/kafka/server.properties
```
1. Run [producer.py](producer.py) in another terminal tab
1. Run [consumer.py](consumer.py) in another terminal tab
1. Navigate to http://localhost:5000 to see the corgis run!

The kafka client address can be modified in [config.yml](config.yml).

## Acknowledgements

* Video shamelessly cribbed from [Anne Indergaard](https://www.youtube.com/watch?v=Dsg8JccRZCw)
