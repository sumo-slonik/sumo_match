from time import sleep

from selenium.webdriver.chrome.webdriver import WebDriver
from sqlalchemy import create_engine

from Data_base.DataBaseConnection.DataBaseConnector import DataBaseConnector
from Data_base.sport_zona_download.sport_zona_downloader import SportZonaDownloader
from webdriver_manager.chrome import ChromeDriverManager
from selenium import webdriver

from Data_base.tables import ClubsLicences


class ClubLicenceDownloader(DataBaseConnector):
    def __init__(self, address, user, password):
        super(ClubLicenceDownloader, self).__init__(address, user, password)
        self.driverClubs = webdriver.Chrome(ChromeDriverManager().install())
        self.driverClubs.get('https://sportzona.pl/app/clubs/list/sumo')
        self.driverSingleClubs = webdriver.Chrome(ChromeDriverManager().install())
        self.allClubsDownloader = SportZonaDownloader('club', self.driverClubs)
        self.singleClubDownloader = SportZonaDownloader('competitors', self.driverSingleClubs)

    def iterate_by_clubs(self):
        clubs_downloader = self.allClubsDownloader
        single_club_downloader = self.singleClubDownloader
        pages_of_clubs = int(clubs_downloader.get_number_of_pages())
        for _ in range(pages_of_clubs):
            clubs_on_page = clubs_downloader.get_number_of_rows()
            sleep(1)
            print(clubs_on_page)
            for i in range(1, clubs_on_page):
                sleep(1)
                try:
                    if clubs_downloader.get_row_column_value(i, 3) == "POL":
                        print(clubs_downloader.get_row_column_value(i, 1))
                        club_link = clubs_downloader.get_row_link(i)
                        print(club_link)
                        single_club_downloader.go_to_link(club_link)
                        sleep(1)
                        club, licence_date = single_club_downloader.download_club_data(True)
                        print(club)
                        try:
                            self.create_session()
                            self.session.merge(club)
                            self.session.merge(ClubsLicences(club.club_id,licence_date))
                            self.session.commit()
                            self.close_session()
                        except Exception as ex:
                            print(ex)
                            print(club, " błąd dodania")
                    else:
                        print(clubs_downloader.get_row_column_value(i, 1), "not from poland")
                except Exception as ex:
                    print(ex)
            clubs_downloader.got_to_next_page()


if __name__ == '__main__':
    clubDownloader = ClubLicenceDownloader('mysql+mysqlconnector://{user}:{password}@{server}/{database}', 'root',
                                           'admin')
    clubDownloader.iterate_by_clubs()
