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
        print("ID z eliminacji:", self.actualMatchId)
        actual_match = self.tree[self.actualMatchId]
        actual_match.left_child_win() if left_child_win else actual_match.right_child_win()
        # testowo
        # if self.actualMatchId != 1:
        #     self.actualMatchId = self.get_next_match_id()

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
        self.tree = [Node() for x in range(0, 16)]
        for ids, node in enumerate(self.tree[1:8]):
            node.set_left_child(self.tree[(ids + 1) * 2])
            node.set_right_child(self.tree[(ids + 1) * 2 + 1])
        for competitor, node in zip(competitors[1:5] + competitors[6:], self.tree[8:]):
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
        self.bronzeFights = []
        # in this array we will be having places of all competitors
        self.results = []
        # eliminations matches (with half finals) [1,14], repechages [15,20], finals (with bronzes) [21,22,23]
        self.actualMatchId = 1

    def make_match(self, left_win):
        print(self.actualMatchId)
        if 1 <= self.actualMatchId <= 14:
            self.eliminations.make_match(left_win)
            self.go_to_next_mach()

        elif 15 <= self.actualMatchId <= 20:
            print("repasarze")
            self.repechage.make_match(left_win)
            self.go_to_next_mach()
        elif self.actualMatchId in [21, 22]:
            self.bronzeFights[self.actualMatchId - 21].make_match(left_win)
            self.go_to_next_mach()
        else:
            self.eliminations.go_to_next_round()
            print("Finały")
            self.eliminations.make_match(left_win)
            # print(self.eliminations.tree[1].get_competitor())
            print(self.eliminations.tree[1].get_competitor().get_name())
            self.get_places()

    def go_to_next_mach(self):
        if 1 <= self.actualMatchId <= 13:
            self.eliminations.go_to_next_round()
            self.actualMatchId += 1
        elif self.actualMatchId == 14:
            competitors = self.eliminations.get_repassage_squad()
            self.repechage = Repechage(competitors)
            self.actualMatchId += 1
        elif 15 <= self.actualMatchId <= 19:
            self.repechage.go_to_next_round()
            self.actualMatchId += 1
        elif self.actualMatchId == 20:
            tmp = Node()
            tmp.set_left_child(self.repechage.halfFinalist[0])
            tmp.set_right_child(self.repechage.tree[2].get_competitor())
            self.bronzeFights.append(tmp)
            tmp = Node()
            tmp.set_left_child(self.repechage.halfFinalist[1])
            tmp.set_right_child(self.repechage.tree[3].get_competitor())
            self.bronzeFights.append(tmp)
            self.actualMatchId += 1
        elif self.actualMatchId in [21, 22]:
            self.actualMatchId += 1

    def go_to_prev_round(self):
        pass  # TO DO

    def get_actual_match_id(self):
        return self.actualMatchId

    def get_eliminations(self):
        return self.eliminations

    def get_repechage(self):
        return self.repechage

    def get_places(self):
        results = []
        last_place = []
        prev_last = []
        seventh_place = []
        fifth_place = []
        third_place = []
        first_place = []
        second_place = []

        all_competitors = [x.get_competitor() for x in self.eliminations.tree[16:]]
        repasage_competitors = [x.get_competitor() for x in self.repechage.tree[8:]]
        finalists = [x.get_competitor() for x in self.eliminations.tree[4:8]]
        for x in all_competitors:
            if x not in repasage_competitors + finalists:
                last_place.append(x)
                print("losser ", x.get_name())

        for x in [x.get_competitor() for x in self.repechage.tree[8:]]:
            if x not in [x.get_competitor() for x in self.repechage.tree[4:8]]:
                prev_last.append(x)
                print("losser ", x.get_name())

        for x in [x.get_competitor() for x in self.repechage.tree[4:8]]:
            if x not in [x.get_competitor() for x in self.repechage.tree[2:4]]:
                seventh_place.append(x)
                print("losser ", x.get_name())

        fifth_place.append(
            self.bronzeFights[0].get_left_child() if self.bronzeFights[0].get_left_child() != self.bronzeFights[
                0].get_competitor else self.bronzeFights[0].get_right_child())
        fifth_place.append(
            self.bronzeFights[1].get_left_child() if self.bronzeFights[1].get_left_child() != self.bronzeFights[
                1].get_competitor else self.bronzeFights[1].get_right_child())

        third_place.append(
            self.bronzeFights[0].get_left_child() if self.bronzeFights[0].get_left_child() == self.bronzeFights[
                0].get_competitor else self.bronzeFights[0].get_right_child())
        third_place.append(
            self.bronzeFights[1].get_left_child() if self.bronzeFights[1].get_left_child() == self.bronzeFights[
                1].get_competitor else self.bronzeFights[1].get_right_child())
        first_place.append(self.eliminations.tree[1].get_competitor())
        second_place.append(self.eliminations.tree[1].get_left_child().get_competitor() if self.eliminations.tree[
                                                                                               1].get_left_child().get_competitor() !=
                                                                                           first_place[0] else
                            self.eliminations.tree[1].get_right_child().get_competitor())

        results.append(first_place)
        results.append(second_place)
        results.append(third_place)
        results.append(fifth_place)
        results.append(seventh_place)
        results.append(prev_last)
        results.append(last_place)
        print("_________________________________________________________________")
        for id, x in enumerate(results):
            print(id)
            for comp in x:
                print(comp.get_name())


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
