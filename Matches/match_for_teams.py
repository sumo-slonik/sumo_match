from abc import ABC
from DataStructures.tree_node import Node as Match
from DataStructures.club_competitor import ClubCompetitor
from DataStructures.personal_competitor import PersonalCompetitor
from random import choice

from Matches.abstractMatchesMaker import AbstractMatchesMaker


class TeamMatch(AbstractMatchesMaker, ABC):

    def __init__(self, team1, team2):
        self.team1 = team1
        self.team2 = team2
        self.team1_selected_competitor = None
        self.team2_selected_competitor = None
        self.actual_match_id = 0
        self.rounds = [Match() for _ in range(3)]
        self.score = [0, 0]
        self.is_end = False
        for single_round, first, second in zip(self.rounds, self.team1.get_competitors_list()[:-1],
                                               self.team2.get_competitors_list()[:-1]):
            single_round.set_left_child(first)
            single_round.set_right_child(second)

    def make_match(self, win_left):
        if not self.is_end:
            if win_left:
                self.score[0] += 1
            else:
                self.score[1] += 1

            self.rounds[self.actual_match_id].make_match(win_left)
            self.print_actual_match()
            self.go_to_next_round()

    def go_to_next_round(self):
        if self.actual_match_id < 2:
            self.actual_match_id += 1
        else:
            self.is_end = True

    def use_substitute(self,in_left):
        pass

    def go_to_prev_round(self):
        if self.actual_match_id > 0:
            self.actual_match_id -= 1

    def get_actual_match_id(self):
        return self.actual_match_id

    def print_actual_match(self):
        print("Pierwszy zawodnik", self.rounds[self.get_actual_match_id()].get_left_child())
        print("Drugi zawodnik", self.rounds[self.get_actual_match_id()].get_right_child())
        print("Zwycięzca", self.rounds[self.get_actual_match_id()].get_competitor())
        print('__________________________________________________')


if __name__ == '__main__':
    marciny = [PersonalCompetitor("Marcin Warchoł" + str(x)) for x in range(4)]
    kuby = [PersonalCompetitor("Kuba Nowakowski" + str(x)) for x in range(4)]

    team_1 = ClubCompetitor(*marciny, "marciny")
    team_2 = ClubCompetitor(*kuby, "kuby")

    match = TeamMatch(team_1, team_2)
    states = [True, False]
    for i in range(3):
        res = choice(states)
        print(res)
        match.make_match(res)
