from abstractMatchesMaker import AbstractMatchesMaker
from enum import Enum
from match_under_16 import MatchUnder16
from match_under_5 import MatchUnder5Wrapper
from Program_GUI.functionality.GUI_manipulation import *


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

    def __init__(self, competitors):
        self.competitors = competitors
        self.match_type = correctTypeFromLength(len(self.competitors))
        self.engine = None
        if self.match_type == TypeOFMatch.Under16:
            self.engine = MatchUnder16(self.competitors)
        elif self.match_type == TypeOFMatch.Under5:
            self.engine = MatchUnder5Wrapper(self.competitors)

    def make_match(self, left_win):
        self.engine.make_match(left_win)

    def go_to_next_round(self):
        self.engine.go_to_next_round()

    def go_to_prev_round(self):
        self.engine.go_to_prev_round()

    def get_actual_match_id(self):
        self.engine.get_actual_match_id()

    def print_fighters(self, window):
        competitors = self.engine.get_actual_fighters()
        print_actual_competitors(*competitors,window)

    def print_match(self, window):
        if self.match_type == TypeOFMatch.Under16:
            print_match_under_16(self.engine, window)
            self.print_fighters(window)
        elif self.match_type == TypeOFMatch.Under5:
            print_match_under_5_wrapper(self.engine, window)


if __name__ == '__main__':
    for i in range(2, 34):
        print(i, correctTypeFromLength(i))
