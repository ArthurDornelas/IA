from src.Node import Node
from src.Bottle import Bottle

'''
Regras:
1) Transferir bottle1 -> bottle2
2) Transferir bottle1 -> bottle3
3) Transferir bottle2 -> bottle1
4) Transferir bottle2 -> bottle3
5) Transferir bottle3 -> bottle1
6) Transferir bottle3 -> bottle2

Ordem de aplicação de regras: crescente
'''

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

    def ordem_crescente(self):
        print(1)

    def regra1(self):
        self.bottles[0].transfer(self.bottles[1])

    def regra2(self):
        self.bottles[0].transfer(self.bottles[2])

    def regra3(self):
        self.bottles[1].transfer(self.bottles[0])

    def regra4(self):
        self.bottles[1].transfer(self.bottles[2])

    def regra5(self):
        self.bottles[2].transfer(self.bottles[0])

    def regra6(self):
        self.bottles[2].transfer(self.bottles[1])

    def sucess(self, node):
        node_quantity = node.get_bottles_quantity()
        if(node_quantity[0] == 4 and node_quantity[1] == 4 and node_quantity[2] == 0):
            return True
        return False
