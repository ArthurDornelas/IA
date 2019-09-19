from src.Node import Node


class Backtracking:

    def __init__(self, bottle1, bottle2, bottle3):
        self.bottles = [bottle1, bottle2, bottle3]
        self.id = 1
        self.root_node = Node(0, None, bottle1, bottle2, bottle3)

    def start(self):
        print('oi')
