'''
Definir dos funciones para calcular la suma del 1 a n números.
Una de ellas sumando uno a uno cada número, y otra aplicando 
la fórmula de la suma aritmética de Gaus: (n / 2) * (n + 1)
'''

import time


def suma_lineal(n):
    suma = 0
    for i in range(n+1):
        suma += i
    return suma


def suma_constante(n):
    return (n / 2) * (n + 1)


cantidad = 1000000

for i in range(4):
    t0 = time.time()
    suma1 = suma_lineal(cantidad)
    t1 = time.time()
    suma2 = suma_constante(cantidad)
    t2 = time.time()

    print(f'{suma1} - {t1-t0}')
    print(f'{suma2} - {t2-t1}')

    cantidad *= 10
