from unittest import TestCase
from selenium.webdriver.chrome.webdriver import WebDriver

from Data_base.sport_zona_download.sport_zona_downloader import SportZonaDownloader


class TestSportZonaDownloader(TestCase):
    clubs_list_link = 'https://sportzona.pl/app/clubs/list/sumo'
    competitors_list_link = 'https://sportzona.pl/app/clubs/view/sumo/799'
    events_list_link = 'https://sportzona.pl/app/events/list/sumo'
    matches_list_link = 'https://sportzona.pl/app/events/view/sumo/3174'

    def test_get_number_of_navi_buttons_competitors(self):
        # set
        competitors_driver = WebDriver()
        competitors_driver.get(self.competitors_list_link)
        # act
        competitors_downloader = SportZonaDownloader('competitors', competitors_driver)
        competitors_navi_buttons = competitors_downloader.get_number_of_navi_buttons()
        # test
        self.assertEqual(8, competitors_navi_buttons, "Competitors list navi button counter")

    def test_get_number_of_navi_buttons_clubs(self):
        # set
        clubs_driver = WebDriver()
        clubs_driver.get(self.clubs_list_link)
        # act
        clubs_downloader = SportZonaDownloader('club', clubs_driver)
        clubs_navi_buttons = clubs_downloader.get_number_of_navi_buttons()
        # test
        self.assertEqual(clubs_navi_buttons, 15, "Clubs list navi button counter")

    def test_get_number_of_navi_buttons_events(self):
        # set
        events_driver = WebDriver()
        events_driver.get(self.events_list_link)
        # act
        events_downloader = SportZonaDownloader('event', events_driver)
        events_navi_buttons = events_downloader.get_number_of_navi_buttons()
        # test
        self.assertEqual(events_navi_buttons, 15, "Events list navi button counter")

    def test_get_number_of_navi_buttons_matches(self):
        # set
        matches_driver = WebDriver()
        matches_driver.get(self.matches_list_link)
        matches_downloader = SportZonaDownloader('match', matches_driver)
        # act
        matches_navi_buttons = matches_downloader.get_number_of_navi_buttons()
        # test
        self.assertEqual(matches_navi_buttons, 12, "Matches list navi button counter")

    def test_get_number_of_navi_buttons(self):
        self.test_get_number_of_navi_buttons_competitors()
        self.test_get_number_of_navi_buttons_clubs()
        self.test_get_number_of_navi_buttons_matches()
        self.test_get_number_of_navi_buttons_events()




    def test_get_number_of_pages(self):
        self.fail()

    def test_get_number_of_rows(self):
        self.fail()

    def test_get_number_of_all_rows(self):
        self.fail()
