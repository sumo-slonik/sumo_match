import random

from Data_base.Analyse.DataAnalyser import DataAnalyser
from Data_base.DataBaseConnection.DataBaseConnector import DataBaseConnector
from Data_base.tables import ApplicationsForCompetitions, Competition, CategoryAtCompetitions


class DeclarationAdder(DataBaseConnector):
    def __init__(self, address, user, password):
        super(DeclarationAdder, self).__init__(address, user, password)

    def add_competitor_declaration(self, competitor, categoryAtCompetitions):
        self.create_session()
        new_declaration = ApplicationsForCompetitions(competitor.licence_no,
                                                      categoryAtCompetitions,
                                                      self.generate_hash(competitor.licence_no,
                                                                         categoryAtCompetitions))

        self.session.add(new_declaration)
        self.session.commit()
        self.close_session()

    def add_competition(self, competition_name, city, start_date, end_date, competition_type):
        self.create_session()
        competition_id = self.generate_hash(competition_name, city, start_date, end_date, competition_type)
        new_competition = Competition(competition_name, city, start_date, end_date, competition_type, competition_id)
        self.session.add(new_competition)
        self.session.commit()
        self.close_session()

    def add_category_at_competition(self, category_id, competition_id):
        self.create_session()
        category_at_competition_id = self.generate_hash(category_id, competition_id)
        new_category_at_competition = CategoryAtCompetitions(category_id, competition_id, category_at_competition_id)
        self.session.add(new_category_at_competition)
        self.session.commit()
        self.close_session()


if __name__ == '__main__':
    data_adder = DeclarationAdder('mysql+mysqlconnector://{user}:{password}@{server}/{database}', 'root', 'admin')
    data_getter = DataAnalyser(
        'mysql+mysqlconnector://{user}:{password}@{server}/{database}'.format(user='root', password='admin',
                                                                              server='localhost',
                                                                              database='sumo_match_maker'))

    competitors = data_getter.get_competitors_in_year(2020)

    categories = [1139907,
                  2569929,
                  3670053,
                  5869828,
                  6159943]
    categories_at_competitions = []

    for category in categories:
        data_adder.add_category_at_competition(category, 2215)
        categories_at_competitions.append(data_adder.generate_hash(category, 2215))

    for _ in range(80):
        data_adder.add_competitor_declaration(random.choice(list(competitors)), random.choice(categories_at_competitions))
