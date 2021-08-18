from time import sleep

from selenium.common.exceptions import ElementNotInteractableException
from selenium.webdriver.chrome.webdriver import WebDriver

from Data_base.age_categories import AgeCategoriesUpdater
from Data_base.sport_zona_download.sport_zona_downloader import SportZonaDownloader
from Data_base.tables import Competition, Match, Competitor, CategoryAtCompetitions
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
import hashlib

from Data_base.weight_categories import generate_id


class CompetitionDownloader:
    def __init__(self, DATABSE_URI):
        self.db = create_engine(DATABSE_URI)
        self.driver = WebDriver()
        self.gender = ''
        self.age = ''
        self.competition_id = 1
        self.city = None
        self.start_date = None
        self.end_date = None
        self.country = None
        self.competition_name = None
        self.competition_type = None
        self.match_no = 0
        self.ageCategoriesUpdater = AgeCategoriesUpdater()
        self.close_counter = 5
        self.skip_counter = 0

    def generate_id(self):
        description = self.competition_name + self.start_date + self.end_date + self.competition_type + self.city
        self.competition_id = int(hashlib.sha1((description).encode("utf-8")).hexdigest(), 16) % (10 ** 8)

    def download_competitions(self):
        self.competition_name = \
            self.driver.find_elements_by_xpath(
                '//*[@id="top"]/article/div/div[2]/div/div[2]/div/div[1]/div[1]/div[1]/h1')[
                0].text
        description = self.driver.find_elements_by_xpath('//*[@id="event-description"]/strong[6]')[
            0].text.split(',')
        self.city = description[0]
        description = description[1].split(' ')[1:]
        self.country = description[0]
        self.start_date = description[1][:10]
        self.end_date = description[1][11:]
        description = self.driver.find_elements_by_xpath(
            '//*[@id="event-description"]/strong[5]')[
            0].text.split(',')
        self.gender = description[0]
        self.age = description[1][1:]
        print('name:', self.competition_name)
        print('city:', self.city)
        print('gender:', self.gender)
        print('age:', self.age)
        print('country:', self.country)
        print('start:', self.start_date)
        print('end:', self.end_date)
        self.competition_type = ''
        if 'Mistrzostwa Polski' in self.competition_name:
            self.competition_type = 'Mistrzostwa Polski'
        elif 'Międzywojewódzkie' in self.competition_name:
            self.competition_type = 'Miedzywojewódzkie Mistrzostwa Młodzików'
        elif 'Puchar Polski' in self.competition_name:
            self.competition_type = 'Puchar Polski'
        print('competition_type:', self.competition_type)
        self.generate_id()
        new_competition = Competition(self.competition_name, self.city, self.start_date, self.end_date,
                                      self.competition_type,
                                      self.competition_id)
        session_maker = sessionmaker(self.db)
        session = session_maker()
        session.merge(new_competition)
        session.commit()
        session.close()
        return new_competition

    def iterate_by_competition(self):
        iterator_driver = WebDriver()
        iterator_driver.get('https://sportzona.pl/app/events/list/sumo')
        competitions_iterator = SportZonaDownloader('event', iterator_driver)
        self.driver.close()
        self.driver = WebDriver()
        first_time = True

        for pages in range(competitions_iterator.get_number_of_pages()):
            for row in range(1, competitions_iterator.get_number_of_all_rows()):
                if first_time:
                    for _ in range(29):
                        competitions_iterator.got_to_next_page()
                    sleep(0.5)
                    first_time = False
                if self.skip_counter == 0:
                    try:
                        competitions_link = competitions_iterator.get_row_column_link(row, 1)
                        print(competitions_link)
                        self.driver.get(competitions_link)
                        new_competitions = self.download_competitions()
                        if 'Międzywojewódzkie' in new_competitions.competition_name:
                            self.download_matches()
                    except Exception as ex:
                        print(ex)
                else:
                    self.skip_counter -= 1
            competitions_iterator.got_to_next_page()
        self.driver.close()

    def update_gender(self, competitor, gender):
        print(competitor)
        session_maker = sessionmaker(self.db)
        session = session_maker()
        competitor.gender = gender
        session.query(Competitor).where(Competitor.licence_no == competitor.licence_no).update({'gender': gender})
        session.commit()

    def download_matches(self):
        self.generate_id()
        competitor_1_link = ''
        competitor_2_link = ''
        sport_zona_downloader = SportZonaDownloader('match', self.driver)
        competitor_1_driver = WebDriver()
        competitor_2_driver = WebDriver()
        for page in range(sport_zona_downloader.get_number_of_pages()):
            for row in range(1, sport_zona_downloader.get_number_of_all_rows() - 1):
                if sport_zona_downloader.check_row(row):
                    try:
                        fight_round = sport_zona_downloader.get_row_column_value(row, 2)
                        competitor_1_link = sport_zona_downloader.get_row_column_link(row, 3)
                        competitor_2_link = sport_zona_downloader.get_row_column_link(row, 10)
                        first_win = sport_zona_downloader.get_row_winner(row)
                        self.gender = self.gender.lower()
                        self.age = self.ageCategoriesUpdater.get_age_categories(self.age)
                        category = sport_zona_downloader.get_row_column_value(row, 1).lower()
                        category = category.replace('kg', '')
                        category = category.replace(' ', '')
                        category_id = generate_id(category, self.age,
                                                  self.gender)
                        category_at_competition_id = generate_id(
                            sport_zona_downloader.get_row_column_value(row, 1).lower(),
                            str(category_id),
                            self.competition_name)
                        category_at_competition = CategoryAtCompetitions(category_id, self.competition_id,
                                                                         category_at_competition_id)
                        print(fight_round, self.competition_name, self.gender, self.age, category)
                        print(competitor_1_link, competitor_2_link, first_win, category_id)
                        competitor_1_driver.get(competitor_1_link)
                        competitor_2_driver.get(competitor_2_link)

                        competitor_1_downloader = SportZonaDownloader('competitors', competitor_1_driver)
                        competitor_2_downloader = SportZonaDownloader('competitors', competitor_2_driver)

                        competitor_1 = competitor_1_downloader.download_competitor_data()
                        competitor_2 = competitor_2_downloader.download_competitor_data()
                        # self.update_gender(competitor_1, self.gender)
                        # self.update_gender(competitor_2, self.gender)
                        winner = competitor_1 if first_win else competitor_2
                        new_match = Match(competitor_1.licence_no, competitor_2.licence_no, category_at_competition_id,
                                          winner.licence_no,
                                          generate_id(str(competitor_1.licence_no), str(competitor_2.licence_no),
                                                      str(self.match_no)), fight_round)
                        self.match_no += 1

                        session_maker = sessionmaker(self.db)
                        session = session_maker()
                        session.merge(category_at_competition)
                        session.merge(new_match)
                        session.commit()
                        session.close()
                    except Exception as ex:
                        print(ex)
            sport_zona_downloader.got_to_next_page()
            if self.close_counter == 0:
                self.close_counter = 5
                competitor_1_driver.close()
                competitor_2_driver.close()
                competitor_1_driver = WebDriver()
                competitor_2_driver = WebDriver()
            else:
                self.close_counter -= 1


if __name__ == '__main__':
    DATABSE_URI = 'mysql+mysqlconnector://{user}:{password}@{server}/{database}'.format(user='root', password='admin',
                                                                                        server='localhost',
                                                                                        database='sumo_match_maker')
    downloader = CompetitionDownloader(DATABSE_URI)
    #
    # # session_maker = sessionmaker(downloader.db)
    # # session = session_maker()
    # # category_at_competition = CategoryAtCompetitions(788791, 990308, 1)
    # # session.merge(category_at_competition)
    # # session.commit()
    # # session.close()
    downloader.iterate_by_competition()
