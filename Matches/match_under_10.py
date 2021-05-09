from abc import ABC

from DataStructures import personal_competitor
from Matches.match_under_5 import MatchUnder5Wrapper
from Matches.abstractMatchesMaker import AbstractMatchesMaker
from DataStructures.tree_node import Node


class Overtime:
    def __init__(self, winners):
        self.competitors = [winners[0][0], winners[1][1], winners[0][1], winners[1][0]]
        self.actual_match_id = 0
        self.tree = [Node() for x in range(3)]

        self.tree[0].left_child = self.competitors[0]
        self.tree[0].right_child = self.competitors[1]

        self.tree[1].left_child = self.competitors[2]
        self.tree[1].right_child = self.competitors[3]

        self.tree[2].left_child = self.tree[0]
        self.tree[2].right_child = self.tree[1]

    def make_match(self, left_wins):
        print("--------------------" + str(self.actual_match_id))
        self.tree[self.actual_match_id].make_match(left_wins)
        self.go_to_next_round()

    def go_to_next_round(self):
        self.actual_match_id += 1

    def go_to_prev_round(self):
        if self.actual_match_id > 0:
            self.actual_match_id -= 1


class MatchUnder10(AbstractMatchesMaker, ABC):
    def __init__(self, competitors):
        self.first_group = MatchUnder5Wrapper(competitors[:int(len(competitors) / 2)])
        self.second_group = MatchUnder5Wrapper(competitors[int(len(competitors) / 2):])

        self.overtime = None
        self.winners = [[], []]

        self.is_end = False
        self.results = []
        self.state = 0

    def make_match(self, left_wins):
        if not self.first_group.is_end:
            self.first_group.make_match(left_wins)
            if self.first_group.is_end:
                self.state = 1

        elif not self.second_group.is_end:
            self.second_group.make_match(left_wins)
            if self.second_group.is_end:
                self.state = 2
                self.extract_winners()
                self.overtime = Overtime(self.winners)

        else:
            print("finały----------------------")
            self.overtime.make_match(left_wins)

            if self.overtime.actual_match_id == 3:
                self.is_end = True
            self.state += 1

    def extract_winners(self):
        self.winners[0] = [self.first_group.results[0], self.first_group.results[1]]
        self.winners[1] = [self.second_group.results[0], self.second_group.results[1]]

    def get_results(self):
        self.results = self.first_group.results[2:] + self.second_group.results[2:]
        self.results.sort(key=lambda x: x.wins, reverse=True)

        if self.overtime.tree[0].left_child != self.overtime.tree[0].competitor:
            self.results.append(self.overtime.tree[0].left_child)
        else:
            self.results.append(self.overtime.tree[0].right_child)

        if self.overtime.tree[1].left_child != self.overtime.tree[1].competitor:
            self.results.append(self.overtime.tree[1].left_child)
        else:
            self.results.append(self.overtime.tree[1].right_child)

        if self.overtime.tree[2].left_child.competitor != self.overtime.tree[2].competitor:
            self.results.append(self.overtime.tree[2].left_child.competitor)
        else:
            self.results.append(self.overtime.tree[2].right_child.competitor)

        self.results.append(self.overtime.tree[2].competitor)

        self.results.reverse()

    def go_to_next_round(self):
        pass

    def go_to_prev_round(self):
        pass

    def get_actual_match_id(self):
        pass

    def print_results(self):
        for competitor in self.results:
            print(competitor.name, competitor.wins)


if __name__ == "__main__":
    Competitors = [personal_competitor.PersonalCompetitor("Kuba1"), personal_competitor.PersonalCompetitor("Kuba2"),
                   personal_competitor.PersonalCompetitor("Marcin1"), personal_competitor.PersonalCompetitor("Marcin2"),
                   personal_competitor.PersonalCompetitor("pojedynczy1"),
                   personal_competitor.PersonalCompetitor("pojedynczy2")]

    competition = MatchUnder10(Competitors)

    while not competition.is_end:
        first_won = input("czy pierwszy zawodnik wygrał? ")
        first_won = True if first_won == "tak" else False
        competition.make_match(first_won)

    print("after while")

    competition.first_group.print_results()
    print("-------------------")
    competition.second_group.print_results()
    print("--------------------")

    competition.get_results()
    competition.print_results()
