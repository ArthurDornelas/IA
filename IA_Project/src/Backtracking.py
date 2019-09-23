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


class Backtracking:

    def __init__(self, bottle1, bottle2, bottle3):
        self.bottles = [bottle1, bottle2, bottle3]
        self.id = 1
        self.root_node = Node(0, None, bottle1, bottle2, bottle3)
        self.path = []

    def start(self):
        node = self.root_node
        self.path.append(node.get_bottles_quantity())
        rules = [self.rule_1, self.rule_2, self.rule_3, self.rule_4, self.rule_5, self.rule_6]
        while node is not None and not self.is_success(node):
            current_rule = node.get_rule()
            if current_rule < 6 and rules[current_rule]():
                node.increase_rule()
                current_bottle_quantity = [self.bottles[0].getCurrentQuantity(),
                                           self.bottles[1].getCurrentQuantity(),
                                           self.bottles[2].getCurrentQuantity()]
                if current_bottle_quantity not in self.path:
                    new_node = Node(self.id, node, self.bottles[0], self.bottles[1], self.bottles[2])
                    self.path.append(current_bottle_quantity)
                    node.add_child(new_node)
                    node = new_node
                    self.id = self.id + 1
                else:
                    node.fillBottles(self.bottles[0], self.bottles[1], self.bottles[2])
            elif current_rule < 6:
                node.increase_rule()
            else:
                self.path.remove(node.get_bottles_quantity())
                node = node.get_father()
        self.show_success_path()
        self.show_level_success_path()
        self.print_tree()

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
        if node_quantity[0] == 4 and node_quantity[1] == 4 and node_quantity[2] == 0:
            return True
        return False

    def show_information(self):
        self.root_node.show_information()

    def show_success_path(self):
        print('Caminho do sucesso: {}'.format(self.path))

    def show_level_success_path(self):
        print("O nivel da solucao eh: {}".format(len(self.path) - 1))

    def print_tree(self):
        print("\n A arvore gerada eh: \n")
        i = 0
        while i < len(self.path):
            print("{}\n".format(self.path[i]))
            i += 1