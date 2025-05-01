import xml.etree.ElementTree as ET

#xml
arbol = ET.parse('datos.xml')
raiz = arbol.getroot()

#Busqueda de el led ab (led alto brillo)
def ab_led (color_led:str):
    #SE CARGA EL APARTADO DE <led_ab>
    ab_valores = raiz[0][1]
    valor_led = float(ab_valores.find(color_led).text)
    #retorna el voltaje del led
    if valor_led == None:
        return 0/0
    else:
        return valor_led

#busqueda de el led std (led estandar)
def std_led (color_led:str,desicion_voltaje:str):
    #se carga el apartado de <led_std>
    std_valores = raiz[0][0]
    if color_led != 'blanco' and desicion_voltaje == 'y':
        #se busca en <led_std_1.5>
        valor_led = float(std_valores[0].find(color_led).text)
        intensidad = 40
    else:
        #se busca en <Led_std_variado>
        valor_led = float(std_valores[1].find(color_led).text)
        intensidad = 30
    #retorna una tupla con los datos    
    if valor_led == None:
        return 0/0
    else:
        return valor_led,intensidad