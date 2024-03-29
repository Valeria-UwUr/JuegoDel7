from TDA.Dado import Dado
from TDA.Jugador import jugador

class Juego4:

    def __init__(self, dao1, dado2, jugador):
        self.dado1=dado1
        self.dado2=dado2
        self.jugador=jugador

    def seguirJugando(self):
        return self.jugador.getCapital()>0

    def tirarDados(self):
        return self.dado1.tirarDado()
        return self.dado2.tirarDado()

    def getDado1(self):
        return self.dado1.getDado()

    def getDado2(self):
        return self.dado2.getDado()

    def suma(self):
        return self.dado1.getDado()+self.dado2.getDado()
    
    def jugar(self):
        suma=self.suma()
        capital=self.jugador.getCapital()
        if ((suma>7)&(self.jugador.getJugada()==1)):
            self.jugador.setCapital(capital+self.jugador.getApuesta())
        elif ((suma<7)&(self.jugador.getJugada()==2)):
            self.jugador.setCapital(capital+self.jugador.getApuesta())
        elif((suma==7)&(capital+self.jugador.getJugada()==3):
             self.jugador.setCapital(capital+self.jugador.getApuesta()*2)
        else:
            self.jugador.setCapital(capital-self.jugador.getApuesta())
