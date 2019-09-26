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
            self.print_fluxograma()
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
            print("------------- Final ---------------")
            self.show_success_way()
            self.show_level_success_way()
            print("\n A arvore gerada eh: \n")
            self.pprint_tree(self.root_node, "", True)

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

    def show_level_success_way(self):
        print("O nivel da solucao eh: {}".format(len(self.success_way) - 1))

    def pprint_tree(self, node, _prefix, _last):
        print(_prefix, "`- " if _last else "|- ", node.get_information(), sep="")
        _prefix += "   " if _last else "|  "
        child_count = len(node.children)
        for i, child in enumerate(node.children):
            _last = i == (child_count - 1)
            self.pprint_tree(child, _prefix, _last)

    def print_opened_list(self):
        print("Lista de Abertos: ")
        for i in self.openedList:
            print(i.get_bottles_quantity(), end=" ")
        print("\n")

    def print_closed_list(self):
        print("Lista de Fechados: ")
        for j in self.closedList:
            print(j , end=" ")
        print("\n")

    def print_fluxograma(self):
        print("------------ Fluxograma ---------------")
        self.print_opened_list()
        self.print_closed_list()
        print("Arvore Atual")
        self.pprint_tree(self.root_node, "", True)
        print("\n\n")


class Bottle:

    def __init__(self, capacity, current_quantity):
        self.capacity = capacity
        self.current_quantity = current_quantity

    def transfer(self, otherBottle):
        capacity2 = otherBottle.getCapacity()                   # Capacidade máxima do galão passado como parâmetro
        current_quantity2 = otherBottle.getCurrentQuantity()    # Quantidade atual do galão passado como parâmetro

        max_transfer = capacity2 - current_quantity2            # Determina qual a maior quantidade que pode ser transferida
        #print("mmax : {} current q: {}".format(max_transfer, self.current_quantity))
        if self.current_quantity <= 0 or max_transfer == 0:      # Galao Vazio ou galão2 cheio
            return 0
        #print("passou")
        amount_to_transfer = 0
        if self.current_quantity >= max_transfer:               # Se galao nao esta lotado
            amount_to_transfer = max_transfer
        else:
            amount_to_transfer = self.current_quantity
        self.current_quantity -= amount_to_transfer
        current_quantity2 += amount_to_transfer
        otherBottle.setCurrentQuantity(current_quantity2)
        return 1

    def getCapacity(self):
        return self.capacity

    def getCurrentQuantity(self):
        return self.current_quantity

    def setCurrentQuantity(self, new_quantity):
        self.current_quantity = new_quantity

    def fillBottle(self):
        self.current_quantity = self.capacity

    def showInformation(self):
        print('Total capacity: {}'.format(self.capacity))
        print('Current quantity: {} \n'.format(self.current_quantity))

    def set_quantity(self, quantity):
        self.current_quantity = quantity


class Node:

    def __init__(self, identity, father_node, bottle1, bottle2, bottle3):
        self.bottles_quantity = [bottle1.getCurrentQuantity(), bottle2.getCurrentQuantity(), bottle3.getCurrentQuantity()]
        self.bottles_capacity = [bottle1.getCapacity(), bottle2.getCapacity(), bottle3.getCapacity()]     # não sei se irá usar
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
        print("{}  {}".format(self.id, self.bottles_quantity))
        #for child in self.children:
         #   child.show_information()

    def get_information(self):
        return self.bottles_quantity

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

####### MAIN
def main():
    galao1 = Bottle(8, 8)
    galao2 = Bottle(5, 0)
    galao3 = Bottle(3, 0)
    lar = BFS(galao1, galao2, galao3)
    lar.start()

if __name__== "__main__":
  main()