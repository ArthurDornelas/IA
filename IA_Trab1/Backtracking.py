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
        self.print_fluxograma()
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
                    self.print_fluxograma()
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
        print("\n A arvore gerada eh: \n")
        self.print_tree(self.root_node, "", True)

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

    def print_tree(self, node, _prefix, _last):
        print(_prefix, "`- " if _last else "|- ", node.get_information(), sep="")
        _prefix += "   " if _last else "|  "
        child_count = len(node.children)
        for i, child in enumerate(node.children):
            _last = i == (child_count - 1)
            self.print_tree(child, _prefix, _last)

    def print_fluxograma(self):
        print("----------- Fluxograma ------------")
        self.print_tree(self.root_node, "", True)
        print("\n")

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


def main():
    galao1 = Bottle(8, 8)
    galao2 = Bottle(5, 0)
    galao3 = Bottle(3, 0)
    back = Backtracking(galao1, galao2, galao3)
    back.start()

if __name__== "__main__":
  main()