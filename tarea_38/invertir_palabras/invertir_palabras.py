# TODO: diagrama de flujo!
def main():
    # TODO : preguntar por input cuantas frases se van a voltear

    # texto = 'this is a test'
    # texto = 'foobar'
    texto = 'all your base'  # TODO pedir por input
    # TODO: añadir formato de "Case #: ..." a salidas
    print(invertir_palabras(texto))


def invertir_palabras(texto):
    '''
    Invierte el orden de las palabras de un texto que recibe (contando como palabras aquellas separadas por espacios) y devuelve el resultado de esta operación.
    '''
    indice_actual = 0
    indice_espacio = 0
    palabras = []

    while True:
        try:
            indice_espacio = texto.index(' ', indice_actual)
            palabras.append(texto[indice_actual: indice_espacio])
            indice_actual = indice_espacio + 1
        except Exception:  # TODO la exception especifica
            palabras.append(texto[indice_actual:])
            break

    palabras_invertidas = " ".join(list(reversed(palabras)))
    return palabras_invertidas


if __name__ == "__main__":
    main()
# TODO checkear si funciona con cadena vacia
