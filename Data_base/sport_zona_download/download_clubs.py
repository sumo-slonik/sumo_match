from selenium import webdriver
from time import sleep


# Press the green button in the gutter to run the script.

def get_number_of_navi_buttons(driver):
    tabble_navi_buttons = driver.find_elements_by_xpath('/html/body/article/div/div[2]/div/div[2]/div/div[1]/div/ul/li')
    return len(tabble_navi_buttons)


def get_number_of_pages(driver):
    buttons_count = get_number_of_navi_buttons(driver)
    last_button = driver.find_elements_by_xpath(
        '/html/body/article/div/div[2]/div/div[2]/div/div[1]/div/ul/li[' + (buttons_count).__str__() + ']/a')[0]
    last_button.click()
    tabble_navi_buttons = driver.find_elements_by_xpath('/html/body/article/div/div[2]/div/div[2]/div/div[1]/div/ul/li')
    buttons_count = len(tabble_navi_buttons)
    last_page_button = driver.find_elements_by_xpath(
        '/html/body/article/div/div[2]/div/div[2]/div/div[1]/div/ul/li[' + (buttons_count - 2).__str__() + ']/a')[0]
    result = last_page_button.text
    first_page_button = \
        driver.find_elements_by_xpath('/html/body/article/div/div[2]/div/div[2]/div/div[1]/div/ul/li[1]/a')[0]
    first_page_button.click()
    return int(result)


def get_number_of_rows(driver):
    return len(driver.find_elements_by_xpath('/html/body/article/div/div[2]/div/div[2]/div/div[1]/table/tbody/tr'))


def got_to_next_page(driver):
    buttons_count = get_number_of_navi_buttons(driver)
    next_page_button = driver.find_elements_by_xpath(
        '/html/body/article/div/div[2]/div/div[2]/div/div[1]/div/ul/li[' + (buttons_count - 1).__str__() + ']/a')[0]
    next_page_button.click()


def get_row_link(driver, row_number):
    link = driver.find_elements_by_xpath(
        '// *[ @ id = "home"] / table / tbody / tr[' + (row_number + 1).__str__() + '] / td[1] / a')[0]

    return link.get_attribute('href')


def isRowPoland(driver, row_number):
    label = driver.find_elements_by_xpath(
        '// * [ @ id = "home"] / table / tbody / tr[' + (row_number + 1).__str__() + '] / td[3]')[0].text

    return label == 'POL'


class club:
    def __init__(self, name, city, id_no, foundation_year):
        self.name = name
        self.city = city
        self.id = id_no
        self.foundation_year = foundation_year

    def __str__(self) -> str:
        return self.name + '' + self.city + ' ' + self.id + '' + self.foundation_year

    def __repr__(self) -> str:
        return self.__str__()

    def __hash__(self) -> int:
        return super().__hash__()

def get_clubs(driver, club_preview):
    results = []
    pages = get_number_of_pages(driver)
    for page in range(pages):
        sleep(0.5)
        print(page/pages)
        rows = get_number_of_rows(driver)
        for row in range(2, rows):
            if isRowPoland(driver, row):
                link = get_row_link(driver, row)
                club = get_club(club_preview, link)
                results.append(club)
        got_to_next_page(driver)
    return results


def get_club(driver, link):
    driver.get(link)
    name = driver.find_elements_by_xpath(
        '//*[@id="top"]/article/div/div[2]/div/div[2]/div/div[1]/div[2]/div[3]/table/tbody/tr[1]/td[2]/strong')[0].text
    city = driver.find_elements_by_xpath(
        '//*[@id="top"]/article/div/div[2]/div/div[2]/div/div[1]/div[2]/div[3]/table/tbody/tr[2]/td[2]/strong')[0].text
    year = driver.find_elements_by_xpath(
        '//*[@id="top"]/article/div/div[2]/div/div[2]/div/div[1]/div[2]/div[3]/table/tbody/tr[5]/td[2]/strong')[0].text
    licence_no = driver.find_elements_by_xpath(
        '//*[@id="top"]/article/div/div[2]/div/div[2]/div/div[1]/div[2]/div[3]/table/tbody/tr[7]/td[2]/strong')[0].text

    return club(name, city, licence_no, year)


if __name__ == '__main__':
    driver = webdriver.Chrome()
    club_preview = webdriver.Chrome()
    driver.get('https://sportzona.pl/app/clubs/list/sumo')

    clubs = get_clubs(driver, club_preview)
    for i in clubs:
        print(i)

    # # sleep(2)
    # links = []
    # # get tabble
    # number_of_pages = get_number_of_pages(driver)
    #
    # print(get_row_link(driver, 1))
    # club_preview.get(get_row_link(driver, 1))
    # # for _ in range(number_of_pages):
    # #     sleep(0.2)
    # #     got_to_next_page(driver)
    #
    # print(number_of_pages)
