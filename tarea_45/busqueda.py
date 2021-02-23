def busqueda_secuencial(lista, item):
    """ Recibe una lista ordenada y un elemento a buscar, que busca utilizando el algoritmo de búsqueda secuencial.

    Devuelve un tuplo con el índice del elemento en la lista (o None en caso de que no se encuentre) y el número de iteraciones necesarias para obtener el resultado.
    """
    iteraciones = 0
    for indice, element in enumerate(lista):
        iteraciones += 1
        if element == item:
            return (indice, iteraciones)
    return (None, iteraciones)


def busqueda_binaria(lista, item):
    """ Recibe una lista ordenada y un elemento a buscar, que busca utilizando el algoritmo de búsqueda binaria.

    Devuelve un tuplo con el índice del elemento en la lista (o None en caso de que no se encuentre) y el número de iteraciones necesarias para obtener el resultado.
    """
    iteraciones = 0
    bajo = 0
    alto = len(lista) - 1
    while bajo <= alto:
        iteraciones += 1
        centro = (bajo + alto) // 2
        guess = lista[centro]
        if guess == item:
            return (centro, iteraciones)
        if guess > item:
            alto = centro - 1
        else:
            bajo = centro + 1
    return (None, iteraciones)
