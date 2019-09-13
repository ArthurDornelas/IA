#Primeiro galão com capacidade 8, outro com 5 e outro com 3
#bottle.py

class Bottle:
    def __init__(self, capacity, currentCapacity):
        self.capacity = capacity
        self.currentCapacity = currentCapacity


    def transfer(self, otherBottle):

        if self.currentCapacity <= 0:   #Galao Vazio
            return 0

        otherCapacity = otherBottle.getCapacity()
        otherCurrentCapacity = otherBottle.getCurrentCapacity()
        maxTransfer = otherCapacity - otherCurrentCapacity

        if maxTransfer > 0:            #Se galao nao esta lotado
            self.currentCapacity -= maxTransfer
            otherBottle.setCurrentCapacity(maxTransfer)
        else:
            return 0


    def getCapacity(self):
        return self.capacity

    def getCurrentCapacity(self):
        return self.currentCapacity

    def setCurrentCapacity(self, new_capacity):
        if (self.currentCapacity + new_capacity) <= self.capacity:
            self.currentCapacity += new_capacity
        else:
            return 0
