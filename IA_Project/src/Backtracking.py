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
        self.caminho = []

    def start(self):
        node = self.root_node
        print('teste')
        #node.show_information()
        print('testee')
        rules = [self.rule_1, self.rule_2, self.rule_3, self.rule_4, self.rule_5, self.rule_6]
        while node is not None and self.is_success(node) != True:
            current_rule = node.get_rule()
            node.show_information()
            print("regra atual: {}".format(current_rule))
            if current_rule < 6 and rules[current_rule]():
                print("aplicou regra")
                node.increase_rule()
                current_bottle_quantity = [self.bottles[0].getCurrentQuantity(), self.bottles[1].getCurrentQuantity(),
                                           self.bottles[2].getCurrentQuantity()]
                print("caminho: {}  :  {}".format(self.caminho, current_bottle_quantity))
                if current_bottle_quantity not in self.caminho:
                    print("cria novo no filho")
                    self.caminho.append(node.get_bottles_quantity())
                    new_node = Node(self.id, node, self.bottles[0], self.bottles[1], self.bottles[2])
                    node.add_child(new_node)
                    node = new_node
                    self.id = self.id + 1
                #node.fillBottles(self.bottles[0], self.bottles[1], self.bottles[2])
            elif current_rule < 6:
                print("nao aplicou a regra")
                node.increase_rule()
            else:
                print("Else")
                node = node.get_father()
        print("acabou")
            # Quando se chega no estado de sucesso
            # if(self.is_success(node)):
            #     self.sucess = True
            #     break
            #
            # elif(self.rule_1() == 1 ):
            #     new_node = Node(self.id, node, self.bottles[0], self.bottles[1], self.bottles[2])
            #     node.add_child(new_node)
            #     node = new_node
            #
            # elif(self.rule_2() == 1 ):
            #     new_node = Node(self.id, node, self.bottles[0], self.bottles[1], self.bottles[2])
            #     node.add_child(new_node)
            #     node = new_node
            #
            # elif(self.rule_3() == 1 ):
            #     new_node = Node(self.id, node, self.bottles[0], self.bottles[1], self.bottles[2])
            #     node.add_child(new_node)
            #     node = new_node
            #
            # elif (self.rule_4() == 1 ):
            #     new_node = Node(self.id, node, self.bottles[0], self.bottles[1], self.bottles[2])
            #     node.add_child(new_node)
            #     node = new_node
            #
            # elif (self.rule_5() == 1 ):
            #     new_node = Node(self.id, node, self.bottles[0], self.bottles[1], self.bottles[2])
            #     node.add_child(new_node)
            #     node = new_node
            #
            # elif (self.rule_6() == 1 ):
            #     new_node = Node(self.id, node, self.bottles[0], self.bottles[1], self.bottles[2])
            #     node.add_child(new_node)
            #     node = new_node
            #
            # else:
            #     node = node.father()


    def ordem_crescente(self):
        print(1)

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
        #node.show_information()
        node_quantity = node.get_bottles_quantity()
        if(node_quantity[0] == 4 and node_quantity[1] == 4 and node_quantity[2] == 0):
            return True
        return False

    def show_information(self):
        self.root_node.show_information()


