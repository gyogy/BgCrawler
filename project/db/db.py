from sqlalchemy.exc import IntegrityError
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from contextlib import contextmanager

Base = declarative_base()
engine = create_engine('sqlite:///domains.db', echo=False)
Session = sessionmaker(bind=engine)


@contextmanager
def session_cm(domain=None):
    session = Session()
    try:
        yield session
        session.commit()
    except IntegrityError:
        session.rollback()
        print(f'{domain} already in records.')
    except Exception:
        session.rollback()
        raise
    finally:
        session.close()


class Site(Base):
    __tablename__ = 'sites'
    id = Column(Integer, primary_key=True)
    site = Column(String, unique=True)
    server = Column(String)


def update_sites_table(dom_serv_tuple):
    domain = dom_serv_tuple[0]
    server = dom_serv_tuple[1]
    site = Site(site=domain, server=server)

    if domain.endswith('.bg'):

        with session_cm(domain) as session:
            session.add(site)

        return True

    else:

        print(f'Didn\'t add {domain}. It is not a .bg domain.')

        return False


class Queue(Base):
    __tablename__ = 'queue'
    id = Column(Integer, primary_key=True)
    site = Column(String, unique=True)


def update_queue_table(ext_links):

    for domain in ext_links:
        print(domain)
        entry = Queue(site=domain)

        with session_cm(domain) as session:
            session.add(entry)


def get_queue_count():
    with session_cm() as session:
        rows = session.query(Queue).count()

    return rows


def select_and_delete_first_from_queue():
    with session_cm() as session:
        first_record = session.query(Queue).first()

        ajdi = first_record.id
        url = first_record.site

        session.query(Queue).filter(Queue.id == ajdi).delete(synchronize_session=False)

    return url
