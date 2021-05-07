from abc import ABC

import personal_competitor
from all_match_engine import MatchUnder5Wrapper
from abstractMatchesMaker import AbstractMatchesMaker
from tree_node import Node


class Overtime:
    def __init__(self, winners):
        self.competitors = [winners[0][0], winners[0][1], winners[1][0], winners[1][1]]
        self.actual_match_id = 0
        self.tree = [Node() for x in range(3)]

        self.tree[0].left_child = self.competitors[0]
        self.tree[0].right_child = self.competitors[4]

        self.tree[1].left_child = self.competitors[3]
        self.tree[1].right_child = self.competitors[2]

        self.tree[3].left_child = self.tree[0]
        self.tree[3].right_child = self.tree[1]

    def make_match(self, left_wins):
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

    def make_match(self, left_wins):
        if not self.first_group.is_end:
            self.first_group.make_match(left_wins)

        elif not self.second_group.is_end:
            self.second_group.make_match(left_wins)

        else:
            print("dogrywka----------------------")
            if self.overtime is None:
                self.overtime = Overtime(self.winners)

            self.overtime.make_match(left_wins)

    def go_to_next_round(self):
        pass

    def go_to_prev_round(self):
        pass

    def get_actual_match_id(self):
        pass


if __name__ == "__main__":
    Competitors = [personal_competitor.PersonalCompetitor("Kuba1"), personal_competitor.PersonalCompetitor("Kuba2"),
                   personal_competitor.PersonalCompetitor("Marcin1"), personal_competitor.PersonalCompetitor("Marcin2"),
                   personal_competitor.PersonalCompetitor("pojedynczy1"),
                   personal_competitor.PersonalCompetitor("pojedynczy2")]

    competition = MatchUnder10(Competitors)

    while True:
        first_won = input("czy pierwszy zawodnik wygrał? ")
        first_won = True if first_won == "tak" else False
        competition.make_match(first_won)
