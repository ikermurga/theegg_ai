def main():
    lista = [3, 56, 21, 33, 874, 123, 66, 1000,
             23, 45, 65, 56]
    elemento_a_buscar = 875
    lista_ordenada = ordenamiento_seleccion(lista)
    print(lista_ordenada)
    indice_secuencial, iteraciones_secuencial = busqueda_secuencial(
        lista_ordenada, elemento_a_buscar)
    indice_binaria, iteraciones_binaria = busqueda_binaria(
        lista_ordenada, elemento_a_buscar)
    print(
        f'El indice del elemento {elemento_a_buscar} resultante de la búsqueda secuencial es el {indice_secuencial}')
    print(
        f'El número de interaciones de la búsqueda secuencial han sido: {iteraciones_secuencial}')
    print(
        f'El indice del elemento {elemento_a_buscar} resultante de la búsqueda secuencial es el {indice_binaria}')
    print(
        f'El número de interaciones de la búsqueda binaria han sido: {iteraciones_binaria}')


def busqueda_secuencial(lista, item):
    iteraciones = 0
    for indice, element in enumerate(lista):
        iteraciones += 1
        if element == item:
            return (indice, iteraciones)
    return (None, iteraciones)


def busqueda_binaria(lista, item):
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
    lista_ordenada = []
    for _ in range(len(lista)):
        indice_menor = encontrar_menor(lista)
        lista_ordenada.append(lista.pop(indice_menor))
    return lista_ordenada


def encontrar_menor(lista):
    menor = lista[0]
    indice_menor = 0
    for indice in range(1, len(lista)):
        if lista[indice] < menor:
            menor = lista[indice]
            indice_menor = indice
    return indice_menor


if __name__ == '__main__':
    main()
