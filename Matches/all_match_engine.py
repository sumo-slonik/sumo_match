from DataStructures.tree_node import Node
from Matches.abstractMatchesMaker import AbstractMatchesMaker
from enum import Enum

from Matches.match_under_10 import MatchUnder10
from Matches.match_under_16 import MatchUnder16
from Matches.match_under_5 import MatchUnder5Wrapper
from Program_GUI.functionality.GUI_manipulation import *
from DataStructures.club_competitor import ClubCompetitor
from Matches.match_for_teams import TeamMatch
from random_functions.random_function_16 import random_function_16


class TypeOFMatch(Enum):
    Under5 = 5
    Under10 = 10
    Under16 = 16
    Under32 = 32
    Under64 = 64


def correctTypeFromLength(length):
    if length == 2:
        return TypeOFMatch(2)
    if length <= 5:
        return TypeOFMatch(5)
    if length <= 10:  # (5,10]
        return TypeOFMatch(10)
    if length <= 16:  # (10,16]
        return TypeOFMatch(16)
    if length <= 32:  # (16,32]
        return TypeOFMatch(32)
    if length <= 64:
        return TypeOFMatch(64)


class AllMatchEngine(AbstractMatchesMaker):

    def __init__(self, competitors, window):
        self.competitors = competitors
        self.match_type = correctTypeFromLength(len(self.competitors))
        self.engine = None
        self.teamMatch = isinstance(competitors[0], ClubCompetitor)
        self.in_match = False
        self.teamEngine = None
        self.window = window
        if self.match_type == TypeOFMatch.Under16:
            if len(self.competitors) == 16:
                self.engine = MatchUnder16(self.competitors)
            else:
                print("trzeba wstawić wolne losy")
        elif self.match_type == TypeOFMatch.Under5:
            self.engine = MatchUnder5Wrapper(self.competitors)
        elif self.match_type == TypeOFMatch.Under10:
            self.engine = MatchUnder10(self.competitors)
        else:
            print("Nie mamy zaimplementowanegoe")
        self.print_match()

    def go_to_team_match(self):
        self.in_match = True
        change_match_buttons(self.window, True, True)
        first_competitor = self.engine.get_actual_match().get_left_child()
        second_competitor = self.engine.get_actual_match().get_right_child()
        first_competitor = first_competitor if not isinstance(first_competitor,
                                                              Node) else first_competitor.competitor
        second_competitor = second_competitor if not isinstance(second_competitor,
                                                                Node) else second_competitor.competitor

        print('_______________________________')
        print(first_competitor)
        print(second_competitor)
        print(type(first_competitor))
        print(type(second_competitor))
        print('_______________________________')
        self.teamEngine = TeamMatch(first_competitor, second_competitor)
        self.print_match()

    def go_to_all_matches(self):
        self.in_match = False
        change_match_buttons(self.window, True, False)
        if self.teamEngine.is_end:
            # if we done team match we can give results to all matches
            self.make_match(self.teamEngine.score[0] > 1)
        self.teamEngine = None
        self.print_match()

    def make_match(self, left_win):
        print('_____________________________________________________________________________________________________')
        if self.in_match:
            self.teamEngine.make_match(left_win)
        else:
            self.engine.make_match(left_win)

    def go_to_next_round(self):
        self.engine.go_to_next_round()

    def go_to_prev_round(self):
        self.engine.go_to_prev_round()

    def get_actual_match_id(self):
        self.engine.get_actual_match_id()

    def print_fighters(self):
        competitor1 = self.engine.get_actual_match().get_left_child()
        competitor2 = self.engine.get_actual_match().get_right_child()
        if isinstance(competitor1, Node):
            competitor1 = competitor1.get_competitor()
        if isinstance(competitor2, Node):
            competitor2 = competitor2.get_competitor()

        competitors = [competitor1, competitor2]
        print_actual_competitors(*competitors, self.window)

    def print_match(self):
        if self.in_match and self.teamMatch:
            print_team_match(self.teamEngine, self.window)
            change_match_buttons(self.window, True, True)
            if self.teamEngine.is_end:
                hide_wind_buttons(self.window, True)
        else:
            if self.match_type == TypeOFMatch.Under16:
                print_match_under_16(self.engine, self.window)
            elif self.match_type == TypeOFMatch.Under5:
                print_match_under_5_wrapper(self.engine, self.window)
            elif self.match_type == TypeOFMatch.Under10:
                print_match_under_10(self.engine, self.window)

            if self.teamMatch:
                change_match_buttons(self.window, True, False)
            else:
                change_match_buttons(self.window, False, False)
                hide_wind_buttons(self.window, False)
            self.print_fighters()

if __name__ == '__main__':
    for i in range(2, 34):
        print(i, correctTypeFromLength(i))
