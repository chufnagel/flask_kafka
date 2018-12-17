from flask import Flask, Response
from kafka import KafkaConsumer
import yaml

config = yaml.safe_load(open("config.yml"))
kafka_client = config["kafka_client"]
client = f'{kafka_client["uri"]}:{kafka_client["port"]}'

consumer = KafkaConsumer(
    "testTopic", group_id="view", bootstrap_servers=[client]
)

app = Flask(__name__)


@app.route("/")
def index():
    # return a multipart response
    return Response(kafkastream(),
                    mimetype="multipart/x-mixed-replace; boundary=frame")


def kafkastream():
    for msg in consumer:
        yield (b'--frame\r\n'
                b'Content-Type: image/png\r\n\r\n' + msg.value + b'\r\n\r\n')


if __name__ == "__main__":
    app.run(host="0.0.0.0", debug=True)
