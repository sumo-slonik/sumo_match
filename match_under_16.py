from club_competitor import ClubCompetotor
from personal_competitor import PersonalCompetitor
from tree_node import Node


class Eliminations:
    def __init__(self, competitors):
        # first match is the first node on the lvl 3
        self.actualMatchId = 8
        self.tree = [Node(competitor=competitors[x]) for x in range(0, 32)]
        self.tree = [] + self.tree
        # giving children to all nodes in tree
        for ids, node in enumerate(self.tree[1:]):
            node.set_left_child(self.tree[ids * 2])
            node.set_right_child(self.tree[ids * 2 + 1])

    """" This function is returning id of next match node in tree"""

    def get_next_match_id(self):
        result = self.actualMatchId
        if 8 <= self.actualMatchId < 15 or 4 <= self.actualMatchId < 7 or 2 <= self.actualMatchId < 3:
            result += 1
        if self.actualMatchId == 15:
            result = 4
        if self.actualMatchId == 7:
            result = 2
        if self.actualMatchId == 3:
            result = "REPASARZE"
        return result

    """" This function is returning id of previous match node in tree"""

    def get_prev_match_id(self):
        result = 0
        if 8 < self.actualMatchId <= 15 or 4 < self.actualMatchId <= 7 or 2 < self.actualMatchId <= 3:
            result -= 1
        if self.actualMatchId == 2:
            result = 7
        if self.actualMatchId == 4:
            result = 15
        if self.actualMatchId == 8:
            result = "To Pierwsza runda"
        return result

    def make_match(self, left_child_win):
        actual_match = self.tree[self.actualMatchId]
        actual_match.left_child_win() if left_child_win else actual_match.right_child_win()

    def go_to_next_round(self):
        pass

    def make_repassage_squad(self):
        repassage_squad = []

        def recurrent_repassage_getter(depth, actual_node):
            if 1 < depth <= 3:
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
