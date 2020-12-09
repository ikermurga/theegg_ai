# TODO: diagrama de flujo!

# TODO : preguntar por input cuantas frases se van a voltear

# texto = 'this is a test'
# texto = 'foobar'
texto = 'all your base'  # TODO pedir por input

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

palabras_invertidas = palabras[::-1]  # TODO usar reverse en vez de esto?
for palabra in palabras_invertidas:
    # TODO: añdir formato de "Case #: ..." a salidas
    print(f'{palabra} ', end='')

# TODO main
