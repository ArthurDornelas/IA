from src.Node import Node
from src.Bottle import Bottle

"""
Regras:
1) Transferir bottle1 -> bottle2
2) Transferir bottle1 -> bottle3
3) Transferir bottle2 -> bottle1
4) Transferir bottle2 -> bottle3
5) Transferir bottle3 -> bottle1
6) Transferir bottle3 -> bottle2

Ordem de aplicação de regras: crescente
"""


class Largura:
    def __init__(self, bottle1, bottle2, bottle3):
        self.bottles = [bottle1, bottle2, bottle3]
        self.id = 1
        self.root_node = Node(0, None, bottle1, bottle2, bottle3)
        self.abertos = []
        self.fechados = []

    def start(self):
        fail = False
        success = False
        self.abertos.append(self.root_node)
        rules = [self.rule_1, self.rule_2, self.rule_3, self.rule_4, self.rule_5, self.rule_6]
        while fail == False and success == False:
            if len(self.abertos) < 1:
                fail = True
            else:
                #print("Entro primeiro else")
                node = self.abertos.pop(0)
                node.show_information()
                #print("{}".format(node.id))
                node.fillBottles(self.bottles[0], self.bottles[1], self.bottles[2])
                if self.is_success(node):
                    success = True
                else:
                    current_rule = 0
                    while current_rule < 6:
                        if rules[current_rule]():
                            new_node = Node(self.id, node, self.bottles[0], self.bottles[1], self.bottles[2])
                            node.add_child(new_node)
                            self.id = self.id + 1
                            self.abertos.append(new_node)
                            current_rule = current_rule + 1
                            node.fillBottles(self.bottles[0], self.bottles[1], self.bottles[2])
                        else:
                            current_rule = current_rule + 1
                    self.fechados.append(node)

    def rule_1(self):
        return self.bottles[0].transfer(self.bottles[1])

    def rule_2(self):
        return self.bottles[0].transfer(self.bottles[2])

    def rule_3(self):
        return self.bottles[1].transfer(self.bottles[0])

    def rule_4(self):
        return self.bottles[1].transfer(self.bottles[2])

    def rule_5(self):
        return self.bottles[2].transfer(self.bottles[0])

    def rule_6(self):
        return self.bottles[2].transfer(self.bottles[1])

    @staticmethod
    def is_success(node):
        node_quantity = node.get_bottles_quantity()
        if (node_quantity[0] == 4 and node_quantity[1] == 4 and node_quantity[2] == 0):
            return True
        return False
