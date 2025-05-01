#AUN NO ESTA LISTA
class CircuitoParalelo():
    def __init__(self,componentes:list):
        self.componentes = componentes
        
    def comportamiento_paralelo(self):
        for i in self.componentes:
            i.comportamiento_paralelo()