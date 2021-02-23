from busqueda import busqueda_secuencial, busqueda_binaria
from ordenamiento import ordenamiento_por_mezcla


def main():
    """ Crea una lista de elementos, la ordena, busca un elemento tanto con búsqueda secuencial como con búsqueda binaria y muestra tanto el índice del elemento buscado como el número de iteraciones que ha necesitado cada algoritmo de búsqueda para obtener el resultado.

    No devuelve nada.
    """
    lista = [3, 56, 21, 33, 874, 123, 66, 1000,
             23, 45, 65, 56]

    lista_ordenada = ordenamiento_por_mezcla(lista)
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
        f'El indice del elemento {elemento_a_buscar} resultante de la búsqueda binaria es el {indice_binaria}')
    print(
        f'El número de interaciones de la búsqueda binaria han sido: {iteraciones_binaria}')


if __name__ == '__main__':
    main()
