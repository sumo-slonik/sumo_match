from personal_competitor import *
from tree_node import Node as Match
from abstractMatchesMaker import AbstractMatchesMaker
from random import choice


class MatchUnder4(AbstractMatchesMaker):

    def __init__(self, competitors):
        self.competitors = competitors
        self.matches = [Match() for _ in range(6)]
        self.actualMatchId = 0
        self.is_end = False

        # in the documents directory there is
        # a visualisation of the players' order, the player
        # number in matches is an index in the competitors table increased by one
        self.__matchOrder = [(1, 2), (3, 4), (1, 3), (4, 2), (1, 4), (2, 3)]
        for competitors_id, match in zip(self.__matchOrder, self.matches):
            match.set_left_child(self.competitors[competitors_id[0] - 1])
            match.set_right_child(self.competitors[competitors_id[1] - 1])

    def make_match(self, left_win):
        self.matches[self.actualMatchId].make_match(left_win)
        self.print_actual_match()
        if self.actualMatchId == 5:
            self.is_end = True
        else:
            self.go_to_next_round()

    def go_to_next_round(self):
        if self.actualMatchId < 10:
            self.actualMatchId += 1

    def go_to_prev_round(self):
        if self.actualMatchId > 0:
            self.actualMatchId -= 1

    def get_actual_match_id(self):
        return self.actualMatchId

    def get_actual_match(self):
        return self.matches[self.get_actual_match_id()]

    def print_actual_match(self):
        print(self.actualMatchId)
        print("Left: ", self.matches[self.actualMatchId].get_left_child().name)
        print("Right: ", self.matches[self.actualMatchId].get_right_child().name)
        print("Winner: ", self.matches[self.actualMatchId].get_competitor().name)

    def get_results(self):
        competitors_points = {competitor: 0 for competitor in self.competitors}
        for match in self.matches:
            actual = competitors_points.get(match.get_competitor(), 0)
            competitors_points[match.get_competitor()] = actual + 1
        return competitors_points

    def get_competitors(self):
        return self.competitors[:]


if __name__ == '__main__':

    Competitors = [PersonalCompetitor("Kuba " + str(x)) for x in range(5)]
    matches = MatchUnder4(Competitors)
    for _ in range(10):
        result = choice([True, False])
        print("Left Win:", result)
        matches.make_match(result)
        matches.print_actual_match()
        matches.go_to_next_round()
    matches.get_results()
