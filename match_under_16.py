from club_competitor import ClubCompetotor
from personal_competitor import PersonalCompetitor
from tree_node import Node


class Eliminations:
    def __init__(self, competitors):
        # first match is the first node on the lvl 3
        self.actualMatchId = 8
        self.tree = [Node() for x in range(0, 16)]
        self.tree = self.tree + [Node(competitor=competitors[x]) for x in range(0, 16)]
        # giving children to all nodes in tree
        for ids, node in enumerate(self.tree[1:16]):
            node.set_left_child(self.tree[(ids + 1) * 2])
            node.set_right_child(self.tree[(ids + 1) * 2 + 1])

    """" This function is returning id of next match node in tree"""

    def get_next_match_id(self):
        if 8 <= self.actualMatchId < 15 or 4 <= self.actualMatchId < 7 or 2 <= self.actualMatchId < 3:
            return self.actualMatchId + 1
        if self.actualMatchId == 15:
            return 4
        if self.actualMatchId == 7:
            return 2
        if self.actualMatchId == 3:
            return "REPASARZE"

    """" This function is returning id of previous match node in tree"""

    def get_prev_match_id(self):
        if 8 < self.actualMatchId <= 15 or 4 < self.actualMatchId <= 7 or 2 < self.actualMatchId <= 3:
            return self.actualMatchId - 1
        if self.actualMatchId == 2:
            return 7
        if self.actualMatchId == 4:
            return 15
        if self.actualMatchId == 8:
            return "To Pierwsza runda"

    """"
    This function is making match in actual node, winner competitor 
    from children will be rewritten to actual node competitor
    """
    def make_match(self, left_child_win):
        actual_match = self.tree[self.actualMatchId]
        actual_match.left_child_win() if left_child_win else actual_match.right_child_win()

    def go_to_next_round(self):
        pass

    def get_repassage_squad(self):
        repassage_squad = []

        def recurrent_repassage_getter(depth, actual_node):
            if 1 < depth <= 4:
                if actual_node.competitor == actual_node.get_left_child():
                    repassage_squad.append(actual_node.get_right_child().get_competitor())
                else:
                    repassage_squad.append(actual_node.get_left_child().get_competitor())
            if depth == 1:
                recurrent_repassage_getter(depth + 1, actual_node.get_left_child())
                recurrent_repassage_getter(depth + 1, actual_node.get_right_child())
            if depth == 2:
                recurrent_repassage_getter(depth + 1, actual_node.get_left_child())
                recurrent_repassage_getter(depth + 1, actual_node.get_right_child())
            if depth == 3:
                if actual_node.competitor == actual_node.get_left_child().competitor:
                    recurrent_repassage_getter(depth + 1, actual_node.get_left_child())
                else:
                    recurrent_repassage_getter(depth + 1, actual_node.get_right_child())

        recurrent_repassage_getter(1, self.tree[1])
        return repassage_squad

    def print_actual_match(self):
        print("Aktualne Id: ", self.actualMatchId)
        print("zawodnik I:",
              self.tree[self.actualMatchId].get_left_child().competitor.custom_string_repr(1, 0, 0, 0, 0))
        print("zawodnik II:",
              self.tree[self.actualMatchId].get_right_child().competitor.custom_string_repr(1, 0, 0, 0, 0))


if __name__ == "__main__":
    zawodnicy = [PersonalCompetitor(name="Kuba" + str(x)) for x in range(0, 16)]
    match = Eliminations(zawodnicy)
    while match.actualMatchId != "REPASARZE":
        match.print_actual_match()
        bool = input("czy pierwszy zawodnik wygrał? ")
        bool = True if bool == "tak" else False
        match.make_match(bool)
        match.actualMatchId = match.get_next_match_id()

    repassage = match.get_repassage_squad()
    for i in repassage:
        print(i.custom_string_repr(1, 0, 0, 0, 0))
