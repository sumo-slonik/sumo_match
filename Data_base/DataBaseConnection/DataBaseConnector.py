import hashlib

import sqlalchemy
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker


class DataBaseConnector:
    session: sqlalchemy.orm.session.Session

    def __init__(self, address, user, password):
        self.url = address.format(user=user, password=password,
                                  server='localhost',
                                  database='sumo_match_maker')
        self.engine = create_engine(self.url, pool_size=float('inf'), max_overflow=float('inf'))
        self.session = None

    def create_session(self):
        session_maker = sessionmaker(self.engine)
        self.session = session_maker()

    def close_session(self):
        self.session.close()

    def generate_hash(*description):
        res = ''
        for i in description:
            res += str(i)
        return int(hashlib.sha1(res.encode("utf-8")).hexdigest(), 16) % (10 ** 8)

