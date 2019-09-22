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
from src.Node import Node


class BFS:

    def __init__(self, bottle1, bottle2, bottle3):
        self.bottles = [bottle1, bottle2, bottle3]
        self.root_node = Node(0, None, bottle1, bottle2, bottle3)
        self.id = 1
        self.openedList = []
        self.closedList = []
        self.success_way = []
        self.openedList.append(self.root_node)
        self.rules = [self.rule_1, self.rule_2, self.rule_3, self.rule_4, self.rule_5, self.rule_6]

    def start(self):
        success = False
        while len(self.openedList) != 0:
            print(self.openedList[0].get_bottles_quantity())
            node = self.openedList.pop(0)                                   # Pega o primeiro elemento da lista
            self.set_bottle_quantity(node.get_bottles_quantity())           # Coloca a quantidade do nó atual nos galões da classe
            if not self.is_success(node):
                current_rule = node.get_rule()
                while current_rule < 6:
                    if self.apply_rule(current_rule, node):                 # Se retornar True, cria novo nó
                        new_node = Node(self.id, node, self.bottles[0], self.bottles[1], self.bottles[2])
                        node.add_child(new_node)
                        self.openedList.append(new_node)
                    self.set_bottle_quantity(node.get_bottles_quantity())   # Coloca a quantidade do nó atual nos galões da classe
                    current_rule += 1
                self.closedList.append(node.get_bottles_quantity())         # Adiciona o nó atual na lista de fechados

            else:  #Construir caminho inverso
                aux_node = node
                while aux_node is not None:
                    self.success_way.append(aux_node.get_bottles_quantity())
                    aux_node = aux_node.get_father()
                success = True
                break
        if success:
            self.show_success_way()

    def set_bottle_quantity(self, current_quantity):
        for i in range(3):
            self.bottles[i].set_quantity(current_quantity[i])

    """ Função que faz tranferência entre galões se for possível transferir
    e se a nova quantidade não estiver no caminho do nó """
    def apply_rule(self, regra, node):
        new_bottle = self.bottles.copy()
        success = self.rules[regra](new_bottle)
        new_quantity = [new_bottle[0].getCurrentQuantity(),
                       new_bottle[1].getCurrentQuantity(),
                       new_bottle[2].getCurrentQuantity()]
        if success and not self.in_the_way(node, new_quantity):
            self.bottles = new_bottle
            return True
        return False

    """ Função que retorna True se o novo nó que se quer inserir já está na árvore """
    def in_the_way(self, current_node, new_node):
        aux_node = current_node
        while aux_node is not None:
            if aux_node.get_bottles_quantity() == new_node:
                return True
            aux_node = aux_node.get_father()
        return False

    """Funções que aplicam as regras"""
    def rule_1(self, new_bottle):
        return new_bottle[0].transfer(new_bottle[1])

    def rule_2(self, new_bottle):
        return new_bottle[0].transfer(new_bottle[2])

    def rule_3(self, new_bottle):
        return new_bottle[1].transfer(new_bottle[0])

    def rule_4(self, new_bottle):
        return new_bottle[1].transfer(new_bottle[2])

    def rule_5(self, new_bottle):
        return new_bottle[2].transfer(new_bottle[0])

    def rule_6(self, new_bottle):
        return new_bottle[2].transfer(new_bottle[1])

    """Função que verifica se o nó atual é sucesso"""
    @staticmethod
    def is_success(node):
        node_quantity = node.get_bottles_quantity()
        if (node_quantity[0] == 4 and node_quantity[1] == 4 and node_quantity[2] == 0):
            return True
        return False

    def show_information(self):
        self.root_node.show_information()

    def show_success_way(self):
        self.success_way.reverse()
        print('Caminho do sucesso: {}'.format(self.success_way))