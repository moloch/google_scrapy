import requests


class Scraper:
    def __init__(self, parser):
        self.parser = parser

    async def get_contents(self, url):
        content = requests.get(url)
        return self.parser.parse(content.text)
