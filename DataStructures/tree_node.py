from DataStructures import personal_competitor


class Node:
    def __init__(self, competitor=personal_competitor.PersonalCompetitor(), left_child=None, right_child=None):
        self.right_child = right_child
        self.left_child = left_child
        self.competitor = competitor
        self.points = None

    def make_match(self, left_child_win):
        if left_child_win:
            if isinstance(self.left_child, Node):
                self.competitor = self.left_child.competitor
            else:
                self.competitor = self.left_child
        else:
            if isinstance(self.right_child, Node):
                self.competitor = self.right_child.competitor
            else:
                self.competitor = self.right_child
        self.competitor.win()
        print(self.competitor.name, self.competitor.wins)

    def set_left_child(self, child):
        self.left_child = child

    def set_right_child(self, child):
        self.right_child = child

    def left_child_win(self):
        self.competitor = self.left_child.competitor

    def right_child_win(self):
        self.competitor = self.right_child.competitor

    def get_left_child(self):
        return self.left_child

    def get_right_child(self):
        return self.right_child

    def get_competitor(self):
        return self.competitor

    def set_competitor(self, competitor):
        self.competitor = competitor


if __name__ == "__main__":
    k = Node()
    k.set_left_child(None)
    b = k
    arr = [k]
    for i, node in enumerate(arr[:]):
        node.set_left_child(Node())
    print(type(b.get_left_child()))
    print(type(k.get_left_child()))
