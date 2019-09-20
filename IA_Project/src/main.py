# main.py

# from .src import Bottle

from __future__ import unicode_literals
from src.Bottle import Bottle
from src.Backtracking import Backtracking
from src.Node import Node

# MAIN BEGIN

galao1 = Bottle(8, 4)
galao2 = Bottle(5, 4)
galao3 = Bottle(3, 0)

no = Node(0, None, galao1, galao2, galao3)
no2 = no
galao1.transfer(galao2)


back = Backtracking(galao1, galao2, galao3)
back.start()
