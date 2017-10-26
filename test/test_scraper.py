from asynctest import mock, CoroutineMock, MagicMock
from src.scraper import Scraper
import pytest


def requests_get(url):
    class Response:
        text = 'content'
    return Response()


@mock.patch('src.scraper.requests.get', requests_get)
@pytest.mark.asyncio
async def test_scraper_should_call_parser():
    url = "https://www.google.com"
    parser = CoroutineMock()
    parser.parse = MagicMock(return_value='foo')

    scraper = Scraper(parser)

    assert 'foo' == await scraper.get_contents(url)
    parser.parse.assert_called_with('content')
