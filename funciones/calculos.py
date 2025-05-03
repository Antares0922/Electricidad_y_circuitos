from clases.Resistencias import Resistencia
from clases.leds import Led,LedAB,LedSTD

#Sacando resistencia total
def RTotal(circuito:list):
    resistencia_valores = []
    resistencia_total = 0
    for componente in circuito:
        #Verifica si el componente es de la clase Resistencia
        if isinstance(componente,Resistencia):
            resistencia_valores.append(componente.resistencia)
    #sacando la resistencia total del circuito   
    resistencia_total = sum(resistencia_valores)
    return resistencia_total

#leyes de ohm y watt
def intensidad_ley(voltaje,resistencia_total):
    intensidad = voltaje / resistencia_total
    return intensidad

def voltaje_ley(intensidad,resistencia_total):
    voltaje = intensidad * resistencia_total
    return voltaje

def potencia_ley(voltaje,intensidad):
    potencia = voltaje * intensidad
    return potencia

def omh_ley(voltaje,intensidad):
    resistencia = voltaje / intensidad
    return resistencia

#Datos de cada componente