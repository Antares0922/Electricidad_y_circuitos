from funciones import valor_r, desicion_resistencia_patron, suma_resistencia_paralelo,desicion_resistencia_ohm
from funciones import ley_ohm, ley_watt

#dando la bienvenida al programa
print('RESISTENCIAS Y CIRCUITOS')

#elecciones
estado = True
while estado:
    #variables para seguir con el progreso del programa
    resistencias_valores = []
    print('''que accion deseas realizar:
          1 = ver los valores de una resistencia por medio de omhs
          2 = ver los valres de una resistencia por medio de sus colores
          3 = sacar  valor de resistencia o tolerancaia/min/max
          4 = sumar un circuito en paralelo
          5 = sumar un circuito en serie
          6 = ley de omh
          7 = ley de watt''')
    accion = input('escribe el numero de la accion a realizar:')
    if accion == '1':
        desicion_ohm = int(input('coloca el valor de ohm'))
        desicion_tole = float(input('colaca el porcentaje de tolerancia'))
        if input('quieres que se muestren los colores?:').lower == 'si':
            (desicion_resistencia_ohm(desicion_ohm,desicion_tole))
        else:
            desicion_resistencia_ohm(desicion_ohm,desicion_tole,colores=False)