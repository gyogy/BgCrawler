from sqlalchemy.exc import IntegrityError
from contextlib import contextmanager
from .setup import Session


@contextmanager
def session_manager():

    session = Session()
    try:
        yield session
        session.commit()

    except IntegrityError:
        print('Link already added.')

    except Exception:
        session.rollback()
        raise

    finally:
        session.close()
