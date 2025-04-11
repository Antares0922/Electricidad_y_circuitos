#retorna los valores de cada color de la resistencia
def resistencia_color(color1:str,color2:str,color3:str,color4:str):
    color4bandas = {
    'negro':['0','0',1,None],
    'cafe':['1','1',10,0.01],
    'rojo':['2','2',100,0.02],
    'naranja':['3','3',1000,0.03],
    'amarillo':['4','4',10000,0.04],
    'verde':['5','5',100000,0.005],
    'azul':['6','6',1000000,0.0025],
    'morado':['7','7',10000000,None],
    'gris':['8','8',100000000,None],
    'blanco':['9','9',1000000000,None], 
    'oro':[None,None,0.1,0.05],
    'plata':[None,None,0.01,0.1]
    }
    colores = [color1,color2,color3,color4]
    resistencia = []
    indice_color = 0
    while indice_color < 4:
        for color in colores: 
            for i in color4bandas:
                #si no encuentra un color disponible salta al siguiente 
                if color.lower() == i.lower():
                    resistencia.append(color4bandas[i][indice_color])
                    indice_color += 1

    else:
        #lsita con los valores de cada color
        return resistencia

#retorna los valores por medio de el valor omh y tolerancia de la resistencia
def resistencia_ohm(resistencia:str,tolerancia:float):
    valores_4bandas = {
    0:['0','0',1,0,'negro'],
    1:['1','1',10,0.01,'cafe'],
    2:['2','2',100,0.02,'rojo'],
    3:['3','3',1000,0.03,'naranja'],
    4:['4','4',10000,0.04,'amarillo'],
    5:['5','5',100000,0.005,'verde'],
    6:['6','6',1000000,0.0025,'azul'],
    7:['7','7',10000000,0,'morado'],
    8:['8','8',100000000,0,'gris'],
    9:['9','9',1000000000,0,'blanco'], 
    10:[None,None,0.1,0.05,'oro'],
    11:[None,None,0.01,0.1,'plata']
    }
    valor_resistencia = []
    resistencia = str(resistencia)
    
    #buscando equivalentes  de los 1ros 2 digitos
    for a in valores_4bandas:
        if str(resistencia[0]) == valores_4bandas[a][0]:
            valor_resistencia.append(valores_4bandas[a][0])
            break
    for e in valores_4bandas:
        if str(resistencia[1]) == valores_4bandas[e][1]:
            valor_resistencia.append(valores_4bandas[e][1])
            break
    #buscando el multiplicador
    num = resistencia[0] + resistencia[1]
    num = float(num)
    for i in valores_4bandas:
        if num*valores_4bandas[i][2] == float(resistencia):
            valor_resistencia.append(valores_4bandas[i][2])
            break
    #buscando la tolerancia
    for o in valores_4bandas:
        if tolerancia == valores_4bandas[o][3]*100:
            valor_resistencia.append(valores_4bandas[o][3])
            break
    #lista con los valores de la resistencia
    return valor_resistencia

#retorna el valor en omh en float por medio de una lista
def valor_r(resistencia:list):
    #desnpaquetado de datos
    color_1, color_2, multi, porcentaje_tolerancia = resistencia
    
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

