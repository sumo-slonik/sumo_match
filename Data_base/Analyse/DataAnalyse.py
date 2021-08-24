import sqlalchemy
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from Data_base.tables import Competition, Competitor, Match, CategoryAtCompetitions, Club, AgeCategory, WeightCategory
from copy import deepcopy
from Data_base.Analyse.DataVisualiser import one_value_per_label


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

    """" Returns list of all age categories names (str)"""

    def get_age_categories(self):
        self.create_session()
        res = self.session.query(AgeCategory.category).all()
        self.close_session()
        return [x[0] for x in res]

    def get_competitors_started_in_age_category_in_year(self, category, year):
        self.create_session()
        res = self.session.query(Competitor) \
            .outerjoin(Match,
                       Match.first_competitor == Competitor.licence_no or Match.second_competitor == Competitor.licence_no) \
            .outerjoin(CategoryAtCompetitions, CategoryAtCompetitions.category_at_competition_id == Match.category_id) \
            .outerjoin(WeightCategory, WeightCategory.category_id == CategoryAtCompetitions.category_id) \
            .filter_by(age_category=category) \
            .outerjoin(Competition, Competition.competition_id == CategoryAtCompetitions.competition_id) \
            .filter(sqlalchemy.extract('year', Competition.start_date) == year) \
            .all()
        self.close_session()
        return set(res)

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
                .filterby(age_category=age_category)
        self.close_session()
        return competitions.all()

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

    def create_session(self):
        session_maker = sessionmaker(self.engine)
        self.session = session_maker()

    def close_session(self):
        self.session.close()


def separate_genders(competitors: {Competitor}):
    result = {'Man': set(), 'Woman': set()}
    for competitor in competitors:
        result[competitor.gender].add(competitor)
    return result


if __name__ == '__main__':
    DATABSE_URI = 'mysql+mysqlconnector://{user}:{password}@{server}/{database}'.format(user='root', password='admin',
                                                                                        server='localhost',
                                                                                        database='sumo_match_maker')
    analyser = DataAnalyser(DATABSE_URI)
    # dicts to collect data

    # set of all competitors
    competitors_all = dict()
    # dict key = gender value = set of competitors
    competitors_in_genders = dict()
    # dict key = year value = set of active competitors in year
    competitors_active_in_years = dict()
    # dict key = year value = set of new competitors in year
    competitors_new_in_years = dict()
    # dict key = region value = set of competitors
    competitors_in_regions = dict()
    # dict key = year value = dict where key = age category value = set of competitors
    competitors_in_age_categories_in_years = dict()

    # Getting active competitors in years
    for year in range(2014, 2022):
        competitors_active_in_years[year] = analyser.get_competitors_in_year(year)

    print('active competitors in each years:')
    for year in competitors_active_in_years:
        print(year, len(competitors_active_in_years[year]))

    one_value_per_label("Aktywni zawodnicy w latach 2014-2021",
                        "Liczba aktywnych zawodników",
                        competitors_active_in_years.keys(),
                        [len(competitors_active_in_years[x]) for x in competitors_active_in_years])

    for age_category in analyser.get_age_categories():
        for year in competitors_active_in_years:
            competitors = analyser.get_competitors_started_in_age_category_in_year(age_category, year)
            dict_of_competitors = competitors_in_age_categories_in_years.get(year, dict())
            new_dict = {age_category: deepcopy(competitors)}
            dict_of_competitors.update(new_dict)
            competitors_in_age_categories_in_years[year] = dict_of_competitors
    print('__________________________________________________________________')
    print('active competitors in age categories')
    for age_category in competitors_in_age_categories_in_years:
        for year in competitors_in_age_categories_in_years[age_category]:
            print(age_category, year, len(competitors_in_age_categories_in_years[age_category][year]))

    for region in analyser.get_regions():
        competitors_in_regions[region] = analyser.get_competitors_in_region(region)
    print('__________________________________________________________________')
    print('competitors in regions')
    for region in competitors_in_regions:
        print(region, len(competitors_in_regions[region]))

    used = set()
    for year in competitors_active_in_years:
        competitors_new_in_years[year] = competitors_active_in_years[year] - used
        used = used | competitors_active_in_years[year]

    print('__________________________________________________________________')
    print('new competitors in years')
    for year in competitors_new_in_years:
        print(year, len(competitors_new_in_years[year]))

    print('__________________________________________________________________')
    print('new competitors in years in age categories')
    for year in competitors_new_in_years:
        for age_category in competitors_in_age_categories_in_years[year]:
            print(year,age_category, len(competitors_new_in_years[year] & competitors_in_age_categories_in_years[year][age_category]))





    # print('activity levels of competitors')
    # for year in competitors_active_in_years:
    #     print(year, ':')
    #     activity_lvl = analyser.get_competitors_activity_levels(competitors_active_in_years[year], year)
    #     for activity in activity_lvl:
    #         print(activity, len(activity_lvl[activity]))
    #         separated_genders = separate_genders(activity_lvl[activity])
    #         for gender in separated_genders:
    #             print(gender, len(separated_genders[gender]))

    #
    # print('activity levels of competitors in age categories')
    # for age_category in analyser.get_age_categories():
    #     print(age_category)
    #     for year in competitors_active_in_years:
    #         print(year, ':')
    #         competitors = analyser.get_competitors_started_in_age_category_in_year(age_category, year)
    #         activity_lvl = analyser.get_competitors_activity_levels(competitors, year)
    #         for activity in activity_lvl:
    #             print(activity, len(activity_lvl[activity]))
    #             separated_genders = separate_genders(activity_lvl[activity])
    #             for gender in separated_genders:
    #                 print(gender, len(separated_genders[gender]))

    # for region in analyser.get_regions():
    #     print(region)
    #     for year in range(2014, 2022):
    #         print(year)
    #         print(len(competitors_active_in_years[year] & analyser.get_competitors_in_region(region)))
    #
    # used = set()
    # new_competitor = {year: {} for year in range(2014, 2022)}
    # for year in range(2014, 2022):
    #     new_competitor[year] = competitors_active_in_years[year] - used
    #     print(year, len(new_competitor[year]))
    #     used = used | competitors_active_in_years[year]
