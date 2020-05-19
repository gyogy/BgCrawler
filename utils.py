import tldextract
import requests
from bs4 import BeautifulSoup


PREFIX = 'https://'


def request(site):
    try:
        assert site.startswith(PREFIX)
    except AssertionError:
        site = PREFIX + site

    try:
        req = requests.get(site, timeout=1)
    except Exception as e:
        print(e)
        req = None

    return req


def fully_qualified_domain_name(site):

    url = tldextract.extract(site)
    return url.fqdn


def get_domain_and_server(req):

    if req is None:
        return None
    else:
        server = req.headers['Server']
        domain = fully_qualified_domain_name(req.url)

        return (domain, server)


def a_has_href(tag):
    # This function is passed to the for loop
    # so it returns all a tags that have defined a href
    if tag.name == 'a' and tag.has_attr('href'):
        return True


def get_external_links(req):
    soup = BeautifulSoup(req.content, 'html.parser')
    ext_links = []

    if len(soup.find_all(a_has_href)) == 0:
        return ext_links

    else:
        for tag in soup.find_all(a_has_href):
            if tag['href'].startswith('link.php?id='):
                temp = req.url + tag['href']
                ext_links.append(temp)
        else:
            # import ipdb; ipdb.set_trace()
            ext_links.append(tag['href'])

    return ext_links
