import sqlalchemy
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from Data_base.tables import Competition, Competitor, Match, CategoryAtCompetitions, Club, AgeCategory, WeightCategory
from copy import deepcopy
from Data_base.Analyse.DataVisualiser import one_value_per_label, two_value_per_label, tree_value_per_label, \
    six_value_per_label, plot_on_poland_regions_map, get_region_for_city
from Data_base.Analyse.DataAnalyser import DataAnalyser


def separate_genders(competitors: {Competitor}):
    result = {'Man': set(), 'Woman': set()}
    for competitor in competitors:
        result[competitor.gender].add(competitor)
    return result


if __name__ == '__main__':

    # configure class to get data
    DATABSE_URI = 'mysql+mysqlconnector://{user}:{password}@{server}/{database}'.format(user='root', password='admin',
                                                                                        server='localhost',
                                                                                        database='sumo_match_maker')
    analyser = DataAnalyser(DATABSE_URI)

    genders = ['kobiety', 'mężczyźni']

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
    # dict key = year value = dict where key = age category value
    # dict where key = weight category value = set of competitors
    competitors_in_weight_categories = dict()
    # dict where key = year value = set od clubs
    clubs_active_in_years = dict()
    # dict where key = year value = competitions
    competitions_in_year = dict()

    # Getting active competitors in years
    for year in range(2014, 2022):
        competitors_active_in_years[year] = analyser.get_competitors_in_year(year)
    ages = sorted(competitors_active_in_years.keys())

    # print('active competitors in each years:')
    # for year in competitors_active_in_years:
    #     print(year, len(competitors_active_in_years[year]))
    #
    # one_value_per_label("Aktywni zawodnicy w latach 2014-2021",
    #                     "Liczba aktywnych zawodników",
    #                     competitors_active_in_years.keys(),
    #                     [len(competitors_active_in_years[x]) for x in competitors_active_in_years])

    # getting activity level of competitors
    # activity_levels = {year: analyser.get_competitors_activity_levels(competitors_active_in_years[year], year) for year
    #                    in ages}
    # low_active = [len(activity_levels[year]['low active']) for year in ages]
    # active = [len(activity_levels[year]['active']) for year in ages]
    # very_active = [len(activity_levels[year]['very active']) for year in ages]
    # tree_value_per_label("Podział na poziomy aktywności zawodników w latach 2014-2021", "Liczba zawodników", ages,
    #                      low_active, active, very_active, ["Mało aktywni", "Aktywni", "Bardzo aktywni"])
    #
    # # getting active competitors in years separated by gender
    #
    # competitors_active_genders = {year: separate_genders(competitors_active_in_years[year])
    #                               for year in competitors_active_in_years}
    # active_woman = [len(competitors_active_genders[year]["Woman"]) for year in ages]
    # active_man = [len(competitors_active_genders[year]["Man"]) for year in ages]
    #
    # two_value_per_label("Aktywni zaowdnicy w latach 2014-2021 z podziałem na płci", "Liczba aktywnych zawodników", ages,
    #                     active_woman, active_man, ["Kobiety", "Mężczyźni"])

    # getting active competitors separated by age categories

    # for age_category in analyser.get_age_categories():
    #     for year in competitors_active_in_years:
    #         competitors = analyser.get_competitors_started_in_age_category_in_year(age_category, year)
    #         dict_of_competitors = competitors_in_age_categories_in_years.get(year, dict())
    #         new_dict = {age_category: deepcopy(competitors)}
    #         dict_of_competitors.update(new_dict)
    #         competitors_in_age_categories_in_years[year] = dict_of_competitors
    # print('__________________________________________________________________')
    # print('active competitors in age categories')
    # for year in competitors_in_age_categories_in_years:
    #     for age_category in competitors_in_age_categories_in_years[year]:
    #         print(age_category, year, len(competitors_in_age_categories_in_years[year][age_category]))
    # for i in competitors_in_age_categories_in_years:
    #     print(i)
    # active_mlodzik = [len(competitors_in_age_categories_in_years[year]['Młodzik (u14)']) for year in ages]
    # active_kadet = [len(competitors_in_age_categories_in_years[year]['Kadet (u16)']) for year in ages]
    # active_junior = [len(competitors_in_age_categories_in_years[year]['Junior (u18)']) for year in ages]
    # active_mlodzierzowiec21 = [len(competitors_in_age_categories_in_years[year]['Młodzierzowiec (u21)']) for year in
    #                            ages]
    # active_mlodzierzowiec23 = [len(competitors_in_age_categories_in_years[year]['Młodzierzowiec (u23)']) for year in
    #                            ages]
    # active_senior = [len(competitors_in_age_categories_in_years[year]['Senior ']) for year in ages]
    #
    # six_value_per_label("Aktywni zawodnicy z podziałem na kategorie wiekowe", "liczba zawodników",
    #                     ages, active_mlodzik,
    #                     active_kadet, active_junior, active_mlodzierzowiec21, active_mlodzierzowiec23, active_senior)

    # weight categories analyse
    # for year in ages:
    #     competitors_in_year = competitors_in_weight_categories.get(year, dict())
    #     for age_category in analyser.get_age_categories():
    #         competitors_in_age_category = competitors_in_year.get(age_category, dict())
    #         for weight_category in analyser.get_weight_categories_in_age_category(age_category):
    #             competitors_in_weight_category = analyser.get_competitors_in_year_in_age_category_in_weight_category(
    #                 year, age_category, weight_category)
    #             if len(competitors_in_weight_category):
    #                 competitors_in_age_category[weight_category] = len(competitors_in_weight_category)
    #         competitors_in_year[age_category] = competitors_in_age_category
    #     competitors_in_weight_categories[year] = competitors_in_year
    #
    # print('__________________________________________________________________')
    # print('competitors in weight categories')
    #
    # for age_category in analyser.get_age_categories():
    #     for year in ages:
    #         woman_values = []
    #         woman_categories_in_year = []
    #         man_categories_in_year = []
    #         man_values = []
    #         for weight_category in analyser.get_weight_categories_in_age_category(age_category):
    #             # add vals to mens
    #             competitors = analyser.get_competitors_in_year_in_age_category_in_weight_category(year, age_category,
    #                                                                                               weight_category)
    #             if competitors:
    #                 if weight_category.gender == 'kobiety':
    #                     woman_values.append(len(competitors))
    #                     woman_categories_in_year.append(weight_category.weight_category)
    #                 else:
    #                     man_values.append(len(competitors))
    #                     man_categories_in_year.append(weight_category.weight_category)
    #
    #         one_value_per_label(
    #             "Aktywne zawodniczki (kobiety " + age_category + "\nw kategoriach wagowych w roku " + str(year),
    #             "liczba zawodnikczek", woman_categories_in_year, woman_values, "kategorie wagowe")
    #         one_value_per_label(
    #             "Aktywni zawodnicy (mężczyżni " + age_category + "\nw kategoriach wagowych w roku " + str(year),
    #             "liczba zawodników", man_categories_in_year, man_values, "kategorie wagowe")
    #
    # for region in analyser.get_regions():
    #     competitors_in_regions[region] = analyser.get_competitors_in_region(region)
    # print('__________________________________________________________________')
    # print('competitors in regions')
    # for region in competitors_in_regions:
    #     print(region, len(competitors_in_regions[region]))
    #
    # region_values = {region: len(competitors_in_regions[region]) for region in competitors_in_regions}
    # plot_on_poland_regions_map(region_values, "Zawodnicy z podziałem na rejony polski w latach 2014-2021")
    #
    # for year in competitors_active_in_years:
    #     region_values = {region: len(competitors_in_regions[region] & competitors_active_in_years[year]) for region in
    #                      competitors_in_regions}
    #     plot_on_poland_regions_map(region_values, "Zawodnicy z podziałem na rejony polski w roku " + str(year))
    #
    # # activity levels in age categories
    # for age_category in analyser.get_age_categories():
    #     activity_levels = {
    #         year: analyser.get_competitors_activity_levels(competitors_in_age_categories_in_years[year][age_category],
    #                                                        year, age_category) for
    #         year
    #         in ages}
    #     low_active = [len(activity_levels[year]['low active']) for year in ages]
    #     active = [len(activity_levels[year]['active']) for year in ages]
    #     very_active = [len(activity_levels[year]['very active']) for year in ages]
    #     tree_value_per_label("Podział na poziomy aktywności zawodników w latach 2014-2021 dla\n" + age_category,
    #                          "Liczba zawodników", ages,
    #                          low_active, active, very_active, ["Mało aktywni", "Aktywni", "Bardzo aktywni"])
    #
    #
    # # new competitors in years
    #
    # used = set()
    # for year in competitors_active_in_years:
    #     competitors_new_in_years[year] = competitors_active_in_years[year] - used
    #     used = used | competitors_active_in_years[year]
    #
    # print('__________________________________________________________________')
    # print('new competitors in years')
    # for year in competitors_new_in_years:
    #     print(year, len(competitors_new_in_years[year]))
    #
    # new_competitor_in_years = [len(competitors_new_in_years[year]) for year in ages[1:]]
    # one_value_per_label("Nowi zawodnicy w latach 2014-2021", "liczba zawodników", ages[1:], new_competitor_in_years)
    #
    # # new competitors in age categories
    # for age_category in analyser.get_age_categories():
    #     new_competitor_in_years = [
    #         len(competitors_new_in_years[year] & competitors_in_age_categories_in_years[year][age_category]) for year in
    #         ages[1:]]
    #     one_value_per_label("Nowi zawodnicy w latach 2014-2021 dla\n" + age_category, "liczba zawodników", ages[1:],
    #                         new_competitor_in_years)
    #
    # print('__________________________________________________________________')
    # print('new competitors in years in age categories')
    # for year in competitors_new_in_years:
    #     for age_category in competitors_in_age_categories_in_years[year]:
    #         print(year, age_category,
    #               len(competitors_new_in_years[year] & competitors_in_age_categories_in_years[year][age_category]))
    #
    # print('activity levels of competitors')
    # for year in competitors_active_in_years:
    #     print(year, ':')
    #     activity_lvl = analyser.get_competitors_activity_levels(competitors_active_in_years[year], year)
    #     for activity in activity_lvl:
    #         print(activity, len(activity_lvl[activity]))
    #         separated_genders = separate_genders(activity_lvl[activity])
    #         for gender in separated_genders:
    #             print(gender, len(separated_genders[gender]))


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
    #
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

    # active clubs
    # clubs_active_in_years = {year: analyser.get_active_clubs_in_year(year) for year in ages}
    # values = [len(clubs_active_in_years[year]) for year in ages]
    # one_value_per_label("Aktywne kluby w latach 2014-2021", "Aktywne kluby", ages, values)
    # for year in ages:
    #     clubs_in_regions = {region: 0 for region in analyser.get_regions()}
    #     for club in clubs_active_in_years[year]:
    #         clubs_in_regions[club.province] += 1
    #     plot_on_poland_regions_map(clubs_in_regions, "Aktywne kluby w roku " + str(year))
    #
    # clubs_in_regions = {region: 0 for region in analyser.get_regions()}
    # for club in analyser.get_all_clubs():
    #     clubs_in_regions[club.province] += 1
    # plot_on_poland_regions_map(clubs_in_regions, "Aktywne kluby w latach 2014-2021")

    all_competitions_in_regions = {region.upper(): 0 for region in analyser.get_regions()}
    for year in ages:
        competitions_in_year[year] = analyser.get_competitions_in_year(year)
    for year in ages:
        year_competitions_in_regions = {region.upper(): 0 for region in analyser.get_regions()}
        for competition in competitions_in_year[year]:
            year_competitions_in_regions[get_region_for_city(competition.city).upper()] += 1
            all_competitions_in_regions[get_region_for_city(competition.city).upper()] += 1
            if year == 2017 and get_region_for_city(competition.city).upper() == "MAZOWIECKIE":
                print(competition)
        plot_on_poland_regions_map(year_competitions_in_regions,
                                   "Liczba imprez w roku " + str(year) + "\nz podziałem na województwa")
    plot_on_poland_regions_map(all_competitions_in_regions,
                               "Liczba imprez w latach 2014-2021")
    values = []
    for year in ages:
        values.append(len(competitions_in_year[year]))
    one_value_per_label("Liczba imprez sportowych w latach 2014-2021", "Liczba impraz", ages, values)
