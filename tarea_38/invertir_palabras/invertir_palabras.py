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

    El bucle inicial crea una lista de palabras, separando las partes del texto donde se encuentra un espacio. Una vez tenemos la lista, la invertimos utilizando la función reverse (que al no devolver una lista tenemos que una vez más convertir en una lista con list()) y unimos las palabras mediante espacios con el método .join().
    '''
    indice_actual = 0
    indice_espacio = 0
    palabras = []

    # Obtenemos una lista cuyos elementos son los caracteres separados por un espacio en el texto original
    while True:
        try:
            indice_espacio = texto.index(' ', indice_actual)
            palabras.append(texto[indice_actual: indice_espacio])
            indice_actual = indice_espacio + 1
        except Exception:  # TODO la exception especifica
            palabras.append(texto[indice_actual:])
            break

    # Invertimos el orden de las palabras y los volvemos a unir con el método join, indicado que se utilice un espacio entre las palabras al unirlas.
    palabras_invertidas = " ".join(list(reversed(palabras)))
    return palabras_invertidas


if __name__ == "__main__":
    main()
# TODO checkear si funciona con cadena vacia
