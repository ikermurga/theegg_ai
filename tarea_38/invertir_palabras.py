# texto = 'this is a test'
# texto = 'foobar'
texto = 'all your base'

continuar = True
indice_actual = 0
indice_espacio = 0
palabras = []
while continuar:
    try:
        indice_espacio = texto.index(' ', indice_actual)
        palabras.append(texto[indice_actual: indice_espacio])
        indice_actual = indice_espacio + 1
    except Exception:
        palabras.append(texto[indice_actual:])
        continuar = False
palabras_invertidas = palabras[::-1]
for palabra in palabras_invertidas:
    print(f'{palabra} ', end='')
