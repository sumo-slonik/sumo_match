import personal_competitor
import random


def random_function_10(competitors, number_of_competitors, master=None, runner_up=None):

    first_group = []
    second_group = []

    to_first = 1

    if master is not None:
        first_group.append(master)

    if runner_up is not None:
        second_group.append(runner_up)

    while number_of_competitors > 0:
        for i in range(len(competitors)):
            if number_of_competitors == 0:
                break

            if len(competitors[i]) == 0:
                continue

            if len(competitors[i]) == 1:
                if to_first:
                    first_group.append(competitors[i][0])
                    to_first = 0
                else:
                    second_group.append(competitors[i][0])
                    to_first = 1

                competitors[i] = []
                number_of_competitors -= 1
                continue

            first_group.append(competitors[i][0])
            second_group.append(competitors[i][1])

            competitors[i].remove(competitors[i][0])
            competitors[i].remove(competitors[i][0])

            number_of_competitors -= 2

    #przetasować ich
    return first_group, second_group


if __name__ == "__main__":
    competitors = [
        [personal_competitor.PersonalCompetitor("Kuba1"), personal_competitor.PersonalCompetitor("Kuba2")],
        [personal_competitor.PersonalCompetitor("Marcin1"), personal_competitor.PersonalCompetitor("Marcin2")],
        [personal_competitor.PersonalCompetitor("pojedynczy1")],
        [personal_competitor.PersonalCompetitor("pojedynczy2")]
    ]

    master = personal_competitor.PersonalCompetitor(name="Marcin")
    runner_up = personal_competitor.PersonalCompetitor(name="Adas")

    first_group, second_group = random_function_10(competitors, 6, master)

    print("first group:")
    for competitor in first_group:
        print(competitor.get_name())
    print()

    print("second group:")
    for competitor in second_group:
        print(competitor.get_name())
© 2021 GitHub, Inc.
