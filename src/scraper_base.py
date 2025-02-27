import requests
from bs4 import BeautifulSoup

class ScraperBase:
    def __init__(self, base_url):
        self.base_url = base_url

    def get_soup(self, url):
        response = requests.get(url, headers={"User-Agent": "Mozilla/5.0"})
        if response.status_code == 200:
            return BeautifulSoup(response.text, "html.parser")
        else:
            print(f"Error al obtener {url}: {response.status_code}")
            return None
