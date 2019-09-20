from src.Bottle import Bottle



class Node:

    def __init__(self, identity, father_node, bottle1, bottle2, bottle3):
        self.bottles_quantity = [bottle1.getCurrentQuantity(), bottle2.getCurrentQuantity(), bottle3.getCurrentQuantity()]
        self.bottles_capacity = [bottle1.getCapacity, bottle2.getCapacity, bottle3.getCapacity]     # não sei se irá usar
        self.id = identity
        self.father = father_node
        self.children = []
        self.rule = 0

    def fillBottles(self, bottle1, bottle2, bottle3):
        bottle1.setCurrentQuantity(self.bottles_quantity[0])
        bottle2.setCurrentQuantity(self.bottles_quantity[1])
        bottle3.setCurrentQuantity(self.bottles_quantity[2])

    def add_child(self, child):
        self.children.append(child)

    def show_information(self):
        print(self.bottles_quantity)
        for child in self.children:
            child.show_information()

    def set_rule(self, rule1):
        self.rule = rule1

    def get_rule(self):
        return self.rule

    def increase_rule(self):
        self.rule = self.rule + 1

    def get_bottles_quantity(self):
        return self.bottles_quantity

    def get_father(self):
        return self.father