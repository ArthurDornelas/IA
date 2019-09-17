# main.py

# from .src import Bottle


from IA_Project.src.Bottle import Bottle


galao1 = Bottle(8, 8)
galao2 = Bottle(5, 0)
galao3 = Bottle(3, 0)


galao1.showInformation()
galao2.showInformation()
galao3.showInformation()


galao1.transfer(galao2)

galao1.showInformation()
galao2.showInformation()
