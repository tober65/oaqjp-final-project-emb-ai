import unittest
import json

from EmotionDetection.emotion_detection import emotion_detector

class TestEmotionDetection(unittest.TestCase):
    def test_joy(self):
        reply = emotion_detector("I am glad this happened")
        d = json.loads(reply)
        self.assertEqual(d["dominant_emotion"], "joy")

    def test_anger(self):
        reply = emotion_detector("I am really mad about this")
        d = json.loads(reply)
        self.assertEqual(d["dominant_emotion"], "anger")

    def test_disgust(self):
        reply = emotion_detector("I feel disgusted just hearing about this")
        d = json.loads(reply)
        self.assertEqual(d["dominant_emotion"], "disgust")

    def test_sadness(self):
        reply = emotion_detector("I am so sad about this")
        d = json.loads(reply)
        self.assertEqual(d["dominant_emotion"], "sadness")

    def test_fear(self):
        reply = emotion_detector("I am really afraid that this will happen")
        d = json.loads(reply)
        self.assertEqual(d["dominant_emotion"], "fear")

if __name__ == '__main__':
    unittest.main()
