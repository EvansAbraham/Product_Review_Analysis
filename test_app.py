import re
import unittest
from app import app

class SentimentAnalysisTestCase(unittest.TestCase):
    
    def setUp(self):
        app.config['TESTING'] = True
        self.client = app.test_client()

    def test_index_page(self):
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'Enter your review', response.data)

    def test_positive_review(self):
        response = self.client.post('/', data={'review': 'I absolutely loved it!'})
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'Positive', response.data)
        self.assertIn('😄'.encode('utf-8'), response.data)

    def test_negative_review(self):
        response = self.client.post('/', data={'review': 'This was terrible and disappointing.'})
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'Negative', response.data)
        self.assertIn('😔'.encode('utf-8'), response.data)

    def test_neutral_review(self):
        response = self.client.post('/', data={'review': 'It was fine, not bad but not great either.'})
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'Neutral', response.data)
        self.assertIn('😐'.encode('utf-8'), response.data)

    def test_sentiment_score(self):
        response = self.client.post('/', data={'review': 'A very average experience.'})
        self.assertEqual(response.status_code, 200)
        
        # Use regex to locate the score within the 'score' class in HTML
        result_str = response.data.decode('utf-8')
        match = re.search(r'<span class="score">([0-4]\.\d|5\.0)</span>', result_str)
        
        if match:
            score = float(match.group(1))
            self.assertTrue(0.0 <= score <= 5.0, "Score is out of expected range (0.0 - 5.0)")
        else:
            self.fail("Score could not be extracted from response")

if __name__ == '__main__':
    unittest.main()
