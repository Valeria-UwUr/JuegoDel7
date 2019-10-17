import random

class Dado:

    def _init_(self):
        self.dado=0


    def tirarDado(self):
        self.dado=random.randint(1,6)

    def getDado(self):
        return self.dado
        
