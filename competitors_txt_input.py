from personal_competitor import PersonalCompetitor


def personal_competitor_txt_input(source):
    results = []
    file = open(source, "r",encoding="utf-8")
    for line in file:
        tmp = line.strip()
        tmp = tmp.split(";")
        if tmp[0] == "WOLNY LOS":
            results.append(PersonalCompetitor(is_free_fight=True))
        else:
            name = tmp[0]
            club = tmp[1]
            results.append(PersonalCompetitor(name=name, club=club))
    file.close()
    return results


def divide_competitors_to_teams(competitors):
    teams = {}

    for competitor in competitors:
        if competitor.club == '':
            continue
        if teams.get(competitor.club, None) is not None:
            teams[competitor.club].append(competitor)
        else:
            teams[competitor.club] = [competitor]

    teams = list(teams.values())
    teams.sort(key=lambda x: len(x), reverse=True)

    return teams


if __name__ == '__main__':
    competitors = personal_competitor_txt_input("Competitors.txt")
    teams = divide_competitors_to_teams(competitors)

    print(teams)
