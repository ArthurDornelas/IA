from src.Bottle import Bottle

class Node:

    def __init__(self, identity, father_node, bottle1, bottle2, bottle3):
        self.bottleQuantity = [bottle1.getCurrentQuantity, bottle2.getCurrentQuantity, bottle3.getCurrentQuantity]
        self.bottleCapacity = [bottle1.getCapacity, bottle2.getCapacity, bottle3.getCapacity]     # não sei se irá usar
        self.id = identity
        self.father = father_node
        self.children = []

    def fillBottles(self, bottle1, bottle2, bottle3):
        bottle1.setCurrentQuantity(self.bottleQuantity[0])
        bottle2.setCurrentQuantity(self.bottleQuantity[1])
        bottle3.setCurrentQuantity(self.bottleQuantity[2])

    def add_child(self, child):
        self.children.append(child)



