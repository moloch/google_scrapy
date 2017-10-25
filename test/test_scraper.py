from unittest import mock
from unittest.mock import Mock, MagicMock
from src.scraper import Scraper


def requests_get(url):
    class Response:
        text = 'content'
    return Response()


@mock.patch('src.scraper.requests.get', requests_get)
def test_scraper_should_call_parser():
    url = "https://www.google.com"
    parser = Mock()
    parser.parse = MagicMock(return_value='foo')

    scraper = Scraper(parser)

    assert 'foo' == scraper.get_contents(url)
    parser.parse.assert_called_with('content')
