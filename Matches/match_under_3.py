from abc import ABC

from DataStructures.personal_competitor import *
from DataStructures.tree_node import Node as Match
from Matches.abstractMatchesMaker import AbstractMatchesMaker
from random import choice


class MatchUnder3(AbstractMatchesMaker, ABC):
    def __init__(self, competitors):
        self.competitors = competitors
        self.matches = [Match() for _ in range(3)]
        self.actual_match_id = 0
        self.is_end = False

        self._match_order = [(1, 2), (2, 3), (1, 3)]
        for competitor_id, match in zip(self._match_order, self.matches):
            match.set_left_child(self.competitors[competitor_id[0] - 1])
            match.set_right_child(self.competitors[competitor_id[1] - 1])

    def make_match(self, left_wins):
        self.matches[self.actual_match_id].make_match(left_wins)
        if self.actual_match_id == 2:
            self.is_end = True
        else:
            self.go_to_next_round()

    def go_to_next_round(self):
        if self.actual_match_id < 2:
            self.actual_match_id += 1

    def go_to_prev_round(self):
        if self.actual_match_id > 0:
            self.actual_match_id -= 1

    def get_actual_match_id(self):
        return self.actual_match_id

    def print_actual_match(self):
        print(self.actual_match_id)
        print("Left: ", self.matches[self.actual_match_id].get_left_child().name)
        print("Right: ", self.matches[self.actual_match_id].get_right_child().name)
        print("Winner: ", self.matches[self.actual_match_id].get_competitor().name)

    def get_results(self):
        competitors_points = {competitor: 0 for competitor in self.competitors}
        for match in self.matches:
            actual = competitors_points.get(match.get_competitor(), 0)
            competitors_points[match.get_competitor()] = actual + 1
        print(competitors_points)
        return competitors_points

    def check_if_reset_needed(self):
        return self.competitors[0].wins == self.competitors[1].wins == self.competitors[2].wins

    def get_competitors(self):
        return self.competitors[:]


if __name__ == "__main__":
    competitors = [PersonalCompetitor("Marcin " + str(x)) for x in range(3)]

    competiton = MatchUnder3(competitors)

    while competiton.check_if_reset_needed():
        competiton = MatchUnder3(competitors)

        for _ in range(3):
            result = choice([True, False])
            print("Left wins:", result)

            competiton.make_match(result)
            competiton.print_actual_match()
            competiton.go_to_next_round()

        competiton.get_results()