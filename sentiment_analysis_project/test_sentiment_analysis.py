import unittest
from SentimentAnalysis.sentiment_analysis import sentiment_analyzer

class TestSentimentAnalyzer(unittest.TestCase):
    def test_sentiment_analyzer(self):
        request_one = sentiment_analyzer("I love working with Python")
        self.assertEqual(request_one["label"], "SENT_POSITIVE")

        request_two = sentiment_analyzer("I hate working with Python")  # Corrected typo
        self.assertEqual(request_two["label"], "SENT_NEGATIVE")

        request_three = sentiment_analyzer("I am neutral on Python")  # Corrected typo and adjusted sentiment
        self.assertEqual(request_three["label"], "SENT_NEUTRAL")

if __name__ == '__main__':
    unittest.main()
