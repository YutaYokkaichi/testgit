import requests
from bs4 import BeautifulSoup

class Scraper:
    def __init__(self, url):
        self.url = url

    def fetch_data(self):
        response = requests.get(self.url)
        if response.status_code == 200:
            return response.text
        else:
            raise Exception("Failed to fetch data")

    def parse_data(self, html):
        soup = BeautifulSoup(html, 'html.parser')
        return soup
