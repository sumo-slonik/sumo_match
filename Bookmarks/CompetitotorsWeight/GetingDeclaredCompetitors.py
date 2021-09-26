from Data_base.DataBaseConnection.DataBaseConnector import DataBaseConnector
from Data_base.tables import Competitor, Match, CategoryAtCompetitions, Competition, ApplicationsForCompetitions, \
    WeightCategory
from sqlalchemy import create_engine, or_


class DeclaredCompetitorsGetter(DataBaseConnector):
    def __init__(self, address, user, password):
        super(DeclaredCompetitorsGetter, self).__init__(address, user, password)

    def get_declared_competitors(self, competition):
        self.create_session()
        res = self.session.query(Competitor).join(ApplicationsForCompetitions,
                                                  ApplicationsForCompetitions.competitor == Competitor.licence_no) \
            .join(CategoryAtCompetitions,
                  CategoryAtCompetitions.category_at_competition_id == ApplicationsForCompetitions.category_at_competition) \
            .join(Competition, Competition.competition_id == CategoryAtCompetitions.competition_id) \
            .filter_by(competition_id=competition.competition_id) \
            .all()
        self.close_session()
        return res

    def get_competitor_categories(self, competitor, competition):
        self.create_session()
        res = self.session.query(WeightCategory).join(CategoryAtCompetitions,
                                                      CategoryAtCompetitions.category_id == WeightCategory.category_id) \
            .join(Competition, Competition.competition_id == CategoryAtCompetitions.competition_id) \
            .filter_by(competition_id=competition.competition_id) \
            .join(ApplicationsForCompetitions,
                  ApplicationsForCompetitions.category_at_competition == CategoryAtCompetitions.category_at_competition_id) \
            .join(Competitor, Competitor.licence_no == ApplicationsForCompetitions.competitor) \
            .filter_by(licence_no=competitor.licence_no).all()
        self.close_session()
        return res


class ApplicationForCompetitorGetter(DataBaseConnector):

    def __init__(self, address, user, password):
        super(ApplicationForCompetitorGetter, self).__init__(address, user, password)

    def get_categories_for_competitor(self, competitor):
        self.create_session()
        result = self.session.query(WeightCategory).join(CategoryAtCompetitions,
                                                         CategoryAtCompetitions.category_id == WeightCategory.category_id) \
            .join(ApplicationsForCompetitions,
                  ApplicationsForCompetitions.category_at_competition == CategoryAtCompetitions.category_at_competition_id) \
            .filter(ApplicationsForCompetitions.competitor == competitor.licence_no) \
            .all()
        self.close_session()
        return result


if __name__ == '__main__':
    pass
