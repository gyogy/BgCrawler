import unittest
from..controller import Crawler


class TestCrawlerController(unittest.TestCase):

    def setUp(self):
        self.c_valid = Crawler('https://www.abv.bg')
        self.c_404 = Crawler('https://en.wikipedia.org/krava')
        self.c_invalid = Crawler('https://www.asdg.fg/')

    def test_crawler_init_with_valid_site(self):

        result = self.c_valid.response.url
        expected = 'https://www.abv.bg/'

        self.assertEqual(result, expected)

    def test_crawler_init_with_invalid_site(self):

        result = self.c_invalid.response
        expected = None

        self.assertEqual(result, expected)

    def test_crawler_init_with_404_site(self):

        result = self.c_404.response
        expected = None

        self.assertEqual(result, expected)

    def test_get_server_of_valid_site(self):

        result = self.c_valid.get_server()
        expected = 'nginx'

        self.assertEqual(result, expected)


if __name__ == '__main__':
    unittest.main()
