import os
from src.parsers import GoogleParser


def test_google_parser():
    dir_path = os.path.dirname(os.path.realpath(__file__))
    file_path = dir_path + '/test_files/google_sample_source.html'
    with open(file_path, 'r') as file:
        file_content = ''
        for line in file:
            file_content += line

        parser = GoogleParser()

        links = parser.parse(file_content)

        assert 12 == len(links)
        assert 'https://doc.pytest.org/' == links[0]
