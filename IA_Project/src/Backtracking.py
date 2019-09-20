from src.Node import Node
from src.Bottle import Bottle

class Backtracking:

    def __init__(self, bottle1, bottle2, bottle3):
        self.bottles = [bottle1, bottle2, bottle3]
        self.id = 1
        self.root_node = Node(0, None, bottle1, bottle2, bottle3)

    def start(self):
        self.sucess = False
        node = self.root_node

        while(self.sucess != True):

            # Quando se chega no estado de sucesso
            if(self.bottles[0].getCurrentQuantity() == 4 and self.bottles[1].getCurrentQuantity() == 4 and self.bottles[2].getCurrentQuantity() == 0):
                self.sucess = True
                break

            elif(self.bottles[0].transfer(self.bottles[1]) != 0):
                new_node = Node(self.id, node, self.bottles[0], self.bottles[1], self.bottles[2])
                node.add_child(new_node)

        if self.sucess == True:
            print("DEU")



