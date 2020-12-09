# TODO: añadir ejemplo de entradas y salidas en el readme
# texto = 'this is a test'
# texto = 'foobar'
# texto = 'all your base'

def main():
    '''
    La función principal pide al usuario el número de frases que quiere invertir
    y después en bucle pregunta al usuario cada frase y la va guardando invertida
    en la lista _frases_. Una vez tiene las frases necesarias, las muestra con
    el formato _Case #{indice}:_ pedido en el ejercicio.

    No se hace ningún tipo de validación de las frases introducidas por el usuario
    ya que estas pueden ser de cualquier tipo. Simplemente, si la frase no contiene
    un espacio, se muestra tal como fue introducida por el usuario.

    La función auxiliar obtener_numero_frases se encarga de que el usuario haya 
    introducido un valor correcto para indicar el número de frases que quiere
    invertir.
    '''
    numero_frases = obtener_numero_frases()
    frases = []

    for _ in range(numero_frases):
        texto = input('Introduce la frase a invertir: ')
        texto = invertir_palabras(texto)
        frases.append(texto)

    for indice, frase in enumerate(frases):
        print(f'Case #{indice + 1}: {frase}')


def obtener_numero_frases():
    '''
    Esta función pide por input al usuario el número de frases que quiere invertir.
    Sólo acepta que se introduzca un número entero positivo mayor que cero. Una vez
    el usuario introduce un valor correcto, la función devuelve el valor.
    '''
    while True:
        try:
            numero_frases = int(
                input('Introduce el número de frases a invertir: '))
            if numero_frases > 0:
                break
            else:
                print('Debes introducir un número mayor que el cero.')
        except ValueError:
            print('Debes introducir un número entero.')

    return numero_frases


def invertir_palabras(texto):
    '''
    Invierte el orden de las palabras de un texto que recibe (contando como palabras aquellas separadas por espacios) y devuelve el resultado de esta operación.

    El bucle inicial crea una lista de palabras, separando las partes del texto donde se encuentra un espacio. Una vez tenemos la lista, la invertimos utilizando la función reverse (que al no devolver una lista tenemos que una vez más convertir en una lista con list()) y unimos las palabras mediante espacios con el método .join().
    '''
    # Utilizamos indice_actual para indicar la posición actual al recorrer la
    # cadena de texto
    indice_actual = 0
    # En la lista palabras guardaremos las palabras que vamos a extraer de
    # la cadena de texto original
    palabras = []

    # Obtenemos una lista cuyos elementos son los caracteres separados por un espacio en el texto original
    while True:
        try:
            # Utilizamos indice_espacio para guardar la posición del caracter de espacio
            # que hemos encontrado en el texto
            indice_espacio = texto.index(' ', indice_actual)

            # Cuando encontramos un espacio en la cadena de texto, extraemos los caracteres
            # desde la posición actual hasta la posición del espacio, así estamos obteniendo
            # una "palabra"
            palabras.append(texto[indice_actual: indice_espacio])

            # Movemos el índice actual a la posición posterior al espacio utilizado para
            # delimitar la última palabra que hemos obtenido
            indice_actual = indice_espacio + 1

        # Si el método index no encuentra el caracter indicado, lanza una excepción
        # del tipo ValueError. En este punto sabemos que sólo queda una palabra ya
        # que no hay ningún espacio más en la cadena restante.
        except ValueError:
            palabras.append(texto[indice_actual:])
            break

    # Invertimos el orden de las palabras y los volvemos a unir con el método join, indicado que se utilice un espacio entre las palabras al unirlas.
    palabras_invertidas = " ".join(list(reversed(palabras)))
    return palabras_invertidas


if __name__ == "__main__":
    main()
