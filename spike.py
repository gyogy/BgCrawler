import requests
from bs4 import BeautifulSoup


site_to_crawl = 'http://register.start.bg/'
r = requests.get(site_to_crawl)
soup = BeautifulSoup(r.content)


def a_has_href(tag):
    # This function is passed to the for loop
    # so it returns all a tags that have defined a href
    if tag.name == 'a' and tag.has_attr('href'):
        return True


links = []
for tag in soup.find_all(a_has_href):
    if tag['href'].startswith('link.php?id='):
        try:
            temp = requests.get(site_to_crawl + tag['href'], timeout=1)
            links.append(temp.url)
        except Exception as e:
            links.append(e)
    else:
        links.append(tag['href'])


for link in links:
    print(link)
