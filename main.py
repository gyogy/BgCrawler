import sys
from project.db.controller import DBController
from project.crawler.controller import Crawler
from project.db.setup import Domain, Queue, Base, engine
from project.utils import *


def add_site_to_domains(crawler):
    name = crawler.get_domain()
    server = crawler.get_server()
    time = crawler.get_time()
    print(f'Adding {name} to Domains table')
    dbc.update_domains(name=name, server=server, time=time)


def add_ext_links_to_queue(crawler):
    ext_links = crawler.get_external_links()
    Qs = []

    if not ext_links:
        print(f'No external links found on {crawler.response.url}')
    else:
        urls = ext_links[::2]
        times = ext_links[1::2]

        for url, time in zip(urls, times):
            Qs.append((Queue(url=url, collected_at=time, marked=False)))
        dbc.update_q(Qs)


if __name__ == '__main__':

    Base.metadata.create_all(engine)
    choice = sys.argv[1]
    if choice.lower() == 'queue':
        pass
    else:
        url = url_normalizer(choice)
        dbc = DBController()
        c = Crawler(url)

        if c.response is not None:
            add_site_to_domains(c)
            add_ext_links_to_queue(c)
        else:
            pass

        # for link in elinks:
        #     print(link)
        #     q = Queue(url=link, collected_at='12:00', marked=False)
        #     dbc.update_q(q)
