from asynctest import mock, Mock, MagicMock
from src.scraper import Scraper
import pytest
import requests


@mock.patch('src.scraper.requests.get', new=MagicMock(return_value=type('', (object, ), {'text': 'content'})()))
@pytest.mark.asyncio
async def test_scraper_should_call_parser():
    url = "https://www.google.com"
    parser = Mock()
    parser.parse = MagicMock(return_value='foo')

    scraper = Scraper(parser)

    assert 'foo' == await scraper.get_contents(url)
    requests.get.assert_called_with(url)
