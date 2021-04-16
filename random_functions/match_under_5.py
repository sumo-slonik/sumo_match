from personal_competitor import *
from tree_node import Node as Match
class Under5:

    def __init__(self,competitors):
        self.competitors = competitors
        self.matches = [Match() for _ in range(10)]
        

