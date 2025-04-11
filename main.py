from funciones import resistencia_color, valor_r, resistencia_ohm,suma_decimal
print('ELECTRICIDAD Y ELECTRONICA')

#usar las listas con circuitos en serie y los set como diccionarios
circuito = []
circuito_paralelo = {}
circuito_paralelo_estado = False
#descicrir el circuito
while True:
    print('como es el circuito')
    print('''1- Agregar un circuito en paralelo
        2- Agregar un led
        3- Agregar una resistencia
        4- Agregar un capacitor''')
    desicion = int(input('Escribe el numero de la accion a realizar:'))

    match desicion:
        #circuito paralelo
        case 1:
            while True:
                circuito_paralelo_desicion = input('quieres agregar un circuito paralelo(y) o cerrar uno ya existente(n):').lower
                if circuito_paralelo_desicion == 'y':
                    circuito_paralelo_estado = True
                    break
                elif circuito_paralelo_desicion == 'n':
                    circuito_paralelo_estado = False
                    break
                else:
                    print('escribe una opcion valida:')
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
                color_led_desicion = input('escribe el color del led:').lower()
                if color_led_desicion == 'blanco':
                    circuito.append(2.8)
                    break
                elif color_led_desicion in valor_led_ab.keys():
                    while estado_led:
                        color_brillo = input('El led es estandar(std) o alto brillo(ab):').lower()
                        if color_brillo == 'std':
                            for color_led in valor_led_std:
                                if color_led_desicion == color_led:
                                    #se agrega a un circuito paralelo si asi lo desea
                                    if circuito_paralelo_estado == True:
                                        circuito_paralelo.update({'led',valor_led_std[color_led]})
                                        estado_led = False
                                        break
                                    else:
                                        circuito.append(valor_led_std[color_led])
                                        estado_led = False
                                        break
                        elif color_brillo == 'ab':
                            for color_led in valor_led_ab:
                                if color_led_desicion == color_led:
                                    #se agrega a un circuito paralelo si asi lo desea
                                    if circuito_paralelo_estado == True:
                                        circuito_paralelo.update({'led',valor_led_ab[color_led]})
                                        estado_led = False
                                        break
                                    else:
                                        circuito.append(valor_led_ab[color_led])
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
                    while True:
                        omh_resistencia = input('escribe el valor omh de la resistencia:')
                        tolerancia_resistencia = input('escribe la tolerancia de la resistencia:')
                        try:
                            resistencia_ohm(omh_resistencia,float(tolerancia_resistencia))
                        except:
                            print('VALORES NO VALIDOS')
                        else:
                            #se agrega a un circuito paralelo si asi lo desea
                            if circuito_paralelo_estado == True:
                                circuito_paralelo.update({'resistencia':valor_r(resistencia_ohm(omh_resistencia,float(tolerancia_resistencia)))})
                                estado_resistencia = False
                                break
                            else:
                                circuito.append(valor_r(resistencia_ohm(omh_resistencia,float(tolerancia_resistencia))))
                                estado_resistencia = False
                                break
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
                                #se agrega a un circuito paralelo si asi lo desea
                                if circuito_paralelo_estado == True:
                                    circuito_paralelo({'resistencia',valor_r(resistencia_color(color1,color2,color3,color4))})
                                    estado_resistencia = False
                                    r_color_estado = False
                                    break
                                else:
                                    circuito.append(valor_r(resistencia_color(color1,color2,color3,color4)))
                                    estado_resistencia = False
                                    r_color_estado = False
                                    break
        #CAPACITORES
        case 4:
            break
        case 5:
            print(circuito)
    


