from src.Bottle import Bottle

class Node:

    def __init__(self, bottle1, bottle2, bottle3):
        self.bottle_1 = bottle1
        self.bottle_2 = bottle2
        self.bottle_3 = bottle3

    def fillBottles(self, bottle1, bottle2, bottle3):
        bottle1.setCurrentQuantity(self.bottle_1)
        bottle2.setCurrentQuantity(self.bottle_2)
        bottle3.setCurrentQuantity(self.bottle_3)



