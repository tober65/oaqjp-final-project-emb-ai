"""
Uses Flask to render a web page
"""

import json
from flask import Flask, render_template, request
from EmotionDetection.emotion_detection import emotion_detector

app = Flask(__name__)

@app.route("/")
def render_index_page():
    """Renders the index page"""
    return render_template('index.html')

@app.route("/emotionDetector")
def show_emotion_detector():
    """Calls the emotion_detector module to analyze the given text"""
    statement = request.args.get("textToAnalyze")
    resp = json.loads(emotion_detector(statement))

    if resp['dominant_emotion'] is None:
        return "Invalid text! Please try again!"

    return_string = "For the given statement, the system response is" \
     f"'anger': {resp['anger']}, 'disgust': {resp['disgust']}, " \
     f"'fear': {resp['fear']}, 'joy': {resp['joy']} and 'sadness': {resp['sadness']}." \
     f" The dominant emotion is {resp['dominant_emotion']}."
    return return_string
