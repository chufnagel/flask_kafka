import time
import cv2
from kafka import SimpleProducer, KafkaClient

kafka = KafkaClient("localhost:9092")
producer = SimpleProducer(kafka)

topic = "testTopic"

def video_emitter(video):
    video = cv2.VideoCapture(video)
    print("emitting...")

    while (video.isOpened):
        # read the image in each frame
        success, image = video.read()
        # check if file read to end successfully
        if not success:
            break
        # convert the image png
        ret, jpeg = cv2.imencode(".png", image)
        # convert image to bytes, send to Kafka
        producer.send_messages(topic, jpeg.tobytes())
        # reduce cpu usage by sleeping
        time.sleep(0.2)
    # clear capture
    video.release()
    print("done emitting")


if __name__ == "__main__":
    video_emitter("video.mp4")
