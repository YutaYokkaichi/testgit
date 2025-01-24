import os

def create_project_structure():
    directories = [
        'src',
        'tests'
    ]
    
    files = {
        'main.py': '',
        'README.md': '# Project Title\n\nProject description.',
        'requirements.txt': '',
        'src/__init__.py': '',
        'src/scraper.py': 'import requests\nfrom bs4 import BeautifulSoup\n\nclass Scraper:\n    def __init__(self, url):\n        self.url = url\n\n    def fetch_data(self):\n        response = requests.get(self.url)\n        if response.status_code == 200:\n            return response.text\n        else:\n            raise Exception("Failed to fetch data")\n\n    def parse_data(self, html):\n        soup = BeautifulSoup(html, \'html.parser\')\n        return soup\n',
        'src/data_manager.py': 'import json\n\nclass DataManager:\n    def __init__(self, file_path):\n        self.file_path = file_path\n\n    def save_data(self, data):\n        with open(self.file_path, \'w\') as file:\n            json.dump(data, file)\n\n    def load_data(self):\n        with open(self.file_path, \'r\') as file:\n            return json.load(file)\n',
        'src/utils.py': 'def clean_data(data):\n    return data\n',
        'tests/__init__.py': '',
        'tests/test_scraper.py': 'import unittest\nfrom src.scraper import Scraper\n\nclass TestScraper(unittest.TestCase):\n    def test_fetch_data(self):\n        scraper = Scraper(\'https://example.com\')\n        data = scraper.fetch_data()\n        self.assertIsNotNone(data)\n\nif __name__ == \'__main__\':\n    unittest.main()\n',
        'tests/test_data_manager.py': '',
        'tests/test_utils.py': ''
    }

    for directory in directories:
        os.makedirs(directory, exist_ok=True)
    
    for file_path, content in files.items():
        with open(file_path, 'w') as file:
            file.write(content)

if __name__ == "__main__":
    create_project_structure()