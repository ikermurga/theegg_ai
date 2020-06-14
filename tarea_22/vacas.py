'''
Entrada: Número total de vacas en la zona de Zaragoza que están a la venta.
Entrada: Peso total que el camión puede llevar.
Entrada: Lista de pesos de las vacas.
Entrada: Lista de la producción de leche por vaca, en litros por día.
Salida: Cantidad máxima de producción de leche se puede obtener.
'''

#[-1, -1, -1, -1, -1, -1, -1, -1]
# # Datos con resultado: vaca 1, 4, 5, 6, total 93
# numeroVacas = 6
# pesoMaximoCamion = 700
# pesosDeVacas = [360, 250, 400, 180, 50, 90]
# lechePorDiaPorVaca = [40, 35, 43, 28, 12, 13]

# # Datos con resultado: vaca 2, 3, 4, 5, 6 total 188
# numeroVacas = 8
# pesoMaximoCamion = 1000
# pesosDeVacas = [223, 243, 100, 200, 200, 155, 300, 150]
# lechePorDiaPorVaca = [30, 34, 28, 45, 31, 50, 29, 1]

# Datos con resultado: vaca 1, 2, 3, 4, 5, 6, 8, 9 total 320
numeroVacas = 10
pesoMaximoCamion = 2000
pesosDeVacas = [340, 355, 223, 243, 130, 240, 260, 155, 302, 130]
lechePorDiaPorVaca = [45, 50, 34, 39, 29, 40, 30, 52, 31, 1]

# Calcular numero de listas y rellenar con -1
numeroDeListas = 2 ** numeroVacas
listaDeListas = []
for i in range(numeroDeListas):
    listaDeListas.append([-1] * numeroVacas)
    # listaDeListas.append([-1 for _ in range(numeroVacas)]) #TODO: aprender como funciona esta estrctura

# Calcular listas de posiciones (en camion si / no) posibles
posicion = 0
listaActual = 0
subirACamion = True
while posicion < numeroVacas:
    while listaActual < numeroDeListas:
        if listaActual % (2 ** (numeroVacas - posicion - 1)) == 0:
            subirACamion = not subirACamion
        if subirACamion:
            listaDeListas[listaActual][posicion] = 1
        else:
            listaDeListas[listaActual][posicion] = 0
        listaActual += 1
    posicion += 1
    listaActual = 0

# Crear una lista y copiar dentro las listas con exceso de peso
listasADescartar = []
for lista in listaDeListas:
    pesoDeLista = 0
    for posicion in range(len(lista)):
        if lista[posicion] == 1:
            pesoDeLista += pesosDeVacas[posicion]
    if pesoDeLista > pesoMaximoCamion:
        listasADescartar.append(lista)

# Descartar las listas de exceso de peso de la lista de listas
for lista in listasADescartar:
    listaDeListas.remove(lista)

# Encontrar la lista con mayor produccion de leche por dia
lechePorDiaMax = 0
listaConLechePorDiaMax = []
for lista in listaDeListas:
    lechePorDia = 0
    for posicion in range(len(lista)):
        if lista[posicion] == 1:
            lechePorDia += lechePorDiaPorVaca[posicion]
    if lechePorDia > lechePorDiaMax:
        lechePorDiaMax = lechePorDia
        listaConLechePorDiaMax = lista

print(lechePorDiaPorVaca)
lecheTotal = 0
for posicion in range(len(listaConLechePorDiaMax)):
    if listaConLechePorDiaMax[posicion] == 1:
        lecheTotal += lechePorDiaPorVaca[posicion]

print(listaConLechePorDiaMax)
print(lecheTotal)
