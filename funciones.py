def desicion_resistencia_patron():
    valores_4bandas = {
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
    #recolectar los colores de la resistencia
    print("""COLORES DISPONIBLES
              negro = 0
              cafe = 1
              rojo = 2
              naranja = 3
              amarillo = 4
              verde = 5
              azul = 6
              morado = 7
              gris = 8
              blanco = 9
              oro = 10
              plata = 11""")
    resistencia = []
    indice_color = 0
    while indice_color < 4:
        desicion = int(input('elige un color:'))
        if desicion == 0:
            resistencia.append(valores_4bandas['negro'][indice_color])
            indice_color += 1
        elif desicion == 1:
            resistencia.append(valores_4bandas['cafe'][indice_color])
            indice_color += 1
        elif desicion == 2:
            resistencia.append(valores_4bandas['rojo'][indice_color])
            indice_color += 1
        elif desicion == 3:
            resistencia.append(valores_4bandas['naranja'][indice_color])
            indice_color += 1
        elif desicion == 4:
            resistencia.append(valores_4bandas['amarillo'][indice_color])
            indice_color += 1
        elif desicion == 5:
            resistencia.append(valores_4bandas['verde'][indice_color])
            indice_color += 1
        elif desicion == 6:
            resistencia.append(valores_4bandas['azul'][indice_color])
            indice_color += 1
        elif desicion == 7:
            resistencia.append(valores_4bandas['morado'][indice_color])
            indice_color += 1
        elif desicion == 8:
            resistencia.append(valores_4bandas['gris'][indice_color])
            indice_color += 1
        elif desicion == 9:
            resistencia.append(valores_4bandas['blanco'][indice_color])
            indice_color += 1
        elif desicion == 10:
            resistencia.append(valores_4bandas['oro'][indice_color])
            indice_color += 1
        elif desicion == 11:
            resistencia.append(valores_4bandas['plata'][indice_color])
    else: 
        #retorna una lista con los datos de la resistencia
        return resistencia
    
def valor_r(resistencia:list,mostrar_datos=False,datos_completos=False):
    #desnpaquetado de datos
    color_1, color_2, multi, porcentaje_tolerancia = resistencia
    
    #Valor de resistencia
    v_resistencia = color_1 + color_2
    v_resistencia = int(v_resistencia)*multi

    #tolerancia, min y max
    tolerancia = v_resistencia*porcentaje_tolerancia
    tolerancia_min = v_resistencia - tolerancia
    tolerancia_max = v_resistencia + tolerancia
    
    #muestra por pantalla los resultados
    if mostrar_datos == True:
        print(v_resistencia, 'ohm' ,int(porcentaje_tolerancia*100),'%')
        print('tolerancia: ', tolerancia)
        print('tolerancia minima: ', tolerancia_min)
        print('tolerancia maxima: ', tolerancia_max)
    else:
        pass
    #retorna una tupla con los datos
    if datos_completos == True:
        return v_resistencia,tolerancia,tolerancia_min,tolerancia_max 
    #retorna el valor solamente
    else:
        return v_resistencia    

def suma_resistencia_paralelo(resistencias:list):
    decimal_resistencia = []
    
    #sacando decimales de cada resistencia
    for resistencia in resistencias:
        decimal_resistencia.append(1/resistencia)
    #sacando resistencia total
    resistencia_total = sum(decimal_resistencia)
    #dividirlo entre 1
    resistencia_total = 1/resistencia_total
    
    return resistencia_total

def desicion_resistencia_ohm(resistencia,tolerancia:float,colores:False):
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
    color_resistencia = []
    valor_resistencia = []
    resistencia = str(resistencia)
    
    #buscando equivalentes  de los 1ros 2 digitos
    for a in valores_4bandas:
        if str(resistencia[0]) == valores_4bandas[a][0]:
            color_resistencia.append(valores_4bandas[a][4])
            valor_resistencia.append(valores_4bandas[a][0])
            break
    for e in valores_4bandas:
        if str(resistencia[1]) == valores_4bandas[e][1]:
            color_resistencia.append(valores_4bandas[e][4])
            valor_resistencia.append(valores_4bandas[e][1])
            break
    #buscando el multiplicador
    num = resistencia[0] + resistencia[1]
    num = float(num)
    for i in valores_4bandas:
        if num*valores_4bandas[i][2] == float(resistencia):
            color_resistencia.append(valores_4bandas[i][4])
            valor_resistencia.append(valores_4bandas[i][2])
            break
    #buscando la tolerancia
    for o in valores_4bandas:
        if tolerancia == valores_4bandas[o][3]*100:
            color_resistencia.append(valores_4bandas[o][4])
            valor_resistencia.append(valores_4bandas[o][3])
            break
    
    return valor_resistencia
    
def ley_ohm(volts:float,intensidad:float,resistencia:float):
    print('''cual es el datos faltante
          Volts = V
          Intensidad = I
          Resistencia = R''')
    #sacando el valor faltante
    while True:
            desicion = input('escribe la letra del dato:').capitalize()
            if desicion == 'V':
                volts = intensidad * resistencia
                return volts
                break
            elif desicion == 'I':
                intensidad = volts/resistencia
                return intensidad
                break
            elif desicion == 'R':
                resistencia = volts/intensidad
                return resistencia
                break
            else:
                print('escribe una letra valida')

def ley_watt(potencia:float,volts:float,intensidad:float):
    print('''cual es el datos faltante
          Potencia = P
          Volts = V
          Intensidad = I''')
    #sacando el valor faltante
    while True:
            desicion = input('escribe la letra del dato:').capitalize()
            if desicion == 'P':
                potencia = intensidad * volts
                return potencia
                break
            elif desicion == 'V':
                volts = potencia/intensidad
                return volts
                break
            elif desicion == 'I':
                intensidad = potencia/volts
                return intensidad
                break
            else:
                print('escribe una letra valida')