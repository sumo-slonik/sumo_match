from selenium.common.exceptions import ElementNotInteractableException
from selenium.webdriver.chrome.webdriver import WebDriver
from Data_base.tables import Competition
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
import hashlib


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

    def generate_id(self):
        description = self.competition_name + self.start_date + self.end_date + self.competition_type + self.city
        self.competition_id = int(hashlib.sha1((description).encode("utf-8")).hexdigest(), 16) % (10 ** 8)

    def download_competitions(self, link):
        self.driver.get(link)
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
        elif 'Miedzywojewódzkie Mistrzostwa Młodzików' in self.competition_name:
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


if __name__ == '__main__':
    DATABSE_URI = 'mysql+mysqlconnector://{user}:{password}@{server}/{database}'.format(user='root', password='admin',
                                                                                        server='localhost',
                                                                                        database='sumo_match_maker')
    downloader = CompetitionDownloader(DATABSE_URI)
    downloader.download_competitions('https://sportzona.pl/app/events/view/sumo/3174')
