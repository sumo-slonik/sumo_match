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


if __name__ == '__main__':
    personal_competitor_txt_input("Competitors.txt")
