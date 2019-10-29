class Node:

    def __init__(self, id, actual_cost, heurist_cost):
        self.id = id
        self.actual_cost = actual_cost
        self.heuristic_cost = heurist_cost
        self.father = None
        self.edges = []

    def get_id(self):
        return self.id

    def set_id(self, id):
        self.id = id

    def set_position(self, position):
        self.position = position

    def get_position(self):
        return self.position

    def add_edge(self, edge):
        self.edges.append(edge)

    def get_edges(self):
        return self.edges

    def get_father(self):
        return self.father

    def set_father(self, father_node):
        self.father = father_node