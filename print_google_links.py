import sys
import asyncio

from src.scraper import Scraper
from src.parsers import GoogleParser


def main():
    google_parser = GoogleParser()
    scraper = Scraper(google_parser)
    loop = asyncio.get_event_loop()
    links = loop.run_until_complete(scraper.get_contents(sys.argv[1]))
    loop.close()
    for link in links:
        print(link)


if __name__ == '__main__':
    main()
