from funciones import resistencia_color, valor_r, resistencia_ohm,suma_decimal
print('ELECTRICIDAD Y ELECTRONICA')

#usar las listas con circuitos en serie y los set como circuitos en paralelo
circuito = []
#descicrir el circuito
print('como es el circuito')
print('''1- Agregar un circuito en paralelo
      2- Agregar un led
      3- Agregar una resistencia
      4- Agregar un capacitor''')
desicion = int(input('Escribe el numero de la accion a realizar:'))

#CAMBIAR A MATCH Y CASE
match desicion:
    case 1:
        circuito_paralelo = set()
    #LEDS
    case 2:
        valor_led_std ={'rojo':1.5,
                        'verde':1.8,
                        'amarillo':1.8}
        
        valor_led_ab = {'rojo':2,
                        'amarillo':2,
                        'verde':3,
                        'azul':3}
        estado_led = True
        
        while estado_led:
            color_led = input('escribe el color del led:').lower()
            if color_led == 'blanco':
                circuito.append(2.8)
                break
            elif color_led in valor_led_ab.keys():
                while estado_led:
                    color_brillo = input('El led es estandar(std) o alto brillo(ab):').lower()
                    if color_brillo == 'std':
                        for color in valor_led_std:
                            if color_led == color:
                                circuito.append(valor_led_std[color])
                                estado_led = False
                                break
                    elif color_brillo == 'ab':
                        for color in valor_led_ab:
                            if color_led == color:
                                circuito.append(valor_led_ab[color])
                                estado_led = False
                                break
            else:
                print('ESCRIBE UN COLOR EXISTENTE')
    #RESISTENCIA
    case 3:
        estado_resistencia = True
        
        while estado_resistencia:
            resistencia_funcion = input('agregar por el omh y tolerancia(romh) o colores(rcolor):').lower()
            if resistencia_funcion == 'romh':
                #POSIBLE ERROR SI SE PONE UN STR
                omh_resistencia = int(input('escribe el valor en omh de la resistencia:'))
                if omh_resistencia[2] != 0:
                    print('ese valor no se permite')
                else:
                    tolerancia = float(input('escribe la tolerancia de la resistencia:'))
                    tolerancia_valores = [1,2,0.5,0.25,0.1,0.05,5,10]
                    if tolerancia in tolerancia_valores:
                        #se agrega al cicuito y termina el bucle
                        circuito.append(valor_r(resistencia_ohm(str(omh_resistencia),tolerancia)))
                        estado_resistencia = False
                
            elif resistencia_funcion == 'rcolor':
                r_color_estado = True
                while r_color_estado:
                    color1 = input('escribe el color de la 1ra banda de la resistencia:').lower()
                    color2 = input('escribe el color de la 2ra banda de la resistencia:').lower()
                    color3 = input('escribe el color de la 3ra banda de la resistencia:').lower()
                    color4 = input('escribe el color de la 4ra banda de la resistencia:').lower()
                    color_resistencia = [color1,color2,color3,color4]
                    colores = ['negro','cafe','rojo','naranja','amarillo','verde','azul','morado','gris','blanco','oro','plata']
                    for color in color_resistencia:
                        if color not in colores:
                            print('escribe un color disponible')
                            break
                        else:
                            circuito.append(valor_r(resistencia_color(color1,color2,color3,color4)))
                            estado_resistencia = False
                            r_color = False

print(circuito)

#VERIFICAR LA VARIABLE 'COLOR' YA QUE SE REPITE EN DIFERENTES ACCIONES SIN RELACION ALGUNA