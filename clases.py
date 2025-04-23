#checar
class Led():
    def __init__(self,voltaje:float):
        self.voltaje = voltaje
        
    def comportamiento_paralelo(self):
        return 1/self.voltaje
        
class LedAB(Led):
    def __init__(self, voltaje):
        self.intensidad = 20/1000
        super().__init__(voltaje)

    
class LedSTD(Led):
    def __init__(self, voltaje, intensidad):
        self.intensidad = intensidad/1000
        super().__init__(voltaje)
        
class Resistencia():
    def __init__(self,resistencia):
        self.resistencia = resistencia
        
    def comportamiento_paralelo(self):
        return 1/self.resistencia
#checar
class CircuitoParalelo():
    def __init__(self,componentes:list):
        self.componentes = componentes
        
    def comportamiento_paralelo(self):
        for i in self.componentes:
            i.comportamiento_paralelo()      
