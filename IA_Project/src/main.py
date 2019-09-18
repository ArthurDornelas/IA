# main.py

# from .src import Bottle
from src.Bottle import Bottle
from src.Node import Node

#MAIN BEGIN

galao1 = Bottle(8, 8)
galao2 = Bottle(5, 0)
galao3 = Bottle(3, 0)


galao1.showInformation()
galao2.showInformation()
galao3.showInformation()

no = Node(galao1.getCurrentQuantity(), galao2.getCurrentQuantity(), galao3.getCurrentQuantity())

galao1.transfer(galao2)

galao1.showInformation()
galao2.showInformation()

print("Volta o No")

no.fillBottles(galao1, galao2, galao3)

galao1.showInformation()
galao2.showInformation()