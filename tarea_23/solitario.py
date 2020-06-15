import itertools as it
import random


def random_seed():
    return .5


def ordenar_baraja():
    baraja = list(map(str, [*range(1, 53)]))
    baraja.extend(['A', 'B'])
    random.shuffle(baraja, random_seed)
    return baraja


def mover_carta(baraja, valor, puestos):
    posicion_original = baraja.index(valor)
    nueva_posicion = posicion_original + puestos
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


baraja = ordenar_baraja()
# baraja = ['3', 'A', 'B', '8', '9', '6']
# baraja = ['A', '7', '2', 'B', '9', '4', '1']
# print(baraja)
# mover_carta(baraja, 'A', 1)
# print(baraja)
# mover_carta(baraja, 'B', 2)
# print(baraja)
# baraja = [2, 4, 6, 'B', 5, 8, 7, 1, 'A', 3, 9]
# baraja = ['B', 5, 8, 7, 1, 'A', 3, 9]
baraja = ['B', 5, 8, 7, 1, 'A']
print(baraja)
baraja = mover_cartas_por_comodines(baraja)
print(baraja)
