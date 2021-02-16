import time


def main():
    '''
    Hemos definido dos funciones para calcular la suma del 1 a
    n. Una de ellas funciona de modo lineal (es decir, tiene que
    hacer un número de operaciones constante relativo a el
    número de entradas, en este caso n) y otro que lo calcula de
    modo constante (es decir, el número de operaciones que tiene
    que realizar no varía según la entrada cambie).

    Empezamos con el valor de un millón en la variable cantidad.
    Hacemos un bucle que recorreremos cuatro veces, en el cual
    guardamos el tiempo inicial, ejecutamos la suma lineal y vemos
    la diferencia en el tiempo (obteniendo así el tiempo de computo
    de ejecutar la función suma_lineal cuando la cantidad es de
    un millón. Después hacemos lo mismo con la función suma_constante,
    y mostramos tanto el resultado de la suma como el tiempo
    transcurrido en cada una de las funciones. Al final del bucle
    multiplicamos cantidad por 10 y repetimos el proceso.

    De este modo obtenemos en pantalla el tiempo necesitado para
    computar las cantidades de un millón, diez millones, cien
    millones y mil millones por cada función y vemos cómo la
    función de suma_lineal necesita cada vez diez veces más de
    tiempo para el cálculo (ya que al ser lineal el tiempo se
    incrementa de modo lineal relativa a la cantidad).
    '''
    cantidad = 1_000_000

    for _ in range(4):
        t0 = time.time()
        suma1 = suma_lineal(cantidad)
        t1 = time.time()
        suma2 = suma_constante(cantidad)
        t2 = time.time()

        print(f'Cantidad es igual a {cantidad:,}')
        print(
            f'\tEl resultado de la suma lineal es:\n\t\t{int(suma1)}')
        print(
            f'\tEl tiempo de computo de la suma lineal es de:\n\t\t{t1-t0:.3f} segundos.')
        print(
            f'\tEl resultado de la suma constante es:\n\t\t{int(suma2)}')
        print(
            f'\tEl tiempo de computo de la suma constante es de:\n\t\t{t2-t1:.3f} segundos.')
        print()

        cantidad *= 10


def suma_lineal(n):
    '''
    Para calcular la suma de los números enteros entre
    el 1 y n de modo lineal, sumamos en bucle los
    números entre el 1 y n. Para ello utilizamos un
    bucle for con un rango entre 1 y n+1 (ya que
    range empieza por defecto desde el 0 y acaba en
    uno menos que el segundo parámetro).
    '''
    suma = 0
    for numero in range(1, n + 1):
        suma += numero
    return suma


def suma_constante(n):
    '''
    Para calcular las suma de los números enteros entre
    el 1 y n de modo constante, dividimos n entre 2 y lo 
    multiplicamos por n más 1.
    '''
    return (n / 2) * (n + 1)


if __name__ == '__main__':
    main()
