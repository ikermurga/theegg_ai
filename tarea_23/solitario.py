import random


def random_seed():
    return .5


def ordenar_baraja():
    baraja = list(map(str, [*range(1, 53)]))
    baraja.extend(['A', 'B'])
    #random.shuffle(baraja, random_seed)
    return baraja


def mover_carta(baraja, valor, puestos):
    posicion_original = baraja.index(valor)
    nueva_posicion = posicion_original + puestos
    if nueva_posicion >= len(baraja):
        nueva_posicion += 1
    # TODO: fails if not looping through back of deck
    nueva_posicion %= len(baraja)
    baraja.remove(valor)
    baraja.insert(nueva_posicion, valor)


def mover_cartas_por_comodines(baraja):
    posicion_comodin_a = baraja.index('A')
    posicion_comodin_b = baraja.index('B')
    if posicion_comodin_a < posicion_comodin_b:
        primer_comodin = 'A'
        segundo_comodin = 'B'
        posicion_primer_comodin = posicion_comodin_a
        posicion_segundo_comodin = posicion_comodin_b
    else:
        primer_comodin = 'B'
        segundo_comodin = 'A'
        posicion_primer_comodin = posicion_comodin_b
        posicion_segundo_comodin = posicion_comodin_a

    primer_bloque = baraja[:posicion_primer_comodin]
    segundo_bloque = baraja[posicion_primer_comodin+1:posicion_segundo_comodin]
    tercer_bloque = baraja[posicion_segundo_comodin+1:]

    resultado = []
    resultado.extend(tercer_bloque)
    resultado.extend(primer_comodin)
    resultado.extend(segundo_bloque)
    resultado.extend(segundo_comodin)
    resultado.extend(primer_bloque)

    return resultado


def cortar_por_valor_ultima_carta(baraja):
    ultima_carta = baraja[-1]
    if ultima_carta != 'A' and ultima_carta != 'B':
        valor_ultima_carta = int(ultima_carta)
        primer_bloque = baraja[:valor_ultima_carta]
        segundo_bloque = baraja[valor_ultima_carta: -1]
        resultado = segundo_bloque
        resultado.extend(primer_bloque)
        resultado.append(ultima_carta)
        return resultado
    return baraja


def obtener_valor_de_letra(baraja):
    primera_carta = baraja[0]
    if primera_carta != 'A' and primera_carta != 'B':
        valor_primera_carta = int(primera_carta)
        carta_a_traducir = baraja[valor_primera_carta]
        if carta_a_traducir != 'A' and carta_a_traducir != 'B':
            valor_carta_a_traducir = int(carta_a_traducir)
            valor_carta_a_traducir = (valor_carta_a_traducir % 26)
            return valor_carta_a_traducir
    return None


def transformar_valor_a_letra(valor):
    letras = [
        'A', 'B', 'C', 'D', 'E',
        'F', 'G', 'H', 'I', 'J',
        'K', 'L', 'M', 'N', 'O',
        'P', 'Q', 'R', 'S', 'T',
        'U', 'V', 'W', 'X', 'Y',
        'Z'
    ]
    return letras[valor - 1]


def transformar_letra_a_valor(letra):
    letras = [
        'A', 'B', 'C', 'D', 'E',
        'F', 'G', 'H', 'I', 'J',
        'K', 'L', 'M', 'N', 'O',
        'P', 'Q', 'R', 'S', 'T',
        'U', 'V', 'W', 'X', 'Y',
        'Z'
    ]
    valor = letras.index(letra.upper()) + 1
    return valor


def generar_letras_secuencia_de_clave(numero_letras):
    # crear ristra de solitario
    letras = []
    baraja = ordenar_baraja()
    while len(letras) < numero_letras:
        mover_carta(baraja, 'A', 1)
        mover_carta(baraja, 'B', 2)
        baraja = mover_cartas_por_comodines(baraja)
        baraja = cortar_por_valor_ultima_carta(baraja)
        valor = obtener_valor_de_letra(baraja)
        if valor is not None:
            letra = transformar_valor_a_letra(valor)
            letras.append(letra)
    return letras


def texto_desde_lista_numerica(numeros):
    resultado = ''
    for numero in numeros:
        letra = transformar_valor_a_letra(numero)
        resultado += letra
    return resultado


def lista_numerica_desde_texto(texto):
    resultado = []
    for letra in texto:
        if letra != ' ':
            resultado.append(transformar_letra_a_valor(letra))
    return resultado


def sumar_numeros(lista1, lista2):
    resultado = []
    i = 0
    while i < len(lista1):
        valor = (lista1[i] + lista2[i]) % 26
        resultado.append(valor)
        i += 1
    return resultado


texto_original = 'CRYPTONOMICON'
ristra = generar_letras_secuencia_de_clave(len(texto_original))

numeros_original = lista_numerica_desde_texto(texto_original)
numeros_ristra = lista_numerica_desde_texto(ristra)
numeros_combinados = sumar_numeros(numeros_original, numeros_ristra)
texto_cifrado = texto_desde_lista_numerica(numeros_combinados)
print(texto_cifrado)
