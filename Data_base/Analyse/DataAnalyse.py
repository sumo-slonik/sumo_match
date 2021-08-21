import sqlalchemy
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from Data_base.tables import Competition, Competitor, Match, CategoryAtCompetitions, Club


class DataAnalyser:
    session: sqlalchemy.orm.session.Session

    def __init__(self, DATABSE_URI):
        self.engine = create_engine(DATABSE_URI)
        self.session = None

    """" Returns list of all competitions in given year"""

    def get_competitions_in_year(self, year):
        self.create_session()
        Competitions = self.session.query(Competition).filter(
            sqlalchemy.extract('year', Competition.start_date) == year)
        Competitions = Competitions.all()
        self.close_session()
        return Competitions

    """" Returns set of competitors who have at less one fight in given year"""

    def get_competitors_in_year(self, year):
        match: Match
        competitor: Competitor
        self.create_session()
        matches_in_year = self.session.query(Match) \
            .outerjoin(CategoryAtCompetitions, Match.category_id == CategoryAtCompetitions.category_at_competition_id) \
            .outerjoin(Competition, CategoryAtCompetitions.competition_id == Competition.competition_id) \
            .filter(sqlalchemy.extract('year', Competition.start_date) == year).all()
        competitors_ids = {match.first_competitor for match in matches_in_year} | {match.second_competitor for match in
                                                                                   matches_in_year}
        competitors = self.session.query(Competitor).all()
        competitors = set(filter(lambda competitor: competitor.licence_no in competitors_ids, competitors))
        self.close_session()
        return competitors

    """" Returns list of all regions (strings with region name) that contain at less one club """

    def get_all_regions(self):
        self.create_session()
        result = self.session.query(Club.province).distinct().all()
        self.close_session()
        return [x[0] for x in result]

    """" Returns dictionary where key = REGION, and value = list of Clubs (Clubs obj)"""

    def get_clubs_in_regions(self):
        regions = self.get_all_regions()
        self.create_session()
        result = {region: self.session.query(Club).filter_by(province=region).all() for region in regions}
        self.close_session()
        return result

    def get_competitor_starts(self, competitior):
        competitor_id = competitior.licence_no
        self.create_session()
        competitions = self.session.query(Competition) \
            .outerjoin(CategoryAtCompetitions, Competition.competition_id == CategoryAtCompetitions.competition_id) \
            .outerjoin(Match, CategoryAtCompetitions.category_at_competition_id == Match.category_id) \
            .filter(Match.first_competitor == competitor_id or Match.second_competitor == competitor_id) \
            .distinct().all()
        self.close_session()
        return competitions

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
    res = analyser.get_competitor_starts(1500010)
    print(type(res))
    for i in res:
        print(i)
