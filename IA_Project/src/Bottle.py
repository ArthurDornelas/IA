#Primeiro galão com capacidade 8, outro com 5 e outro com 3

class Bottle:
    def __init__(self, capacity, currentCapacity):
        self.capacity = capacity
        self.currentCapacity = currentCapacity


    def transfer(self, otherBottle):
        otherCapacity = otherBottle.capacity
        otherCurrentCapacity = otherBottle.currentCapacity
        maxTransfer = otherCurrentCapacity - otherCapacity
        if(maxTransfer > 0 and self.currentCapacity > 0):
            a = 1

    def getCapacity(self):
        return self.capacity
