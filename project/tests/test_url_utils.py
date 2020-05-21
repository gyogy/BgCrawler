import unittest
from ..utils import url_normalizer, domain_normalizer

class TestUrlUtils(unittest.TestCase):

    def setUp(self):
        self.url1 = 'https://mcafee.bg'
        self.url2 = 'cs.eshop.bg/cart_view.php'
        self.url3 = '#'
        self.url4 = 'mailto:someone@yoursite.bg'

    def test_normalize_url_with_no_subdomain(self):

        result = url_normalizer(self.url1)
        expected = 'https://mcafee.bg'

        self.assertEqual(result, expected)

    def test_normalize_url_with_subdomain_and_some_resource(self):

        result = url_normalizer(self.url2)
        expected = 'https://cs.eshop.bg/cart_view.php'

        self.assertEqual(result, expected)

    def test_normalize_url_with_invalid_url(self):

        result = url_normalizer(self.url3)
        expected = 'https://#'

        self.assertEqual(result, expected)

    def test_normalize_url_from_mailto_link(self):

        result = url_normalizer(self.url4)
        expected = 'https://yoursite.bg'

        self.assertEqual(result, expected)

    def test_normalize_domain_with_no_subdomain(self):

        result = domain_normalizer(self.url1)
        expected = 'www.mcafee.bg'

        self.assertEqual(result, expected)

    def test_normalize_domain_with_subdomain_and_some_resource(self):

        result = domain_normalizer(self.url2)
        expected = 'cs.eshop.bg'

        self.assertEqual(result, expected)

    def test_normalize_domain_with_invalid_url(self):

        result = domain_normalizer(self.url3)
        expected = False

        self.assertEqual(result, expected)

    def test_normalize_domain_from_mailto_link(self):

        result = domain_normalizer(self.url4)
        expected = 'www.yoursite.bg'

        self.assertEqual(result, expected)


if __name__ == '__main__':
    unittest.main()
