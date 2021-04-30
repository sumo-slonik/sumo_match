from abc import ABC

from personal_competitor import *
from tree_node import Node
from abstractMatchesMaker import AbstractMatchesMaker


class MatchIfDraw:
    def __init__(self, competitor1, competitor2):
        self.round = Node(left_child=competitor1, right_child=competitor2)

    def make_match(self, left_wins):
        if left_wins:
            self.round.left_child.wins += 1
            self.round.right_child.losses += 1
        else:
            self.round.left_child.losses += 1
            self.round.right_child.wins += 1


class MatchUnder2(AbstractMatchesMaker, ABC):
    def __init__(self, competitors):
        self.competitors = competitors
        self.actual_round_id = 0
        self.rounds = [Node(left_child=competitors[0], right_child=competitors[1]) for i in range(2)]
        self.final = None

    def make_match(self, left_wins):
        if left_wins:
            self.rounds[self.actual_round_id].competitor = self.competitors[0]
            self.competitors[0].wins += 1
            self.competitors[1].losses += 1

        else:
            self.rounds[self.actual_round_id].competitor = self.competitors[1]
            self.competitors[1].wins += 1
            self.competitors[0].losses += 1

    def check_if_next_round_necessary(self):
        if self.competitors[0].wins == self.competitors[1].wins:
            self.final = MatchIfDraw(self.competitors[0], self.competitors[1])
            return True

        return False

    def go_to_next_round(self):
        if self.actual_round_id == 1:
            return
        self.actual_round_id += 1

    def go_to_prev_round(self):
        if self.actual_round_id == 0:
            return
        self.actual_round_id -= 1

    def get_actual_match_id(self):
        return self.actual_round_id

    def get_places(self):
        if self.competitors[0].wins > self.competitors[1].wins:
            return [[self.competitors[0]], [self.competitors[1]]]
        else:
            return [[self.competitors[1]], [self.competitors[0]]]


if __name__ == "__main__":
    competitors = [PersonalCompetitor(name="Kuba"), PersonalCompetitor(name="Marcin")]

    match = MatchUnder2(competitors)

    for _ in range(2):
        first_won = input("czy pierwszy zawodnik wygrał? ")
        first_won = True if first_won == "tak" else False
        match.make_match(first_won)

    final_necessary = match.check_if_next_round_necessary()

    if final_necessary:
        first_won = input("FINAł: czy pierwszy zawodnik wygrał? ")
        first_won = True if first_won == "tak" else False
        match.final.make_match(first_won)

    results = match.get_places()

    print(results[0][0].name, results[0][0].wins)
    print(results[1][0].name, results[1][0].wins)