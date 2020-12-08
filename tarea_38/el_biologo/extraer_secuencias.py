def medir_secuencia_comun_desde_indices(indice_1, indice_2, secuencia_1, secuencia_2):
    '''
    cada vez que dos letras coincidan, comprobar longitud de la
    cadena desde esas posiones (extraer esto a una funcion)
    '''
    numero_letras_iguales = 0

    while (indice_1 < len(secuencia_1)
            and indice_2 < len(secuencia_2)
            and (secuencia_1[indice_1] == secuencia_2[indice_2])):
        numero_letras_iguales += 1
        indice_1 += 1
        indice_2 += 1

    return numero_letras_iguales


def obtener_secuencia_comun_mas_larga(secuencias_a_comparar):
    '''
    si la longitud es mayor que la actual, extraer esa secuencia
    y guardarla como la secuencia_comun_max
    '''
    secuencia_1, secuencia_2 = secuencias_a_comparar
    secuencia_comun_max = ''

    for posicion_1, letra_1 in enumerate(secuencia_1):
        for posicion_2, letra_2 in enumerate(secuencia_2):
            if letra_1 == letra_2:
                numero_letras_iguales = medir_secuencia_comun_desde_indices(
                    posicion_1, posicion_2,
                    secuencia_1, secuencia_2
                )

                if numero_letras_iguales > len(secuencia_comun_max):
                    secuencia_comun_max = secuencia_1[posicion_1:posicion_1 +
                                                      numero_letras_iguales]

    return secuencia_comun_max
