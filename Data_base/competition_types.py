from Data_base.tables import CompetitionType
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker


class CompetitionTypesAdder():
    def __init__(self, DATABSE_URI):
        self.db = create_engine(DATABSE_URI)

    def add_type(self, competition_type):
        session_maker = sessionmaker(self.db)
        session = session_maker()
        new_type = CompetitionType(competition_type)
        session.merge(new_type)
        session.commit()

if __name__ == '__main__':
    DATABSE_URI = 'mysql+mysqlconnector://{user}:{password}@{server}/{database}'.format(user='root', password='admin',
                                                                                        server='localhost',
                                                                                        database='sumo_match_maker')
    competition_type_adder = CompetitionTypesAdder(DATABSE_URI)
    competition_type_adder.add_type("Mistrzostwa Polski")
    competition_type_adder.add_type("Puchar Polski")
    competition_type_adder.add_type("Turniej Sumo Dzieci")
    competition_type_adder.add_type("Miedzywojewódzkie Mistrzostwa Młodzików")
