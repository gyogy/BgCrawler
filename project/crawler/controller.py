import requests
from bs4 import BeautifulSoup
from ..utils import *


class Crawler():

    def __init__(self, site):

        url = url_normalizer(site)
        try:
            r = requests.get(url)
            if '404' in str(r):
                self.response = None
            else:
                self.response = r
        except Exception:
            self.response = None

    def get_domain(self):
        domain = domain_normalizer(self.response.url)
        return domain

    def get_server(self):
        try:
            server = self.response.headers['Server']

        except KeyError:
            server = 'N/A'

        return server

    def get_time(self):
        return time_string()

    def get_external_links(self):
        soup = BeautifulSoup(self.response.content, 'html.parser')
        ext_links = []

        if len(soup.find_all(a_has_href)) == 0:
            return ext_links

        for tag in soup.find_all(a_has_href):
            if tag['href'].startswith('link.php?id='):
                temp = self.response.url + tag['href']
                ext_links.append(url_normalizer(temp))
                ext_links.append(time_string())
            else:
                # import ipdb; ipdb.set_trace()
                ext_links.append(url_normalizer(tag['href']))
                ext_links.append(time_string())
        return ext_links
