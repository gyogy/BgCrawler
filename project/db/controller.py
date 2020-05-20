# from sqlalchemy import func
from .setup import Domain, Queue, Base, engine
from .context import session_manager


class DBController():

    def __init__(self):
        Base.metadata.create_all(engine)

    def update_domains(self, name, server, time):
        domain = Domain(name=name, server=server, recorded_at=time)
        with session_manager as session:
            session.add(domain)

    def q_count(self):
        with session_manager() as session:
            rows = session.query(Queue).count()

        return rows

    def update_q(self, url, time, marked=False):
        q = Queue(url=url, collected_at=time, marked=marked)
        with session_manager() as session:
            session.add(q)

    # def get_q(self):
    #     # gets the first unmarked entry in queue table
    #     with session_manager() as session:
    #         query = session.query(Queue).filter_by(marked=False)
    #         q = query.first()
    #         print(q)

    #     return q

    def delete_q(self, url):
        with session_manager() as session:
            q = session.query(Queue).filter_by(url=url).one()
            session.delete(q)
