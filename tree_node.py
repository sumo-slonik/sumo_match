class Node:

    def __init__(self, competitor=None, left_child=None, right_child=None):
        self.right_child = right_child
        self.left_child = left_child
        self.competitor = competitor
        self.points = None

    def make_match(self,left_child_win):
        if left_child_win:
            self.competitor = self.left_child
        else:
            self.competitor = self.right_child

