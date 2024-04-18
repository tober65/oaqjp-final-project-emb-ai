from flask import Flask
from EmotionDetection.emotion_detection import emotion_detector

app = Flask(__name__)

@app.route("/")
def hello_world():
    return "<p>Hello, World!</p>"

@app.route("/emotionDetector/<statement>")
def show_emotion_detector():
    return emotion_detector(statement)
