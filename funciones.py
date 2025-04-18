import xml.etree.ElementTree as ET
#XML
arbol = ET.parse('datos.xml')
raiz = arbol.getroot()

#retorna los valores de cada color de la resistencia
def resistencia_color(color1:str,color2:str,color3:str,color4:str):
    #CARGA LOS VALORES DE LA RESISTENCIA <cuatrobandas>
    valores_4bandas = raiz[1][0]
    colores = [color1,color2,color3,color4]
    resistencia = []
    indice_color = 0
    for i in range(4):
        #saca las etiquetas del color
        color = valores_4bandas.find(colores[indice_color])
        #saca la etiqueta del valor 
        valor = color[indice_color]
        #saca y agrega el valor final
        resistencia.append(valor.text)
        indice_color +=1
    else:
        #lista con los valores de cada color en str
        return resistencia

#retorna los valores por medio de el valor omh y tolerancia de la resistencia
def resistencia_ohm(resistencia:str,tolerancia:float):
    #CARGA LOS VALORES DE LA RESISTENCIA <cuatrobandas>
    valores_4bandas = raiz[1][0]
    resistencia_valores = []
    #bsucando el 1er digito
    for color in valores_4bandas:
        if color[0].text == resistencia[0]:
            resistencia_valores.append(color[0].text)
    #buscando el 2do digito
    for color in valores_4bandas:
        if color[1].text == resistencia[1]:
            resistencia_valores.append(color[1].text)
    #buscando el multiplicador
    num = resistencia_valores[0] + resistencia_valores[1]
    for color in valores_4bandas:
        if float(num)*float(color[2].text) == float(resistencia):
            resistencia_valores.append(color[2].text)
    #buscando la tolerancia
    for color in valores_4bandas:
        if str(tolerancia/100) == color[3].text:
            resistencia_valores.append(color[3].text)
    #VERIFICANDO SI LA LISTA ES CORRECTA
    if len(resistencia_valores) == 4:
        return resistencia_valores
    else:
        return 0/0

#retorna el valor en omh en float por medio de una lista
def valor_r(resistencia:list):
    #desnpaquetado de datos
    color_1, color_2, multi, porcentaje_tolerancia = resistencia
    #verificar los datos
    if color_1 or color_2 == None:
        return 0/0
    elif porcentaje_tolerancia == None:
        return 0/0
    else:
        #Valor de resistencia
        v_resistencia = str(color_1) + str(color_2)
        v_resistencia = int(v_resistencia) * float(multi)
        
        #tolerancia, min y max
        tolerancia = v_resistencia * float(porcentaje_tolerancia)
        tolerancia_min = v_resistencia - tolerancia
        tolerancia_max = v_resistencia + tolerancia
        
        #retorna el valor en un float
        return v_resistencia

#suma las resistencia en un circuito paralelo
def suma_decimal(componentes:list):
    decimal_componentes = []
    
    #sacando decimales de cada resistencia
    for componente in decimal_componentes:
        decimal_componentes.append(1/componente)
    #sacando resistencia total
    componente_total = sum(decimal_componentes)
    #dividirlo entre 1
    componente_total = 1/componente_total
    
    return componente_total

