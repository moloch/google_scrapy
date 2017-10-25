from bs4 import BeautifulSoup


class GoogleParser:

    def parse(self, html_doc):
        soup = BeautifulSoup(html_doc, 'html.parser')
        return [h3.find('a')['href'] for h3 in soup.findAll('h3', attrs={'class': 'r'})]
