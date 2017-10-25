import requests


class Scraper:
    def __init__(self, parser):
        self.parser = parser

    def get_contents(self, url):
        content = requests.get(url).text
        return self.parser.parse(content)
