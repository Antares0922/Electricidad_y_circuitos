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