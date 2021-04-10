import personal_competitor
import random


def choose_place_in_order(half, team_number, free_places):
    if len(competitors[team_number]) != 0:
        chosen = random.choice(competitors[team_number])
        competitors[team_number].remove(chosen)

        if half == 1:
            quarter = random.randint(0, 1)
            if len(free_places[quarter]) == 0:
                if quarter == 0:
                    quarter = 1
                else:
                    quarter = 0
            if len(free_places[quarter]) == 0:
                quarter = 2
                if len(free_places[quarter]) == 0:
                    quarter = 3

        else:
            quarter = random.randint(2, 3)
            if len(free_places[quarter]) == 0:
                if quarter == 2:
                    quarter = 3
                else:
                    quarter = 2

            if len(free_places[quarter]) == 0:
                quarter = 0
                if len(free_places[quarter]) == 0:
                    quarter = 1

        place_in_order = random.choice(free_places[quarter])
        free_places[quarter].remove(place_in_order)

        return place_in_order, chosen
    return None, None


def random_function_16(competitors, number_of_competitors, master = None, runner_up = None):
    free_places = [[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12], [13, 14, 15, 16]]
    order = {}

    number_of_contestants = 0

    if master is not None:
        order[1] = master
        free_places[0].pop(0)
        number_of_contestants += 1

    if runner_up is not None:
        order[16] = runner_up
        free_places[3].pop(3)
        number_of_contestants += 1

    number_of_contestants += number_of_competitors

    free_lots = 16 - number_of_contestants
    to_fill = [0, 1, 2, 3]

    while free_lots > 0:
        if len(to_fill) == 0:
            lot = random.randint(0, 3)
        else:
            lot = random.choice(to_fill)
            to_fill.remove(lot)

        place_in_order = random.choice(free_places[lot])
        free_places[lot].remove(place_in_order)

        order[place_in_order] = personal_competitor.PersonalCompetitor(name="Free fight", is_free_fight=True)

        free_lots -= 1

    while number_of_competitors > 1:
        for i in range(len(competitors)):
            if number_of_competitors == 1:
                break

            place_in_order, chosen = choose_place_in_order(1, i, free_places)
            if place_in_order is None:
                continue
            order[place_in_order] = chosen
            number_of_competitors -= 1

            place_in_order, chosen = choose_place_in_order(2, i, free_places)
            if place_in_order is None:
                continue
            order[place_in_order] = chosen
            number_of_competitors -= 1

    return order


if __name__ == "__main__":
    competitors = [
        [personal_competitor.PersonalCompetitor("Kuba1"), personal_competitor.PersonalCompetitor("Kuba2"), personal_competitor.PersonalCompetitor("Kuba3"), personal_competitor.PersonalCompetitor("Kuba4")],
        [personal_competitor.PersonalCompetitor("Marcin1"), personal_competitor.PersonalCompetitor("Marcin2"), personal_competitor.PersonalCompetitor("Marcin3")],
        [personal_competitor.PersonalCompetitor("Adas1"), personal_competitor.PersonalCompetitor("Adas2"), personal_competitor.PersonalCompetitor("Adas3")],
        [personal_competitor.PersonalCompetitor("Gabi1"), personal_competitor.PersonalCompetitor("Gabi2")],
        [personal_competitor.PersonalCompetitor("Piotrek1")],
        [personal_competitor.PersonalCompetitor("Piotrek2")],
        [personal_competitor.PersonalCompetitor("Piotrek3")],
    ]
    master = personal_competitor.PersonalCompetitor(name="Marcin")
    runner_up = personal_competitor.PersonalCompetitor(name="Adas")

    order = random_function_16(competitors, 15, None, runner_up)

    for competitor in sorted(list(order.items()), key=lambda x: x[0]):
        print(competitor[0], competitor[1].get_name())
    print()
