import sqlalchemy
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from Data_base.tables import Competition


class DataAnalyser:
    session: sqlalchemy.orm.session.Session

    def __init__(self, DATABSE_URI):
        self.engine = create_engine(DATABSE_URI)
        self.session = None

    def get_competitions_in_year(self, year):
        self.create_session()
        Competitions = self.session.query(Competition)
        Competitions = Competitions.all()
        self.close_session()
        return Competitions

    def create_session(self):
        session_maker = sessionmaker(self.engine)
        self.session = session_maker()

    def close_session(self):
        self.session.close()


if __name__ == '__main__':
    DATABSE_URI = 'mysql+mysqlconnector://{user}:{password}@{server}/{database}'.format(user='root', password='admin',
                                                                                        server='localhost',
                                                                       database='sumo_match_maker')
    analyser = DataAnalyser(DATABSE_URI)
    for i in analyser.get_competitions_in_year(2019):
        print(i.end_date)
