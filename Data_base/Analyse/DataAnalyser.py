import sqlalchemy
from sqlalchemy import create_engine, or_
from sqlalchemy.orm import sessionmaker

from Data_base.tables import Competition, Competitor, Match, CategoryAtCompetitions, Club, AgeCategory, WeightCategory, \
    ClubsLicences
from copy import deepcopy
from Data_base.Analyse.DataVisualiser import one_value_per_label, two_value_per_label, tree_value_per_label, \
    six_value_per_label, plot_on_poland_regions_map, get_region_for_city


class DataAnalyser:
    session: sqlalchemy.orm.session.Session

    def __init__(self, DATABSE_URI):
        self.engine = create_engine(DATABSE_URI, pool_size=float('inf'), max_overflow=float('inf'))
        self.session = None

    """" Returns list of all competitions in given year"""

    def get_competitions_in_year(self, year):
        self.create_session()
        Competitions = self.session.query(Competition).filter(
            sqlalchemy.extract('year', Competition.start_date) == year)
        Competitions = Competitions.all()
        self.close_session()
        return set(Competitions)

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

    """" Returns list of all age categories names (str)"""

    def get_age_categories(self):
        self.create_session()
        res = self.session.query(AgeCategory.category).all()
        self.close_session()
        res = list(filter(lambda x: x != "Dziecko (u12)", [x[0] for x in res]))
        return res

    """" Returns set od competitor started in age category in year"""

    def get_competitors_started_in_age_category_in_year(self, category, year):
        self.create_session()
        res = self.session.query(Competitor) \
            .outerjoin(Match,
                       or_(Match.first_competitor == Competitor.licence_no,
                           Match.second_competitor == Competitor.licence_no)) \
            .outerjoin(CategoryAtCompetitions, CategoryAtCompetitions.category_at_competition_id == Match.category_id) \
            .outerjoin(WeightCategory, WeightCategory.category_id == CategoryAtCompetitions.category_id) \
            .filter_by(age_category=category) \
            .outerjoin(Competition, Competition.competition_id == CategoryAtCompetitions.competition_id) \
            .filter(sqlalchemy.extract('year', Competition.start_date) == year) \
            .all()
        self.close_session()
        return set(res)

    """" Returns list of weight categories sorted in ascending order"""

    def get_weight_categories_in_age_category(self, age_category):
        self.create_session()
        result = self.session.query(WeightCategory).filter_by(age_category=age_category).all()
        self.close_session()
        return sorted(result)

    def get_competitors_in_year_in_age_category_in_weight_category(self, year, age_category, weight_category):
        self.create_session()
        result = self.session.query(Competitor).outerjoin(Match, or_(Competitor.licence_no == Match.second_competitor
                                                                     , Competitor.licence_no == Match.first_competitor)) \
            .outerjoin(CategoryAtCompetitions, CategoryAtCompetitions.category_at_competition_id == Match.category_id) \
            .outerjoin(Competition, Competition.competition_id == CategoryAtCompetitions.competition_id) \
            .filter(sqlalchemy.extract('year', Competition.start_date) == year) \
            .outerjoin(WeightCategory, WeightCategory.category_id == CategoryAtCompetitions.category_id) \
            .filter_by(weight_category=weight_category.weight_category, age_category=age_category,
                       gender=weight_category.gender).distinct().all()
        self.close_session()
        return result

    def get_competitor_starts_in_year(self, competitor, year, age_category=None):
        competitor_id = competitor.licence_no
        self.create_session()
        competitions = self.session.query(Competition) \
            .outerjoin(CategoryAtCompetitions, Competition.competition_id == CategoryAtCompetitions.competition_id) \
            .outerjoin(Match, CategoryAtCompetitions.category_at_competition_id == Match.category_id) \
            .filter(Match.first_competitor == competitor_id or Match.second_competitor == competitor_id) \
            .filter(sqlalchemy.extract('year', Competition.start_date) == year).distinct()
        if age_category:
            competitions.outerjoin(WeightCategory, WeightCategory.category_id == CategoryAtCompetitions.category_id) \
                .filter_by(age_category=age_category)
        self.close_session()
        return competitions.all()

    def get_all_clubs(self):
        self.create_session()
        res = self.session.query(Club).distinct().all()
        self.close_session()
        return set(res)

    def get_competitors_of_club(self, club):
        self.create_session()
        results = self.session.query(Competitor).filter_by(club=club.club_id).distinct().all()
        self.close_session()
        return set(results)

    def get_active_clubs_in_year(self, year):
        competitors = self.get_competitors_in_year(year)
        competitors_active_in_year = self.get_competitors_in_year(year)
        result = set()
        for club in self.get_all_clubs():
            if (competitors_active_in_year & self.get_competitors_of_club(club)):
                result.add(club)
        return result

    """"Returns set of competitors from region"""

    def get_competitors_in_region(self, region):
        self.create_session()
        results = self.session.query(Competitor).outerjoin(Club, Club.club_id == Competitor.club) \
            .filter_by(province=region).distinct().all()
        self.close_session()
        return set(results)

    def get_competitors_activity_levels(self, competitors, year, age_category=None):
        def get_activity_level(competitor):
            competitor_starts = self.get_competitor_starts_in_year(competitor, year, age_category)
            if len(competitor_starts) == 1:
                return 'low active'
            elif len(competitor_starts) == 2:
                return 'active'
            else:
                return 'very active'

        result = {'low active': set(), 'active': set(), 'very active': set()}
        for competitor in competitors:
            result[get_activity_level(competitor)].add(competitor)

        return result

    """"Returns list of name of regions where exist at less one club (str)"""

    def get_regions(self):
        self.create_session()
        result = self.session.query(Club.province).distinct().all()
        self.close_session()
        return [x[0] for x in result]

    def get_clubs_with_licence_in_year(self, year):
        self.create_session()
        res = self.session.query(Club).join(ClubsLicences)\
            .filter(sqlalchemy.extract('year', ClubsLicences.date) == year).all()
        self.close_session()
        return set(res)

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

    for i in analyser.get_competitions_in_year(2017):
        if get_region_for_city(i.city) == 'Mazowieckie':
            print(i)

    # for i in range(2014, 2022):

    #     print(i, len(analyser.get_active_clubs_in_year(i)))
