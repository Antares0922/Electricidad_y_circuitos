from funciones import resistencia_color, valor_r, resistencia_ohm,suma_decimal
print('ELECTRICIDAD Y ELECTRONICA')

#usar una lista para el circuito y ir agregando listas dependiendo de los circuitos SECUENCIALMENTE
                        #0,0 EL 1ER DATO REPRESENTA EL NUMERO DEL CIRCUITO PARALELO EN CO (circuito origen)
                        #EL 2DO DATO ES QUE TAN PROFUNDO ESTA DEL CIRCUITO QUE SALIO de CO
circuito_origen = [(0,0)]
circuito_paralelo = []
circuito_anidado = []
num_circuito_paralelo = 0
#PROBLEMA 1 NO ES POSIBLE ANIDAR UN CIRCUITO PARALELO A OTRO CIRCUITO PARALELO
circuito_paralelo_estado = False
circuito_anidado_estado = False
#descicrir el circuito
while True:
    print('como es el circuito')
    print('''    1- circuitos paralelos
    2- Agregar un led
    3- Agregar una resistencia
    4- Vizualizar circuito
    5- Salir''')
    desicion = input('Escribe el numero de la accion a realizar:').lower()

    match desicion:
        #circuito paralelo
        case '1':
            while True:
                circuito_paralelo_desicion = input('quieres agregar un circuito paralelo(yes), cerrar uno ya existente(no) o anidar un circuito(ani):').lower()
                match circuito_paralelo_desicion:
                    case 'yes':
                        if circuito_paralelo == True:
                            print('YA ESTAS TRABAJANDO CON UN CIRCUITO')
                            break
                        else:
                            circuito_paralelo_estado = True
                            break
                    case 'no':
                            num_circuito_paralelo += 1
                            circuito_paralelo.append((num_circuito_paralelo,0))
                            circuito_origen.append(circuito_paralelo.copy())
                            circuito_paralelo.clear()
                            circuito_paralelo_estado = False
                            break
                    case 'exit':
                        break
                    case 'ani':
                        print('con que circuito paralelo deseas trabajar')
                        circuito_anidado_estado = True
                        while True:
                            try:
                                num_circuito_paralelo_desicion = int(input('escribe el numero del circuito:'))
                                profundidad_circuito = int(input('escribe que tan profundo esta del num del circuito:'))
                            except:
                                print('ESCRIBE UN NUMERO O UNA CORDENADA VALIDA')
                            else:
                                for busqueda in circuito_origen:
                                    if (num_circuito_paralelo_desicion,profundidad_circuito) == busqueda:
                                        index_busqueda = busqueda.index()
                                        profundidad_circuito += 1
                                        circuito_anidado.append((num_circuito_paralelo,profundidad_circuito))
                                        circuito_anidado.copy(circuito_paralelo[index_busqueda])
                                        
                                        
        #LEDS
        case '2':
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
                    circuito_origen.append(2.8)
                    break
                elif color_led_desicion in valor_led_ab.keys():
                    while estado_led:
                        color_brillo = input('El led es estandar(std) o alto brillo(ab):').lower()
                        if color_brillo == 'std':
                            for color_led in valor_led_std:
                                if color_led_desicion == color_led:
                                    #se agrega a un circuito paralelo si asi lo desea
                                    if circuito_paralelo_estado == True:
                                        if circuito_anidado_estado == True:
                                            circuito_anidado.append(valor_led_std[color_led])
                                            estado_led = False
                                            break
                                        else:
                                            circuito_paralelo.append(valor_led_std[color_led])
                                            estado_led = False
                                            break
                                    else:
                                        circuito_origen.append(valor_led_std[color_led])
                                        estado_led = False
                                        break
                        elif color_brillo == 'ab':
                            for color_led in valor_led_ab:
                                if color_led_desicion == color_led:
                                    #se agrega a un circuito paralelo si asi lo desea
                                    if circuito_paralelo_estado == True:
                                        if circuito_anidado_estado == True:
                                            circuito_anidado.append(valor_led_ab[color_led])
                                        else:
                                            circuito_paralelo.append(valor_led_ab[color_led])
                                            estado_led = False
                                            break
                                    else:
                                        circuito_origen.append(valor_led_ab[color_led])
                                        estado_led = False
                                        break
                else:
                    print('ESCRIBE UN COLOR EXISTENTE')
        #RESISTENCIA
        case '3':
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
                                if circuito_anidado_estado == True:
                                    circuito_anidado.append(valor_r(resistencia_ohm(omh_resistencia,float(tolerancia_resistencia))))
                                    estado_resistencia = False
                                    break
                                else:
                                    circuito_paralelo.append(valor_r(resistencia_ohm(omh_resistencia,float(tolerancia_resistencia))))
                                    estado_resistencia = False
                                    break
                            else:
                                circuito_origen.append(valor_r(resistencia_ohm(omh_resistencia,float(tolerancia_resistencia))))
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
                                    if circuito_anidado_estado == True:
                                        circuito_anidado.append(valor_r(resistencia_color(color1,color2,color3,color4)))
                                        estado_resistencia = False
                                        r_color_estado = False
                                        break
                                    else:
                                        circuito_paralelo.append(valor_r(resistencia_color(color1,color2,color3,color4)))
                                        estado_resistencia = False
                                        r_color_estado = False
                                        break
                                else:
                                    circuito_origen.append(valor_r(resistencia_color(color1,color2,color3,color4)))
                                    estado_resistencia = False
                                    r_color_estado = False
                                    break
        case '4':
            print(circuito_origen, 'circuito normal')
        case '5':
            break