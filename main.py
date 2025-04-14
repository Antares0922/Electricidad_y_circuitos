from funciones import resistencia_color, valor_r, resistencia_ohm,suma_decimal
import xml.etree.ElementTree as ET


print('ELECTRICIDAD Y ELECTRONICA')
#usar una lista para el circuito y ir agregando listas dependiendo de los circuitos
circuito = []
#PROBLEMA 1 NO ES POSIBLE ANIDAR UN CIRCUITO A UN CIRCUITO PARALELO
circuito_paralelo = []
circuito_paralelo_estado = False
#XLM 
arbol = ET.parse('datos.xml')
raiz = arbol.getroot()
#descicrir el circuito
while True:
    print('como es el circuito')
    print('''    1- Agregar un circuito en paralelo
    2- Agregar un led
    3- Agregar una resistencia
    4- Vizualizar circuito
    5- Salir''')
    desicion = input('Escribe el numero de la accion a realizar:').lower()

    match desicion:
        #circuito paralelo
        case '1':
            while True:
                circuito_paralelo_desicion = input('quieres agregar un circuito paralelo(yes) o cerrar uno ya existente(no):').lower()
                match circuito_paralelo_desicion:
                    case 'yes':
                        circuito_paralelo_estado = True
                        break
                    case 'no':
                        circuito.append(circuito_paralelo.copy())
                        circuito_paralelo.clear()
                        circuito_paralelo_estado = False
                        break
                    case 'exit':
                        break

        #LEDS
        case '2':
            estado_led = True
            while estado_led:
                color_led_desicion = input('escribe el color del led:').lower()
                if color_led_desicion == 'blanco':
                    circuito.append(2.8)
                    break
                else:
                    while True:
                        color_brillo = input('El led es estandar(std) o alto brillo(ab):').lower()
                        if color_brillo == 'std':
                            #SE CARGA EL APARTADO DE <led_std>
                            std_valores = raiz[0][0]
                            if std_valores.find(color_led_desicion) != None:
                                valor_led_std = float(std_valores.find(color_led_desicion).text)
                                #se agrega al circuito
                                if circuito_paralelo_estado == True:
                                    circuito_paralelo.append(valor_led_std)
                                    estado_led = False
                                    break
                                else:
                                    circuito.append(valor_led_std)
                                    estado_led = False
                                    break
                            else:
                                print('COLOR NO VALIDO')
                                break
                            
                        elif color_brillo == 'ab':
                            #SE CARGA EL APARTADO DE <led_ab>
                            ab_valores = raiz[0][1]
                            if ab_valores.find(color_led_desicion) != None:
                                valor_led_ab = int(ab_valores.find(color_led_desicion).text)
                                #se agrega al circuito
                                if circuito_paralelo_estado == True:
                                    circuito_paralelo.append(valor_led_ab)
                                    estado_led = False
                                    break
                                else:
                                    circuito.append(valor_led_ab)
                                    estado_led = False
                                    break
                            else:
                                print('COLOR NO CALIDO')
                                break
                        else:
                            print('OPCION NO VALIDA')
                            break
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
                                circuito_paralelo.append(valor_r(resistencia_ohm(omh_resistencia,float(tolerancia_resistencia))))
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
                        try:
                            resistencia_color(color1,color2,color3,color4)
                        except:
                            print('INTENTALO DE NUEVO HUBO UN ERROR')
                        else:                                #se agrega a un circuito paralelo si asi lo desea
                            if circuito_paralelo_estado == True:
                                circuito_paralelo.append(valor_r(resistencia_color(color1,color2,color3,color4)))
                                estado_resistencia = False
                                r_color_estado = False
                                break
                            else:
                                circuito.append(valor_r(resistencia_color(color1,color2,color3,color4)))
                                estado_resistencia = False
                                r_color_estado = False
                                break
        case '4':
            print(circuito)
        case '5':
            break