from sqlite3 import IntegrityError
from time import sleep

import mysql
from selenium.common.exceptions import ElementNotInteractableException
from Data_base.sport_zona_download.sport_zona_downloader import SportZonaDownloader
from selenium.webdriver.chrome.webdriver import WebDriver
from Data_base.tables import Club
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

if __name__ == '__main__':
    DATABSE_URI = 'mysql+mysqlconnector://{user}:{password}@{server}/{database}'.format(user='root', password='admin',
                                                                                        server='localhost',
                                                                                        database='sumo_match_maker')
    db = create_engine(DATABSE_URI)
    print(db.table_names())
    connection = db.connect()
    ses = sessionmaker(db)
    session_clubs = ses()
    session_competitors = ses()

    # clubs_driver = WebDriver()
    # competitors_driver = WebDriver()
    single_competitor_driver = WebDriver()
    # clubs_driver.get('https://sportzona.pl/app/clubs/list/sumo')
    #
    # club_downloader = SportZonaDownloader('club', clubs_driver)
    # competitor_downloader = SportZonaDownloader('competitors', competitors_driver)
    # single_competitor_downloader = SportZonaDownloader('competitors', single_competitor_driver)
    #
    # pages_of_clubs = int(club_downloader.get_number_of_pages())
    # for _ in range(pages_of_clubs):
    #     clubs_on_page = club_downloader.get_number_of_rows()
    #     sleep(1)
    #     for i in range(1, clubs_on_page):
    #         sleep(1)
    #         try:
    #             if club_downloader.get_row_column_value(i, 3) == "POL":
    #                 print(club_downloader.get_row_column_value(i, 1))
    #                 club_link = club_downloader.get_row_link(i)
    #                 competitor_downloader.go_to_link(club_link)
    #                 sleep(1)
    #                 club = competitor_downloader.download_club_data()
    #                 print(club)
    #                 try:
    #                     session_clubs.add(club)
    #                     session_clubs.commit()
    #                 except Exception as ex:
    #                     session_clubs.rollback()
    #                     print(ex)
    #                     print(club, " błąd dodania")
    #                 pages_of_competitors = competitor_downloader.get_number_of_pages()
    #                 for p in range(pages_of_competitors):
    #                     sleep(1)
    #                     competitors_on_page = competitor_downloader.get_number_of_rows()
    #                     for i in range(1, competitors_on_page - 1):
    #                         link = competitor_downloader.get_row_link(i)
    #                         try:
    #                             single_competitor_downloader.go_to_link(link)
    #                             sleep(1)
    #                             competitor = single_competitor_downloader.download_competitor_data(club.club_id)
    #                             try:
    #                                 session_competitors.add(competitor)
    #                                 session_competitors.commit()
    #                                 # print(competitor, "błąd dodania")
    #                             except Exception  as e:
    #                                 print(e)
    #                                 session_competitors.rollback()
    #                                 print(competitor,"błąd dodania")
    #                             print(competitor)
    #                         except Exception as ex:
    #                             print(ex)
    #                     if p < (pages_of_competitors - 1):
    #                         competitor_downloader.got_to_next_page()
    #             else:
    #                 print(club_downloader.get_row_column_value(i, 1), "not from poland")
    #         except Exception as ex:
    #             print(ex)
    #     club_downloader.got_to_next_page()
    #
single_competitor_downloader = SportZonaDownloader('competitors', single_competitor_driver)
single_competitor_downloader.go_to_link('https://sportzona.pl/app/players/view/sumo/22259')
competitor = single_competitor_downloader.download_competitor_data(1500021)
session_competitors.add(competitor)
session_competitors.commit()
session_competitors.close()