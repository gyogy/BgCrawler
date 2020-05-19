import sys
from project.db.db import (
    Site, Queue, Base,
    engine, Session, session_cm,
    update_sites_table,
    update_queue_table,
    select_and_delete_first_from_queue,
    get_queue_count
)
from utils import (
    request,
    get_domain_and_server,
    get_external_links
)

Base.metadata.create_all(engine)


def check_site(site):
    req = request(site)
    dom_serv_tuple = get_domain_and_server(req)
    print(dom_serv_tuple)

    if dom_serv_tuple is None:
        pass

    elif update_sites_table(dom_serv_tuple):
        print('Getting external links.')
        ext_links = get_external_links(req)

        if ext_links:
            print('Adding links to queue')
            update_queue_table(ext_links)


def process_queue():
    while True:
        rows = get_queue_count()
        print(f'{rows} links in queue')
        if rows == 0:
            break
        else:
            site = select_and_delete_first_from_queue()
            check_site(site)


if __name__ == '__main__':
    choice = sys.argv[1]

    if choice == 'queue':
        process_queue()
    else:
        check_site(choice)
