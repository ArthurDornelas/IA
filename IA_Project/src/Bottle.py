# Primeiro galão com capacidade 8, outro com 5 e outro com 3
# Bottle.py

class Bottle:

    def __init__(self, capacity, current_quantity):
        self.capacity = capacity
        self.current_quantity = current_quantity

    def transfer(self, otherBottle):
        capacity2 = otherBottle.getCapacity()                   # Capacidade máxima do galão passado como parâmetro
        current_quantity2 = otherBottle.getCurrentQuantity()    # Quantidade atual do galão passado como parâmetro

        max_transfer = capacity2 - current_quantity2            # Determina qual a maior quantidade que pode ser transferida

        if self.current_quantity <= 0 or max_transfer == 0:      # Galao Vazio ou galão2 cheio
            return 0

        amount_to_transfer = 0
        if self.current_quantity >= max_transfer:               # Se galao nao esta lotado
            amount_to_transfer = max_transfer
        else:
            amount_to_transfer = self.current_quantity
        self.current_quantity -= amount_to_transfer
        current_quantity2 += amount_to_transfer
        otherBottle.setCurrentQuantity(current_quantity2)

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