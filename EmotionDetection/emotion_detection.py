import requests
import json

def emotion_detector(text_to_analyze):
    url = 'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'
    headers = {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}
    input = { "raw_document": { "text": text_to_analyze } }
    
    resp = requests.post(url, json=input, headers=headers)

    if (resp.status_code == 400):
        return json.dumps({"anger": None, "disgust": None, "fear": None, "joy": None, \
        "sadness": None, "dominant_emotion": None})

    prediction = json.loads(resp.text)
    emotion = prediction["emotionPredictions"][0]["emotion"]

    dominant_emotion_score = 0.0
    dominant_emotion = ""

    emotion_names = emotion.keys()

    for e in emotion_names:
        if emotion[e] > dominant_emotion_score:
            dominant_emotion = e
            dominant_emotion_score = emotion[e]

    emotion["dominant_emotion"] = dominant_emotion

    return json.dumps(emotion, indent=0)
