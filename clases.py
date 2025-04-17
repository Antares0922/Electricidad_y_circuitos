class Led():
    def __init__(self,valor):
        self.valor = valor
        
class Resistencia():
    def __init__(self,valor):
        self.valor = valor

class CircuitoParalelo():
    def __init__(self,componentes):
        self.componentes = componentes
        
class LedAb(Led):
    def __init__(self, valor):
        super().__init__(valor)
        self.intensidad = 20