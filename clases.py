from abc import ABC, abstractclassmethod
class Led(ABC):
    def __init__(self,voltaje):
        self.voltaje = voltaje
        
class LedAB(Led):
    def __init__(self, voltaje):
        self.intensidad = 20
        super().__init__(voltaje)
    
class LedSTD(Led):
    def __init__(self, voltaje, intensidad):
        self.intensidad = intensidad
        super().__init__(voltaje)
        
class Resistencia():
    def __init__(self,valor):
        self.valor = valor
    #Como se debe comportar con un circuito paralelo
    def comportamiento_paralelo(self,valor):
        return 1/self.valor

class CircuitoParalelo():
    def __init__(self,componentes:list):
        self.componentes = componentes
        
