#main.py

from src.bottle import Bottle

galao_1 = Bottle(8, 8)
galao_2 = Bottle(5, 0)
galao_3 = Bottle(3, 0)

galao_1.transfer(galao_3)
print(galao_3.getCurrentCapacity())