from DataStructures.club_competitor import ClubCompetitor
from DataStructures.personal_competitor import PersonalCompetitor


def personal_competitor_txt_input(source):
    results = []
    file = open(source, "r", encoding="utf-8")
    for line in file:
        tmp = line.strip()
        tmp = tmp.split(";")
        if tmp[0] == "WOLNY LOS":
            results.append(PersonalCompetitor(name='WOLNY LOS',is_free_fight=True))
        else:
            name = tmp[0]
            club = tmp[1]
            results.append(PersonalCompetitor(name=name, club=club))
    file.close()
    return results


def club_competitor_txt_input(source):
    results = []
    counter = 0
    club_name = ''
    list_of_competitors = []
    with open(source, "r", encoding="utf-8") as file:
        for line in file:
            tmp = line.strip()
            tmp = tmp.split()
            if tmp[0] == 'klub':
                club_name = ' '.join(tmp[1:])
            else:
                if tmp[0] == "WOLNY LOS":
                    results.append(PersonalCompetitor(name='WOLNY LOS', is_free_fight=True))
                else:
                    name = ' '.join(tmp[:])
                    list_of_competitors.append(PersonalCompetitor(name=name, club=club_name))
                    counter += 1
                if counter == 4:
                    results.append(ClubCompetitor(*list_of_competitors, club_name))
                    list_of_competitors = []
                    counter = 0
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
    # competitors = personal_competitor_txt_input("Competitors.txt")
    # teams = divide_competitors_to_teams(competitors)
    #
    # print(teams)

    team_competitors = club_competitor_txt_input(r'D:\sumo_match\Categories\10Team.txt')
    for i in team_competitors:
        print(i)
        for j in i.get_competitors_list():
            print(j.name)
