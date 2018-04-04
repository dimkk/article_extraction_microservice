import unittest
import requests
import json
import sys

class TestArticleService(unittest.TestCase):
    def test_article(self):
        payload = {'url': 'https://www.newyorker.com/news/daily-comment/when-martin-luther-king-jr-became-a-leader'}
        response = requests.get('http://localhost:8000/article', params=payload)
        self.assertEqual(response.json(), {'article'})

if __name__ == "__main__":
    unittest.main()
