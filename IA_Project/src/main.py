# main.py

# from .src import Bottle

from __future__ import unicode_literals

from src.BFS import BFS
from src.Bottle import Bottle
from src.Backtracking import Backtracking
from src.Node import Node


# MAIN BEGIN

code = 3

while code != 0:
    print("\n--------------Menu-----------------\n"
          "Digite 1 para Busca Backtracking\n"
          "Digite 2 para Busca em Largura\n"
          "Digite 0 para Sair\n")
    code = int(input())
    galao1 = Bottle(8, 8)
    galao2 = Bottle(5, 0)
    galao3 = Bottle(3, 0)
    if code == 1:
        back = Backtracking(galao1, galao2, galao3)
        back.start()
    else:
        lar = BFS(galao1, galao2, galao3)
        lar.start()

