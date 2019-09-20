# main.py

# from .src import Bottle

from __future__ import unicode_literals
from src.Bottle import Bottle
from src.Backtracking import Backtracking
from src.Node import Node

# MAIN BEGIN

galao1 = Bottle(8, 8)
galao2 = Bottle(5, 0)
galao3 = Bottle(3, 0)

no = Node(0, None, galao1, galao2, galao3)
galao1.transfer(galao2)
no2 = Node(0, None, galao1, galao2, galao3)
no.add_child(no2)
no3 = no
galao1.transfer(galao3)
no4 = Node(0, None, galao1, galao2, galao3)
no3.add_child(no4)

galao1.showInformation()
galao2.showInformation()
galao3.showInformation()

no.show_information()


#
# back = Backtracking(galao1, galao2, galao3)
# back.start()
