from datetime import date

from Data_base.DataBaseConnection.DataBaseConnector import DataBaseConnector
from Data_base.tables import Competitor, Match, CategoryAtCompetitions, Competition, ApplicationsForCompetitions, \
    WeightCategory, AgeCategory
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

    def get_age_categories_at_competitions(self, competition):
        self.create_session()
        res = self.session.query(AgeCategory).join(WeightCategory, WeightCategory.age_category == AgeCategory.category) \
            .join(CategoryAtCompetitions, CategoryAtCompetitions.category_id == WeightCategory.category_id) \
            .join(Competition, CategoryAtCompetitions.competition_id == Competition.competition_id) \
            .filter(Competition.competition_id == competition.competition_id) \
            .all()
        self.close_session()
        return res

    def weight_categories_age_categories_at_competitions(self, gender, competition):
        self.create_session()
        self.session.query(WeightCategory).join(AgeCategory, AgeCategory.category == WeightCategory.age_category) \
            .join(CategoryAtCompetitions, CategoryAtCompetitions.category_id == WeightCategory.category_id) \
            .join(Competition, Competition.competition_id == CategoryAtCompetitions.competition_id)\
            .filter()


if __name__ == '__main__':
    geter = CompetitionsGetter('mysql+mysqlconnector://{user}:{password}@{server}/{database}', 'root', 'admin')
    competition = geter.get_competitions(date(2021, 12, 12))[0]
    for i in geter.get_age_categories_at_competitions(competition):
        print(i)
