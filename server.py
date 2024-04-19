from flask import Flask
from EmotionDetection.emotion_detection import emotion_detector
import json

app = Flask(__name__)

@app.route("/emotionDetector/<string:statement>")
def show_emotion_detector(statement):
    resp = json.loads(emotion_detector(statement))
    return_string = "For the given statement, the system response is" \
     f"'anger': {resp['anger']}, 'disgust': {resp['disgust']}, " \
     f"'fear': {resp['fear']}, 'joy': {resp['joy']} and 'sadness': {resp['sadness']}." \
     f" The dominant emotion is {resp['dominant_emotion']}."
    return return_string
