from funciones import resistencia_color, valor_r, resistencia_ohm,suma_decimal
import xml.etree.ElementTree as ET
from clases import Resistencia, LedAB,LedSTD, Led
import dearpygui.dearpygui as dpg

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
    5- Salir''')
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
                    #SE CARGA EL APARTADO DE <led_std>
                    std_valores = raiz[0][0]
                    #comparando con los colores de <led_std_variado>
                    if std_valores[1].find(color_led_desicion) != None:
                        #busqueda del voltaje e intensidad correcta
                        voltaje_desicion_led = input('el voltaje del led es de 1.5v si lo es(y):').lower()
                        #no existe un led blanco con 1.5v
                        if voltaje_desicion_led == 'y' and color_led_desicion != 'blanco':                 
                                valor_led_std = float(std_valores[0].find(color_led_desicion).text)
                                intensidad = 40
                        else:
                            valor_led_std = float(std_valores[1].find(color_led_desicion).text)
                            intensidad = 30
                        #se agrega al circuito
                        if circuito_paralelo_estado == True:
                                circuito_paralelo.append(LedSTD(valor_led_std,intensidad))
                                estado_led = False
                        else:
                                circuito.append(LedSTD(valor_led_std,intensidad))
                                estado_led = False
                    else:
                        print('OPCION NO VALIDO')
                                
                elif color_brillo == 'ab':
                    #SE CARGA EL APARTADO DE <led_ab>
                    ab_valores = raiz[0][1]
                    if ab_valores.find(color_led_desicion) != None:
                        valor_led_ab = int(ab_valores.find(color_led_desicion).text)
                        #se agrega al circuito
                        if circuito_paralelo_estado == True:
                            circuito_paralelo.append(LedAB(valor_led_ab))
                            estado_led = False
                        else:
                            circuito.append(LedAB(valor_led_ab))
                            estado_led = False
                    else:
                        print('OPCION NO VALIDO')
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
                        #NO SE PEUDEN AGREGAR RESISTENCIA CON VALOR 0
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
                        else:                               
                            #se agrega a un circuito paralelo si asi lo desea
                            if circuito_paralelo_estado == True:
                                try:
                                    valor_r(resistencia_color(color1,color2,color3,color4))
                                except:
                                    print('ERROR PRUEBE DE NUEVO')
                                    r_color_estado = False
                                else:
                                    circuito_paralelo.append(Resistencia(valor_r(resistencia_color(color1,color2,color3,color4))))
                                    estado_resistencia = False
                                    r_color_estado = False
                                
                            else:
                                try:
                                    valor_r(resistencia_color(color1,color2,color3,color4))
                                except:
                                    print('ERROR PRUEBE DE NUEVO')
                                    r_color_estado = False
                                else:
                                    circuito.append(Resistencia(valor_r(resistencia_color(color1,color2,color3,color4))))
                                    estado_resistencia = False
                                    r_color_estado = False
        case '4':
            print(circuito)
        case '5':
            break
        #CALCULOS
        case '6':
            #saca la resistencia total del circuito
            resistencia_valores = []
            for resistencia in circuito:
                if isinstance(resistencia,Resistencia):
                    resistencia_valores.append(resistencia.resistencia)
                    
            resistecnia_total = sum(resistencia_valores)
            
            #Obtencion de los demas datos
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
                leyes = input('Te falta la intensidad(I) o el voltaje(V):').upper()
                leyes_estado = True
                while leyes_estado:
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
            #SIN TERMINAR
            datos_circuito = {
                
            }
            resistencia_num = 0
            led_num = 0
            for componente in circuito:
                if isinstance(componente,Resistencia):
                    resistencia_num += 1
                    componente_resistecnia = componente.resistencia
                    componente_intensidad = intensidad_total
                    componente_voltaje =  componente_intensidad * componente_resistecnia
                    componente_potencia = componente_voltaje * intensidad
                elif isinstance(componente,Led):
                    led_num += 1
                    #operaciones a realizar
                 