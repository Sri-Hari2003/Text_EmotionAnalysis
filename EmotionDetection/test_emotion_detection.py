import unittest
from emotion_detection import analyze_emotion

class TestSentimentAnalyzer(unittest.TestCase):
    def test_sentiment_analyzer(self):
        result_1, dominant_emotion_1 = analyze_emotion('I am glad this happened')
        self.assertEqual(dominant_emotion_1, 'joy')
        
        result_2, dominant_emotion_2 = analyze_emotion('I am really mad about this')
        self.assertEqual(dominant_emotion_2, 'anger')
        
        result_3, dominant_emotion_3 = analyze_emotion('I feel disgusted just hearing about this')
        self.assertEqual(dominant_emotion_3, 'disgust')
        
        result_4, dominant_emotion_4 = analyze_emotion('I am so sad about this')
        self.assertEqual(dominant_emotion_4, 'sadness')
        
        result_5, dominant_emotion_5 = analyze_emotion('I am really afraid that this will happen')
        self.assertEqual(dominant_emotion_5, 'fear')

if __name__ == '__main__':
    unittest.main()
