from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, Boolean
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

Base = declarative_base()
engine = create_engine('sqlite:///domains.db', echo=True)
Session = sessionmaker(bind=engine)


class Domain(Base):
    __tablename__ = 'domains'
    id = Column(Integer, primary_key=True)
    name = Column(String, unique=True)
    server = Column(String)
    recorded_at = Column(String)  # VARCHAR(10) from datetime object


class Queue(Base):
    __tablename__ = 'queue'
    id = Column(Integer, primary_key=True)
    url = Column(String, unique=False)
    collected_at = Column(String)  # VARCHAR(10) from datetime object
    marked = Column(Boolean)

    def __repr__(self):
        return f'Queue({self.id}, {self.url}, {self.collected_at}, {self.marked})'
