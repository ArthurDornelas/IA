from src.Node import Node
from src.Edge import Edge
import csv


class Maze:

    def __init__(self):
        self.start = None
        self.ending = None
        self.counter = 2
        self.maze = []
        self.width = 0
        self.height = 0
        self.file_path = file_path

    def add_node(self, id1, heuristic_cost, actual_cost):
        no = Node(id1, actual_cost, heuristic_cost)

    def add_edge_and_nodes(self, id1, id2, heuristic_cost_1, heuristic_cost_2, actual_cost_1, actual_cost_2, edge_cost):
        no = Node(id1, heuristic_cost_1, actual_cost_1)
        no2 = Node(id2, heuristic_cost_2, actual_cost_2)
        edge = Edge(edge_cost)
        no.add_edge(no2,cost)
        no.add_edge(no,cost)


    def create_maze(self):


    def get_start(self):
        return self.start

    def get_ending(self):
        return self.ending
