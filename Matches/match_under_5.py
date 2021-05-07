from abc import ABC
from DataStructures.personal_competitor import *
from DataStructures.tree_node import Node as Match
from Matches.abstractMatchesMaker import AbstractMatchesMaker
from random import choice
from Matches.match_under_4 import MatchUnder4
from Matches.match_under_3 import MatchUnder3


class MatchUnder5(AbstractMatchesMaker):

    def __init__(self, competitors):
        self.competitors = competitors[:]
        self.matches = [Match() for _ in range(10)]
        self.actualMatchId = 0
        self.is_end = False

        # in the documents directory there is
        # a visualisation of the players' order, the player
        # number in matches is an index in the competitors table increased by one
        self.__matchOrder = [(1, 2), (3, 4), (1, 3), (2, 5), (1, 4), (3, 5), (1, 5), (2, 4), (2, 3), (4, 5)]
        for competitors_id, match in zip(self.__matchOrder, self.matches):
            print(competitors_id, match)
            match.set_left_child(self.competitors[competitors_id[0] - 1])
            match.set_right_child(self.competitors[competitors_id[1] - 1])

    def make_match(self, left_win):
        self.matches[self.actualMatchId].make_match(left_win)
        self.print_actual_match()
        if self.actualMatchId == 9:
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


class MatchUnder5Wrapper:
    def __init__(self, competitors):
        self.rounds = 0
        self.results = []
        self.losers = []
        self.is_end = False
        self.actual_state = len(competitors)
        self.competitors = competitors[:]
        if self.actual_state == 5:
            self.engine = MatchUnder5(competitors)
        if self.actual_state == 4:
            self.engine = MatchUnder4(competitors)
        if self.actual_state == 3:
            self.engine = MatchUnder3(competitors)

    def check_if_two_competitors_get_the_same_result(self):
        if len(self.competitors) == 2 or (
                len(self.competitors) >= 3 and self.competitors[0].get_wins() == self.competitors[1].get_wins() !=
                self.competitors[2].get_wins()):
            for match in self.engine.matches:
                if (match.left_child == self.competitors[0] and match.right_child == self.competitors[1]) or (
                        match.left_child == self.competitors[1] and match.right_child == self.competitors[0]):
                    if match.competitor == self.competitors[0]:
                        self.results.append(self.competitors[0])
                        self.results.append(self.competitors[1])
                    else:
                        self.results.append(self.competitors[1])
                        self.results.append(self.competitors[0])
                    print("dwaj z tym samym rezultatem",self.competitors[1].name, self.competitors[0].name)
            del self.competitors[0]
            del self.competitors[0]

    def get_bests_competitors_to_results(self):
        while len(self.competitors) > 1 and self.competitors[0].get_wins() != self.competitors[1].get_wins():
            self.results.append(self.competitors[0])
            del self.competitors[0]
        if len(self.competitors) == 1:
            self.results.append(self.competitors[0])
            del self.competitors[0]

    def make_match(self, left_wins):
        print("______________________")
        print("______________________")
        self.rounds += 1
        print("round number", self.rounds)
        # for i in self.competitors:
        #     print(i.name, i.get_wins())
        print("______________________")
        print("______________________")
        if not self.is_end:
            if not self.engine.is_end:
                self.engine.make_match(left_wins)
                if self.engine.is_end:
                    # here we deleting person with the best results
                    # and we adding this person to our results list
                    # only when  we have only one person with the best result
                    # and all is clear
                    self.get_bests_competitors_to_results()
                    # not clear situation
                    if self.competitors:
                        # we only have two best results
                        self.check_if_two_competitors_get_the_same_result()
                        self.get_bests_competitors_to_results()
                        self.check_if_two_competitors_get_the_same_result()
                        self.get_bests_competitors_to_results()
                        # we have more than two competitors with the same result
                        if self.competitors:
                            max_points = self.competitors[0].get_wins()
                            to_rematch = []
                            for i in range(len(self.competitors)):
                                if self.competitors[i].get_wins() == max_points:
                                    # print(i)
                                    to_rematch.append(self.competitors[i])
                            # for i in to_rematch:
                            #     print(i.name)
                            for to_del in to_rematch:
                                print(to_del.name)
                                self.competitors.remove(to_del)

                            new_losers = self.competitors
                            self.losers = new_losers + self.losers
                            self.competitors = to_rematch
                            self.actual_state = len(self.competitors)
                            if self.actual_state == 5:
                                self.engine = MatchUnder5(self.competitors)
                            if self.actual_state == 4:
                                self.engine = MatchUnder4(self.competitors)
                            if self.actual_state == 3:
                                print("tutaj weszło")
                                self.engine = MatchUnder3(self.competitors)
                    else:
                        self.results = self.results + self.losers
                        self.is_end = True


if __name__ == '__main__':

    Competitors = [PersonalCompetitor("Kuba " + str(x)) for x in range(5)]
    for i in range (100):
        matches = MatchUnder5Wrapper(Competitors)

        while not matches.is_end:
            result = choice([True, False])
            print("Left Win:", result)
            matches.make_match(result)

        print("                                                                  len:",len(matches.results))
