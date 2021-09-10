from random import randint

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import geopandas as gpd
# import folium
from matplotlib import cm

TERC_for_regions = {
    "DOLNOŚLĄSKIE": '02',
    "KUJAWSKO-POMORSKIE": '04',
    "LUBELSKIE": '06',
    "LUBUSKIE": '08',
    "ŁÓDZKIE": '10',
    "MAŁOPOLSKIE": '12',
    "MAZOWIECKIE": '14',
    "OPOLSKIE": '16',
    "PODKARPACKIE": '18',
    "PODLASKIE": '20',
    "POMORSKIE": '22',
    "ŚLĄSKIE": '24',
    "ŚWIĘTOKRZYSKIE": '26',
    "WARMIŃSKO-MAZURSKIE": '28',
    "WIELKOPOLSKIE": '30',
    "ZACHODNIOPOMORSKIE": '32'
}

region_for_city = \
    {
        "TYSZOWCE": "Lubelskie",
        "KROTOSZYN": "Wielkopolskie",
        "SIEDLCE - STOK LACKI": "Mazowieckie",
        "GORZÓW WLKP.": "Lubuskie",
        "PYRZYCE": "Zachodniopomorskie",
        "ROPCZYCE": "Podkarpackie",
        "OLSZTYN": "warmińsko-mazurskie",
        "DĘBICA": "Podkarpackie",
        "POZNAŃ": "Wielkopolskie",
        "BIELAWA": "Dolnośląskie",
        "KWIDZYN": "Pomorskie",
        "WOCŁAW JELCZ-LASKOWICE": "dolnośląskie",
        "LUBLIN": "Lubelskie",
        "STRZELCE OP.": "Opolskie",
        "SUWAŁKI": "Podlaskie",
        "WARSZAWA": "Mazowieckie",
        "GORZÓW WIELKOPOLSKI": "Lubuskie",
        "MYŚLENICE": "Małopolskie",
        "STRZELCE OPOLSKIE": "Opolskie",
        "SIEDLCE": "Mazowieckie",
        "ZAMOŚĆ": "Lubelskie",
        "BRZEG DOLNY": "Dolnośląskie",
        "KIELCE": "Świętokrzyskie",
        "SKARBIMIERZ": "Opolskie",
        "BIAŁYSTOK": "Podlaskie",
        "KRAKÓW": "Małopolskie",
        "KOBYLIN": "Wielkopolskie",
        "GORZÓW WLKP": "Lubuskie",
        "WROCŁAW JELCZ-LASKOWICE": "dolnośląskie",
        "MIĘDZYRZECZ": "Lubuskie",
        "KIELCE/SITKÓWKA-NOWINY": "Świętokrzyskie",
        "ŁĘCZNA": "Lubelskie",
        "KORONOWO": "Kujawsko-Pomorskie",
        "WARSZWA": "Mazowieckie",
        "ŁOMŻA": "Podlaskie",
        "ŁÓDŹ": "Łódzkie",
        "NOWINY": "Świętokrzyskie",
        "SITKÓWKA-NOWINY": "Świętokrzyskie",
        "MYSLENICE":"Małopolskie"}


def one_value_per_label(title, Y_label, labels, values, X_label='', width=0.35):
    x = np.arange(len(labels))  # the label locations
    fig, ax = plt.subplots()
    rects1 = ax.bar(x - width / 2, values, width)
    ax.set_ylabel(Y_label)
    ax.set_xlabel(X_label)
    ax.set_title(title)
    ax.set_xticks(x)
    ax.set_xticklabels(labels)
    ax.bar_label(rects1, padding=3)
    fig.tight_layout()
    plt.show()


def two_value_per_label(title, Y_label, labels, values_I, values_II, sub_labels=("Kobiety", "Mężczyżni"), X_label='',
                        width=0.35):
    x = np.arange(len(labels))  # the label locations
    width = 0.35  # the width of the bars

    fig, ax = plt.subplots()
    rects1 = ax.bar(x - width / 2, values_I, width, label=sub_labels[0])
    rects2 = ax.bar(x + width / 2, values_II, width, label=sub_labels[1])

    # Add some text for labels, title and custom x-axis tick labels, etc.
    ax.set_ylabel(Y_label)
    ax.set_xlabel(X_label)
    ax.set_title(title)
    ax.set_xticks(x)
    ax.set_xticklabels(labels)
    ax.legend()

    ax.bar_label(rects1, padding=3)
    ax.bar_label(rects2, padding=3)

    fig.tight_layout()

    plt.show()


def tree_value_per_label(title, Y_label, labels, values_I, values_II, values_III,
                         sub_labels=("Mało aktywni", "Aktywni", "Bardzo aktywni"), X_label='',
                         width=0.35, colors=('red', 'gold', 'forestgreen')):
    x = np.arange(len(labels))  # the label locations
    width = 0.35  # the width of the bars
    fig, ax = plt.subplots()
    rects1 = ax.bar(x - width / 2, values_I, 1 / 3 * width, label=sub_labels[0], color=colors[0])
    rects2 = ax.bar(x + ((-width + 4 / 3 * width) / 2), values_II, 1 / 3 * width, label=sub_labels[1], color=colors[1])
    rects3 = ax.bar(x + ((-width + 8 / 3 * width) / 2), values_III, 1 / 3 * width, label=sub_labels[2], color=colors[2])
    # Add some text for labels, title and custom x-axis tick labels, etc.
    ax.set_ylabel(Y_label)
    ax.set_xlabel(X_label)
    ax.set_title(title)
    ax.set_xticks(x)
    ax.set_xticklabels(labels)
    ax.legend()

    ax.bar_label(rects1, padding=3)
    ax.bar_label(rects2, padding=3)
    ax.bar_label(rects3, padding=3)
    fig.tight_layout()

    plt.show()


def six_value_per_label(title, Y_label, labels, values_I, values_II, values_III, values_IV, values_V, values_VI,
                        sub_labels=(
                                "młodzik (u14)", "kadet (u16)", "junior (u18)", "młodzieżowiec (u21)",
                                "młodzieżowiec (u23)",
                                "senior"), X_label='',
                        width=0.35, show_bar_label=False):
    x = np.arange(0, 3 * len(labels), 3)  # the label locations
    width = 0.35  # the width of the bars
    fig, ax = plt.subplots()
    rects1 = ax.bar(x - 7 * width / 2, values_I, 1 / 3 * width, label=sub_labels[0])
    rects2 = ax.bar(x + ((-7 * width + 2 * width) / 2), values_II, 1 / 3 * width, label=sub_labels[1])
    rects3 = ax.bar(x + ((-7 * width + 4 * width) / 2), values_III, 1 / 3 * width, label=sub_labels[2])
    rects4 = ax.bar(x + ((-7 * width + 6 * width) / 2), values_IV, 1 / 3 * width, label=sub_labels[3])
    rects5 = ax.bar(x + ((-7 * width + 8 * width) / 2), values_V, 1 / 3 * width, label=sub_labels[4])
    rects6 = ax.bar(x + ((-7 * width + 10 * width) / 2), values_VI, 1 / 3 * width, label=sub_labels[5])
    # Add some text for labels, title and custom x-axis tick labels, etc.
    ax.set_ylabel(Y_label)
    ax.set_xlabel(X_label)
    ax.set_title(title)
    ax.set_xticks(x)
    ax.set_xticklabels(labels)
    ax.legend()
    if show_bar_label:
        ax.bar_label(rects1, padding=3)
        ax.bar_label(rects2, padding=3)
        ax.bar_label(rects3, padding=3)
        ax.bar_label(rects4, padding=3)
        ax.bar_label(rects5, padding=3)
        ax.bar_label(rects6, padding=3)
    fig.tight_layout()

    plt.show()


def plot_on_poland_regions_map(data: dict, title):
    region_map = gpd.read_file('D:\sumo_match\Data_base\Analyse\Wojewodztwa.shp')
    region_map = region_map[['JPT_KOD_JE', "geometry"]]

    data_region_names = data.keys()
    data_values = [data[x] for x in data_region_names]
    TERCs = [get_TERC(x) for x in data_region_names]
    data = {"regions": data_region_names, 'values': data_values, 'JPT_KOD_JE': TERCs}
    data = pd.DataFrame.from_dict(data)
    data_for_region_map = pd.merge(region_map, data, how='left', left_on='JPT_KOD_JE', right_on='JPT_KOD_JE')
    data_for_region_map = data_for_region_map.to_crs(epsg=2180)
    print(data)
    print(region_map)
    fig, ax = plt.subplots(1, figsize=(8, 8))

    data_for_region_map.plot(column='values', ax=ax, cmap='YlOrRd', linewidth=0.8, edgecolor='gray', legend=True)

    ax.axis('off')
    ax.set_title(title)
    plt.show()

def get_TERC(region: str):
    region = region.strip().upper()
    if region:
        return TERC_for_regions[region]
    else:
        return False


def get_region_for_city(city):
    return region_for_city[city]



if __name__ == '__main__':
    one_value_per_label("nazwa", "wartości", [1, 2, 3], [5, 10, 15])
    two_value_per_label("nazwa", "wartości", [1, 2, 3], [5, 10, 15], [10, 20, 25])
    tree_value_per_label("nazwa", "wartości", [1, 2, 3], [5, 10, 15], [10, 20, 25], [20, 40, 80])
    six_value_per_label("nazwa", "wartości", [1, 2, 3], [5, 10, 15], [10, 20, 25], [20, 40, 80], [5, 10, 15],
                        [10, 20, 25], [20, 40, 80])
    DATABSE_URI = 'mysql+mysqlconnector://{user}:{password}@{server}/{database}'.format(user='root', password='admin',
                                                                                        server='localhost',
                                                                                        database='sumo_match_maker')

    random_values_for_regions = {region: randint(0, 1000) for region in TERC_for_regions}
    plot_on_poland_regions_map(random_values_for_regions)
