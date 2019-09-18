# main.py

# from .src import Bottle
from __future__ import unicode_literals
from src.Bottle import Bottle
from src.Node import Node

#MAIN BEGIN

galao1 = Bottle(8, 8)
galao2 = Bottle(5, 0)
galao3 = Bottle(3, 0)


galao1.showInformation()
galao2.showInformation()
galao3.showInformation()

no = Node(0, 0, galao1.getCurrentQuantity(), galao2.getCurrentQuantity(), galao3.getCurrentQuantity())


galao1.transfer(galao2)

no2 = Node(1, no, galao1.getCurrentQuantity(), galao2.getCurrentQuantity(), galao3.getCurrentQuantity())
no.children.append(no2)

galao1.showInformation()
galao2.showInformation()

print("Volta o No")

no2.fillBottles(galao1, galao2, galao3)
no.children[0].fillBottles(galao1, galao2, galao3)

galao1.showInformation()
galao2.showInformation()