from node import Node
from random import random

class Connection:

    def __init__(self, node1, node2, weight = random()):
        super().__init__()
        self.weight = weight
        self.node1 = node1
        self.node2 = node2