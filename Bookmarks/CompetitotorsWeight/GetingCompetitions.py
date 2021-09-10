from Data_base.DataBaseConnection.DataBaseConnector import DataBaseConnector
from Data_base.tables import Competitor, Match, CategoryAtCompetitions, Competition, ApplicationsForCompetitions, \
    WeightCategory
from sqlalchemy import create_engine, or_


class CompetitionsGetter(DataBaseConnector):
    def __init__(self, address, user, password):
        super(CompetitionsGetter, self).__init__(address, user, password)

    def get_competitions(self, date):
        self.create_session()
        date = str(date.day) + '-' + str(date.month) + '-' + str(date.year)
        res = self.session.query(Competition).filter(Competition.start_date <= date,
                                                     Competition.end_date >= date) \
            .all()
        self.close_session()
        return res


if __name__ == '__main__':
    geter = CompetitionsGetter('mysql+mysqlconnector://{user}:{password}@{server}/{database}', 'root', 'admin')
    for i in geter.get_competitions('12-12-2021'):
        print(i)
