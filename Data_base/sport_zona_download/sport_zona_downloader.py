from time import sleep

from selenium.common.exceptions import ElementNotInteractableException
from selenium.webdriver.chrome.webdriver import WebDriver
from Data_base.tables import Club
from Data_base.tables import Competitor


class SportZonaDownloader:
    club_navi_patch = '//*[@id="home"]/div/ul/li'
    competitor_navi_patch = '//*[@id="players"]/div/ul/li'
    event_navi_patch = '//*[@id="home"]/div/ul/li'
    match_navi_patch = '//*[@id="fights"]/div/ul/li'

    competitors_button_patch = '//*[@id="top"]/article/div/div[2]/div/div[2]/div/ul/li[4]/a'
    club_table_patch = '//*[@id="home"]/table/tbody/tr'
    competitor_table_patch = '//*[@id="players"]/table/tbody/tr'
    event_table_patch = '//*[@id="home"]/table/tbody/tr'
    match_table_patch = '//*[@id="fights"]/table/tbody/tr'

    def __init__(self, downloader_type: str, driver: WebDriver):
        self.downloader_type = downloader_type
        self.driver = driver
        if downloader_type == 'competitors':
            self.navi_patch = self.competitor_navi_patch
            self.table_patch = self.competitor_table_patch
        elif downloader_type == 'event':
            self.navi_patch = self.event_navi_patch
            self.table_patch = self.event_table_patch
        elif downloader_type == 'match':
            self.navi_patch = self.match_navi_patch
            self.table_patch = self.match_table_patch
        else:
            self.navi_patch = self.club_navi_patch
            self.table_patch = self.club_table_patch

    def get_number_of_navi_buttons(self):
        # TODO exception no navi bar
        table_navi_buttons = self.driver.find_elements_by_xpath(self.navi_patch)
        return len(table_navi_buttons)

    def get_number_of_pages(self):
        try:
            sleep(0.5)
            if self.downloader_type == 'match':
                #for old competitions li =1 for curent li = 2
                fights_buttons = \
                    self.driver.find_elements_by_xpath('//*[@id="top"]/article/div/div[2]/div/div[2]/div/ul/li[1]/a')[0]
                fights_buttons.click()
            buttons_count = self.get_number_of_navi_buttons()
            last_button = self.driver.find_elements_by_xpath(
                self.navi_patch + '[' + buttons_count.__str__() + ']/a')[0]
            if self.downloader_type == 'competitors':
                self.driver.find_elements_by_xpath(self.competitors_button_patch)[0].click()
            last_button.click()
            table_navi_buttons = self.driver.find_elements_by_xpath(self.navi_patch)
            buttons_count = len(table_navi_buttons)
            last_page_button = \
                self.driver.find_elements_by_xpath(self.navi_patch + '[' + (buttons_count - 2).__str__() + ']/a')[0]
            result = last_page_button.text
            first_page_button = self.driver.find_elements_by_xpath(self.navi_patch + '[1]/a')[0]
            first_page_button.click()
            return int(result)
        except ElementNotInteractableException:
            return 1

    def get_number_of_rows(self):
        # first two rows is with no content and they are counted to
        res = self.driver.find_elements_by_xpath(self.table_patch)
        count = 0
        for row in range(len(res)):
            if self.check_row(row + 1):
                count += 1
        # if self.downloader_type == 'match':
        #     res = res[0:3] + self.driver.find_elements_by_xpath(self.table_patch)[2:len(res) + 1:2]
        return count

    def get_number_of_all_rows(self):
        # first two rows is with no content and they are counted to
        res = self.driver.find_elements_by_xpath(self.table_patch)
        return len(res)

    def got_to_next_page(self):
        # TODO exception no navi bar
        buttons_count = self.get_number_of_navi_buttons()
        next_page_button = \
            self.driver.find_elements_by_xpath(self.navi_patch + '[' + (buttons_count - 1).__str__() + ']/a')[0]
        next_page_button.click()

    def get_row_link(self, row_number):
        link = self.driver.find_elements_by_xpath(
            self.table_patch + '[' + (row_number + 2).__str__() + '] / td[1] / a')[0]
        return link.get_attribute('href')

    def get_row_column_link(self, row_number, column_number):
        if self.downloader_type == 'event':
            link = self.driver.find_elements_by_xpath(
                self.table_patch + '[' + (row_number + 2).__str__() + '] / td[' + str(column_number) + '] /div/ a')[0]
        else:
            link = self.driver.find_elements_by_xpath(
                self.table_patch + '[' + (row_number + 2).__str__() + '] / td[' + str(column_number) + '] / a')[0]
        return link.get_attribute('href')

    def get_row_column_value(self, row_number, column_number):
        label = self.driver.find_elements_by_xpath(
            self.table_patch + '[' + (row_number + 2).__str__() + '] / td[' +
            column_number.__str__() + ']')[0].text
        return label

    def download_club_data(self):
        name = self.driver.find_elements_by_xpath(
            '//*[@id="top"]/article/div/div[2]/div/div[2]/div/div[1]/div[2]/div[3]/table/tbody/tr[1]/td[2]/strong')[
            0].text
        city = self.driver.find_elements_by_xpath(
            '//*[@id="top"]/article/div/div[2]/div/div[2]/div/div[1]/div[2]/div[3]/table/tbody/tr[2]/td[2]/strong')[
            0].text
        year = self.driver.find_elements_by_xpath(
            '//*[@id="top"]/article/div/div[2]/div/div[2]/div/div[1]/div[2]/div[3]/table/tbody/tr[5]/td[2]/strong')[
            0].text
        licence_no = self.driver.find_elements_by_xpath(
            '//*[@id="top"]/article/div/div[2]/div/div[2]/div/div[1]/div[2]/div[3]/table/tbody/tr[7]/td[2]/strong')[
            0].text

        province = self.driver.find_elements_by_xpath(
            '//*[@id="top"]/article/div/div[2]/div/div[2]/div/div[1]/div[2]/div[3]/table/tbody/tr[3]/td[2]/strong')[
            0].text.split(' ')[0]
        if not year:
            year = None
        else:
            year = (str(year) + '-01-01')
        return Club(str(name), str(city), year, str(licence_no), province)

    def download_competitor_data(self, club=''):
        name = self.driver.find_elements_by_xpath(
            '//*[@id="top"]/article/div/div[2]/div/div[2]/div/div[1]/div[2]/div[3]/table/tbody/tr[1]/td[2]/strong')[
            0].text.split(' ')[0]
        surname = self.driver.find_elements_by_xpath(
            '//*[@id="top"]/article/div/div[2]/div/div[2]/div/div[1]/div[2]/div[3]/table/tbody/tr[1]/td[2]/strong')[
            0].text.split(' ')[1]
        born = self.driver.find_elements_by_xpath(
            '//*[@id="top"]/article/div/div[2]/div/div[2]/div/div[1]/div[2]/div[3]/table/tbody/tr[3]/td[2]/strong')[
            0].text
        licence_no = self.driver.find_elements_by_xpath(
            '//*[@id="top"]/article/div/div[2]/div/div[2]/div/div[1]/div[2]/div[3]/table/tbody/tr[6]/td[2]/strong')[
            0].text.split(' ')[0]

        return Competitor(name, surname, club, licence_no, born + '-01-01', '')

    def check_row(self, row_number):
        tds_in_row = self.driver.find_elements_by_xpath('//*[@id="fights"]/table/tbody/tr[' + str(row_number) + ']/td')
        return len(tds_in_row) > 2

    def get_row_column_td(self, row_number, column_number):
        td = self.driver.find_elements_by_xpath(
            self.table_patch + '[' + (row_number + 2).__str__() + '] / td[' + str(column_number) + ']')[0]
        return td

    def get_row_winner(self, row_number):
        return self.get_row_column_td(row_number, 3).get_attribute('class') == 'won success'

    def go_to_link(self, link):
        self.driver.get(link)


if __name__ == '__main__':

    pass



    # print('clubs:')
    # print('number of navi buttons:', club_downloader.get_number_of_navi_buttons())
    # print('number of pages:', club_downloader.get_number_of_pages())
    # print('rows:', club_downloader.get_number_of_rows())
    # if club_downloader.get_number_of_pages() > 1:
    #     club_downloader.got_to_next_page()
    #
    # print('competitors:')
    # print('number of navi buttons:', competitors_downloader.get_number_of_navi_buttons())
    # print('number of pages:', competitors_downloader.get_number_of_pages())
    # print('rows:', competitors_downloader.get_number_of_rows())
    # if competitors_downloader.get_number_of_pages() > 1:
    #     competitors_downloader.got_to_next_page()
    #
    # print('events:')
    # print('number of navi buttons:', event_downloader.get_number_of_navi_buttons())
    # print('number of pages:', event_downloader.get_number_of_pages())
    # print('rows:', event_downloader.get_number_of_rows())
    # if event_downloader.get_number_of_pages() > 1:
    #     event_downloader.got_to_next_page()

    # print('matches:')
    # print('number of navi buttons:', match_downloader.get_number_of_navi_buttons())
    # print('number of pages:', match_downloader.get_number_of_pages())
    # print('rows:', match_downloader.get_number_of_rows())
    # if match_downloader.get_number_of_pages() > 1:
    #     match_downloader.got_to_next_page()
    # for i in range(1, match_downloader.get_number_of_all_rows() - 1):
    #     sleep(0.1)
    #     if match_downloader.check_row(i):
    #         print(match_downloader.get_row_column_value(i, 2))
    #         print(match_downloader.get_row_column_link(i, 3))
    #         print(match_downloader.get_row_column_link(i, 10))
    #         print('first win:',match_downloader.get_row_winner(i))


