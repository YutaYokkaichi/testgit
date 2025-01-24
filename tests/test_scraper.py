import unittest
from src.scraper import Scraper

class TestScraper(unittest.TestCase):
    def test_fetch_data(self):
        scraper = Scraper('https://example.com')
        data = scraper.fetch_data()
        self.assertIsNotNone(data)

if __name__ == '__main__':
    unittest.main()
