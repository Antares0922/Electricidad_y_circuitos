from funciones.funciones_resistencia import valor_r,resistencia_color,resistencia_ohm
from funciones.funciones_led import ab_led,std_led
import xml.etree.ElementTree as ET
from clases.leds import Led, LedAB, LedSTD
from clases.Resistencias import Resistencia

#descicrir el circuito
#usar una lista para el circuito y ir agregando listas dependiendo de los circuitos
#AGREGA LOS OBJETOS DE LAS CLASES
circuito = []    #PROBLEMA 1 NO ES POSIBLE ANIDAR UN CIRCUITO A UN CIRCUITO PARALELO
circuito_paralelo = []
circuito_paralelo_estado = False
#XLM 
arbol = ET.parse('datos.xml')
raiz = arbol.getroot()
while True:
    print('como es el circuito')
    print('''    1- Agregar un circuito en paralelo
    2- Agregar un led
    3- Agregar una resistencia
    4- Vizualizar circuito
    5- Salir
    6- Realizar el calculo''')
    desicion = input('Escribe el numero de la accion a realizar:').lower()
    match desicion:
        #circuito paralelo
        case '1':
            while True:
                #DESACTIVADA LA OPCION TEMPORALMENTE
                break
                circuito_paralelo_desicion = input('quieres agregar un circuito paralelo(yes) o cerrar uno ya existente(no):').lower()
                match circuito_paralelo_desicion:
                    case 'yes':
                        if circuito_paralelo_estado == True:
                            print('ya estas trabajando con un circuito paralelo')
                            break
                        else:
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
                color_brillo = input('El led es estandar(std) o alto brillo(ab):').lower()
                if color_brillo == 'std':
                    voltaje_desicion_led = input('el voltaje del led es de 1.5v si lo es(y):').lower()
                    try:
                        std_led(color_led_desicion,voltaje_desicion_led)
                    except:
                        print('ERROR')
                    else:
                        #desenpaquetando los datos
                        valor_led_std, intensidad = std_led(color_led_desicion,voltaje_desicion_led)
                        #Agregando al circuito
                        if circuito_paralelo_estado == True:
                                circuito_paralelo.append(LedSTD(valor_led_std,intensidad))
                                estado_led = False
                        else:
                            circuito.append(LedSTD(valor_led_std,intensidad))
                            estado_led = False
                                       
                elif color_brillo == 'ab':
                    try:
                        valor_led_ab = ab_led(color_led_desicion)
                    except:
                        print('ERROR')
                    else:
                        #Se agrega al circuito
                        if circuito_paralelo_estado == True:
                            circuito_paralelo.append(LedAB(valor_led_ab))
                            estado_led = False
                        else:
                            circuito.append(LedAB(valor_led_ab))
                            estado_led = False
                else:
                    print('OPCION NO VALIDA')
        #RESISTENCIA
        case '3':
            estado_resistencia = True
            
            while estado_resistencia:
                resistencia_funcion = input('agregar por el omh y tolerancia(romh) o colores(rcolor):').lower()
                if resistencia_funcion == 'romh':
                    while True:
                        omh_resistencia = input('escribe el valor omh de la resistencia:')
                        tolerancia_resistencia = input('escribe la tolerancia de la resistencia:')
                        #verifica si son validos los parametros
                        try:
                            resistencia_ohm(omh_resistencia,float(tolerancia_resistencia))
                        except:
                            print('VALORES NO VALIDOS')
                        else:
                            #se agrega a un circuito paralelo si asi lo desea
                            if circuito_paralelo_estado == True:
                                circuito_paralelo.append(Resistencia(valor_r(resistencia_ohm(omh_resistencia,float(tolerancia_resistencia)))))
                                estado_resistencia = False
                                break
                            else:
                                circuito.append(Resistencia(valor_r(resistencia_ohm(omh_resistencia,float(tolerancia_resistencia)))))
                                estado_resistencia = False
                                break
                elif resistencia_funcion == 'rcolor':
                    while True:
                        color1 = input('escribe el color de la 1ra banda de la resistencia:').lower()
                        color2 = input('escribe el color de la 2ra banda de la resistencia:').lower()
                        color3 = input('escribe el color de la 3ra banda de la resistencia:').lower()
                        color4 = input('escribe el color de la 4ra banda de la resistencia:').lower()
                        if circuito_paralelo_estado == True:
                            try:
                                circuito_paralelo.append(Resistencia(valor_r(resistencia_color(color1,color2,color3,color4))))
                            except:
                                print('ERROR INTENTALO DENUEVO')
                            else:
                                estado_resistencia = False
                                break
                        else:
                            try:
                                circuito.append(Resistencia(valor_r(resistencia_color(color1,color2,color3,color4))))
                            except:
                                print('ERROR INTENTALO DENUEVO')
                            else:
                                estado_resistencia = False
                                break
        case '4':
            print(circuito)
        case '5':
            break
        #CALCULOS
        case '6':
            #saca la resistencia total del circuito
            leds_valores = []
            resistencia_valores = []
            for componente in circuito:
                if isinstance(componente,Resistencia):
                    resistencia_valores.append(componente.resistencia)
                elif isinstance(componente,Led):
                    leds_valores.append(componente.voltaje)
            #sacando la resistencia total del circuito   
            resistecnia_total = sum(resistencia_valores)
            
            #Obtencion de los demas datos del circuito
            leyes = input('Te falta algun dato si(y):').lower()
            if leyes != 'y':
                while True:
                    try:
                        intensidad_total = float(input('escribe la intensidad total:'))
                        voltaje_total = float(input('Escribe el voltaje total:'))
                        potencia_total = voltaje_total * intensidad_total
                    except:
                        print('ERROR OPCION NO VALIDA')
                    else:
                        break
            else:
                leyes_estado = True
                while leyes_estado:
                    leyes = input('Te falta la intensidad(I) o el voltaje(V):').upper()
                    match leyes:
                        case 'I':
                            while True:
                                try:
                                    voltaje_total = float(input('Escribe el voltaje total:'))
                                    intensidad_total = voltaje_total / resistecnia_total
                                    potencia_total = voltaje_total * intensidad_total
                                except:
                                    print('ERROR ESCRIBE UN DATO VALIDO')
                                else:
                                    leyes_estado = False
                                    break
                        case 'V':
                            while True:
                                try:
                                    intensidad_total = float(input('Escribe la intensidad total:'))
                                    voltaje_total = intensidad_total * resistecnia_total
                                    potencia_total = voltaje_total * intensidad_total
                                except:
                                    print('ERROR ESCRIBE UN DATO VALIDO')
                                else:
                                    leyes_estado = False
                                    break
                        case _:
                            print('OPCION NO VALIDA')
            #Mostrando los datos totales
            print(f'resistecnia total:{resistecnia_total} ,intensidad total:{intensidad_total} ,potencia total:{potencia_total} ,voltaje total:{voltaje_total}')
            #obteniendo los datos de los componentes individuales
            datos_circuito = {
                
            }
            resistencia_num = 0
            led_num = 0
            for componente in circuito:
                if isinstance(componente,Resistencia):
                    #numero de resistencia
                    resistencia_num += 1
                    #sacando los datos de la resistencia
                    if circuito_paralelo_estado == True:
                        pass
                    else:
                        componente_resistecnia = componente.resistencia
                        componente_intensidad = intensidad_total
                        componente_voltaje =  componente_intensidad * componente_resistecnia
                        componente_potencia = componente_voltaje * componente_intensidad
                    #agregando los datos de la resistencia
                    resistencia_datos = {
                        'resistencia':componente.resistencia,
                        'intensidad':round(componente_intensidad,5),
                        'voltaje':round(componente_voltaje,5),
                        'potencia':round(componente_potencia,5)
                    }
                    datos_circuito[f'resistencia {resistencia_num}'] = resistencia_datos
                elif isinstance(componente,Led):
                    #numero de led
                    led_num += 1
                    #sacando datos del led
                    if circuito_paralelo_estado == True:
                        pass
                    else:
                        try:
                            voltaje_led = componente_voltaje - componente.voltaje
                        except:
                            voltaje_led = voltaje_total - componente.voltaje
                    resistencia_necesaria = voltaje_led / componente.intensidad
                    componente_potencia_led = componente.voltaje * componente.intensidad
                    #agregando los datos de el led
                    led_datos = {
                        'resistencia necesaria': resistencia_necesaria,
                        'intensidad': componente.intensidad,
                        'voltaje': componente.voltaje,
                        'potencia': componente_potencia_led,
                    }
                    datos_circuito[f'led {led_num}'] = led_datos
            print(datos_circuito)