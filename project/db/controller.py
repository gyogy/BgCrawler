from .setup import Domain, Queue, Base, engine
from .context import session_manager


class DBController():

    def __init__(self):
        Base.metadata.create_all(engine)

    def update_domains(self, name, server, time):
        domain = Domain(name=name, server=server, recorded_at=time)
        with session_manager() as session:
            session.add(domain)

    def row_count(self, tablename):
        with session_manager() as session:
            rows = session.query(tablename).count()

        return rows

    def update_q(self, Qs):
        # import ipdb; ipdb.set_trace()
        with session_manager() as session:
            session.add_all(Qs)

    def get_q(self):
        # gets the first unmarked entry in queue table
        with session_manager() as session:
            first_unmarked = session.query(Queue).filter_by(marked=False).first()
            q = Queue(
                id=first_unmarked.id,
                url=first_unmarked.url,
                collected_at=first_unmarked.collected_at,
                marked=first_unmarked.marked
            )

            return q

    def delete_q(self, url):
        with session_manager() as session:
            q = session.query(Queue).filter_by(url=url).one()
            session.delete(q)
