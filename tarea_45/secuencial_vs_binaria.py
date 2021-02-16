def main():
    '''
    Creamos una lista, la ordenamos (utilizando el ordenamiento de selección) y
    después buscamos el número 875 en la misma lista que no incluye el número,
    tanto utilizando la búsqueda secuencial como la binaria.

    Buscar un número no incluido en la lista nos costará el mayor número de 
    iteraciones por ellas para llegar al resultado y las funciones de
    busqueda_secuencial y busqueda_binaria devolverán precisamente el
    número de iteraciones junto con el índice donde se encontró el elemento
    (o None en caso de no encontrarse) así como  el número de iteraciones
    para llegar al resultado.

    Finalmente mostramos los datos en consola.
    '''
    lista = [3, 56, 21, 33, 874, 123, 66, 1000,
             23, 45, 65, 56]

    lista_ordenada = ordenamiento_seleccion(lista)
    print(f'La lista ordenada es:\n{lista_ordenada}\n')

    elemento_a_buscar = 875
    indice_secuencial, iteraciones_secuencial = busqueda_secuencial(
        lista_ordenada, elemento_a_buscar)
    indice_binaria, iteraciones_binaria = busqueda_binaria(
        lista_ordenada, elemento_a_buscar)

    print(
        f'El indice del elemento {elemento_a_buscar} resultante de la búsqueda secuencial es el {indice_secuencial}')
    print(
        f'El número de interaciones de la búsqueda secuencial han sido: {iteraciones_secuencial}')
    print()
    print(
        f'El indice del elemento {elemento_a_buscar} resultante de la búsqueda secuencial es el {indice_binaria}')
    print(
        f'El número de interaciones de la búsqueda binaria han sido: {iteraciones_binaria}')


def busqueda_secuencial(lista, item):
    '''
    Recorre la lista elemento a elemento hasta que encuentra
    el item recibido. Antes de comprobar cada elemento se
    añade 1 a la variable de iteraciones, que se devolverá
    junto con el índice donde se encontró el item en la
    lista (o None en caso de que item no sea parte de la lista)
    '''
    iteraciones = 0
    for indice, element in enumerate(lista):
        iteraciones += 1
        if element == item:
            return (indice, iteraciones)
    return (None, iteraciones)


def busqueda_binaria(lista, item):
    '''

    '''
    iteraciones = 0
    bajo = 0
    alto = len(lista) - 1
    while bajo <= alto:
        iteraciones += 1
        mid = (bajo + alto) // 2
        guess = lista[mid]
        if guess == item:
            return (mid, iteraciones)
        if guess > item:
            alto = mid - 1
        else:
            bajo = mid + 1
    return (None, iteraciones)


def ordenamiento_seleccion(lista):
    '''

    '''
    lista_ordenada = []
    for _ in range(len(lista)):
        menor = lista[0]
        indice_menor = 0
        for indice in range(1, len(lista)):
            if lista[indice] < menor:
                menor = lista[indice]
                indice_menor = indice
        lista_ordenada.append(lista.pop(indice_menor))
    return lista_ordenada


if __name__ == '__main__':
    main()
