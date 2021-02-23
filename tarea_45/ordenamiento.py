def ordenamiento_por_mezcla(lista):
    """ Recibe una lista de elementos y la ordena utilizando el algoritmo de ordenamiento por mezcla.

    Utiliza la función mezclar para unir y ordenar los elementos una vez se han separado.

    Devuelve la lista ordenada según el orden indicado por la función mezclar.
    """
    if len(lista) < 2:
        return lista

    centro = len(lista) // 2

    return mezclar(
        izquierda=ordenamiento_por_mezcla(lista[:centro]),
        derecha=ordenamiento_por_mezcla(lista[centro:]))


def mezclar(izquierda, derecha):
    """ Recibe dos listas de elementos comparables con el operador menor que o igual. Cualquiera de las listas puede ser una lista vacía. 

    Devuelve una lista compuesta de los elementos en ambas listas ordenados de menor a mayor.
    """
    if len(izquierda) == 0:
        return derecha

    if len(derecha) == 0:
        return izquierda

    resultado = []
    indice_izquierda = indice_derecha = 0

    while len(resultado) < len(izquierda) + len(derecha):
        if izquierda[indice_izquierda] <= derecha[indice_derecha]:
            resultado.append(izquierda[indice_izquierda])
            indice_izquierda += 1
        else:
            resultado.append(derecha[indice_derecha])
            indice_derecha += 1

        if indice_derecha == len(derecha):
            resultado += izquierda[indice_izquierda:]
            break

        if indice_izquierda == len(izquierda):
            resultado += derecha[indice_derecha:]
            break

    return resultado
