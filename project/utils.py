from datetime import datetime
import tldextract


URL_PREFIX = 'https://'
DOMAIN_PREFIX = 'www'


def time_string():
    time_obj = datetime.today()
    time_string = time_obj.isoformat(sep=' ', timespec='microseconds')
    return time_string


def time_obj_from_string(time_string):
    time_obj = datetime.strptime(time_string, '%Y-%m-%d %H:%M:%S.%f')
    return time_obj


def url_normalizer(url):

    if url.startswith('http://'):
        pass

    elif url.startswith('mailto:'):
        tld = tldextract.extract(url)
        url = URL_PREFIX + tld.fqdn

    elif not url.startswith(URL_PREFIX):
        url = URL_PREFIX + url

    return url


def domain_normalizer(url):
    tld = tldextract.extract(url)

    if tld.suffix == '':
        print(f'{url} is a malformed URL. Moving along.')
        return False

    elif tld.suffix != 'bg':
        print(f'{tld.fqdn} is not a Bulgarian domain.')
        return False

    elif tld.subdomain == '':
        domain = '.'.join([DOMAIN_PREFIX, tld.domain, tld.suffix])
    else:
        domain = '.'.join([tld.subdomain, tld.domain, tld.suffix])

    if domain == 'www..':
        return False
    else:
        return domain


def a_has_href(tag):
    # This function is passed to the for loop
    # so it returns all a tags that have defined a href
    if tag.name == 'a' and tag.has_attr('href'):
        return True
