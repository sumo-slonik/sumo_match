from club_competitor import ClubCompetotor
from personal_competitor import PersonalCompetitor
from tree_node import Node
from copy import deepcopy


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
            for i in self.get_repassage_squad():
                print(i)
            # return "REPASARZE"
            return 1

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
        # testowo
        if self.actualMatchId!=1:
            self.actualMatchId = self.get_next_match_id()

    def go_to_next_round(self):
        # TO DO: BRAKE RULES
        self.chek_free_fight()
        self.actualMatchId = self.get_next_match_id()

    def go_to_prev_round(self):
        # TO DO: BRAKE RULES
        self.chek_free_fight()
        self.actualMatchId = self.get_prev_match_id()

    def get_repassage_squad(self):
        repassage_squad = []

        def recurrent_repassage_getter(depth, actual_node):
            if 1 < depth <= 4:
                if actual_node.competitor == actual_node.get_left_child().get_competitor():
                    repassage_squad.append(actual_node.get_right_child().get_competitor())
                else:
                    repassage_squad.append(actual_node.get_left_child().get_competitor())
            if depth in [1, 2]:
                recurrent_repassage_getter(depth + 1, actual_node.get_left_child())
                recurrent_repassage_getter(depth + 1, actual_node.get_right_child())
            if depth == 3:
                if actual_node.competitor == actual_node.get_left_child().get_competitor():
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

    def get_actual_match_id(self):
        return self.actualMatchId

    def get_actual_node(self):
        return self.tree[self.actualMatchId]

    def chek_free_fight(self):
        if self.get_actual_node().get_left_child().get_competitor().get_is_free_fight():
            self.make_match(False)
            return True
        if self.get_actual_node().get_right_child().get_competitor().get_is_free_fight():
            self.make_match(True)
            return True
        return False


# to do dodać klasę po której będzie dziedziczył repasarz i elimiations bo są dość podobne

class Repechage:
    def __init__(self, competitors):

        # get half finalist from competitors list
        self.halfFinalist = [competitors[0]] + [competitors[5]]
        self.actualMatchId = 4
        # build tree for with repechages
        self.tree = [] + [Node() for x in range(0, 16)]
        for ids, node in enumerate(self.tree[1:8]):
            node.set_left_child(self.tree[(ids + 1) * 2])
            node.set_right_child(self.tree[(ids + 1) * 2 + 1])
        for competitor, node in zip(competitors[1:5] + competitors[5:], self.tree):
            node.set_competitor(competitor)

    def get_next_match_id(self):
        if 4 <= self.actualMatchId < 7 or 2 <= self.actualMatchId < 3:
            return self.actualMatchId + 1
        if self.actualMatchId == 7:
            return 2
        if self.actualMatchId == 3:
            return "Finały"

    def get_prev_match_id(self):
        if 4 < self.actualMatchId <= 7 or 2 < self.actualMatchId <= 3:
            return self.actualMatchId - 1
        if self.actualMatchId == 2:
            return 7
        if self.actualMatchId == 4:
            return "To Pierwsza runda"

    def go_to_next_round(self):
        # TO DO: BRAKE RULES
        self.chek_free_fight()
        self.actualMatchId = self.get_next_match_id()

    def go_to_prev_round(self):
        # TO DO: BRAKE RULES
        self.chek_free_fight()
        self.actualMatchId = self.get_prev_match_id()

    def get_bronze_finalist(self):
        return (self.halfFinalist[1], self.tree[2]), (self.halfFinalist[0], self.tree[3])

    def chek_free_fight(self):
        if self.get_actual_node().get_left_child().get_competitor().get_is_free_fight():
            self.make_match(False)
            return True
        if self.get_actual_node().get_right_child().get_competitor().get_is_free_fight():
            self.make_match(True)
            return True
        return False

    def get_actual_match_id(self):
        return self.actualMatchId

    def get_actual_node(self):
        return self.tree[self.actualMatchId]

    def make_match(self, left_child_win):
        actual_match = self.tree[self.actualMatchId]
        actual_match.left_child_win() if left_child_win else actual_match.right_child_win()


class MatchUnder16:
    def __init__(self, competitors):
        self.eliminations = Eliminations(competitors)
        # we will get repechages after playing eliminations
        self.repechage = None
        # and we will get finals after playing repechages and eliminations
        self.finalist = []
        # in this array we will be having places of all competitors
        self.results = []
        # eliminations matches (with half finals) [1,14], repechages [15,20], finals (with bronzes) [21,22,23]
        self.actualMatchId = 1

    def make_match(self, left_win):
        if 1 <= self.actualMatchId <= 14:
            self.eliminations.make_match(left_win)
        elif 15 <= self.repechage.actualMatchId <= 20:
            self.repechage.make_match(left_win)
        # To do add repasages and finals

    def go_to_next_mach(self):
        if 1 <= self.actualMatchId <= 13:
            self.eliminations.go_to_next_round()
            self.actualMatchId += 1
        if self.actualMatchId == 14:
            competitors = self.eliminations.get_repassage_squad()
            self.repechage = Repechage(competitors)
            self.actualMatchId += 1
        if 15 <= self.actualMatchId <= 19:
            self.repechage.go_to_next_round()
            self.actualMatchId += 1
        if self.actualMatchId == 20:
            self.finalist = {}
            tmp = (self.eliminations.tree[2].get_competitor(), self.eliminations.tree[3].get_competitor())
            self.finalist["Final"] = tmp[:]
            tmp = (self.repechage.halfFinalist[0], self.repechage.tree[2].get_competitor())
            self.finalist["Bronze_I"] = tmp[:]
            tmp = (self.repechage.halfFinalist[1], self.repechage.tree[3].get_competitor())
            self.finalist["Bronze_I"] = tmp[:]
            self.actualMatchId += 1


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
