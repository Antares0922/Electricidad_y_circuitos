#Clase padre de leds
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
    def __init__(self,valores:tuple):
        #desenpaquetando la tupla
        resistencia,tolerancia,tolerancia_min,tolerancia_max = valores
        
        self.resistencia = resistencia
        self.tolerancia = tolerancia
        self.tolerancia_min = tolerancia_min
        self.tolerancia_max = tolerancia_max
        
    def comportamiento_paralelo(self):
        return 1/self.resistencia
#AUN NO ESTA LISTA
class CircuitoParalelo():
    def __init__(self,componentes:list):
        self.componentes = componentes
        
    def comportamiento_paralelo(self):
        for i in self.componentes:
            i.comportamiento_paralelo()      
