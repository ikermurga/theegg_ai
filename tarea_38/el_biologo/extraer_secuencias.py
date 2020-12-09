def obtener_secuencia_comun_mas_larga(secuencias_a_comparar):
    '''
    Esta función analiza un tuplo con dos cadenas de bases recibidas y encuentra la subcadena común más larga.

    Al analizar las cadenas queremos encontrar el mayor número de caracteres continuos que sean iguales en ambas. Para comenzar decimos que la cadena que coincide es '', es decir una cadena vacía, con longitud cero. Se hacen dos bucles, por un lado empezando desde la primera base (o primer caracter) de la primera cadena y por cada base de la primera cadena lo comparamos a las bases de la segunda cadena. Si en algún momento encontramos dos bases que coinciden, hemos encontrado dos "sub-cadenas" que coinciden (aunque sólo sea de longitude de una base).

    Pasando las dos cadenas y las posiciones de las bases que coinciden a la función auxiliar medir_secuencia_comun_desde_indices() recibiremos la longitud de la cadena común. Si la longitud calculada es más larga que la guardada anteriormente (que al inicio del programa es '' y longitud cero) se sobreescribe la cadena guardada. Este proceso continua hasta que hayamos recorrido completamente ambas cadenas, y de este modo al finalizar los bucles tendríamos la cadena más larga guardada.

    La función devuelve esta cadena.
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


def medir_secuencia_comun_desde_indices(indice_1, indice_2, secuencia_1, secuencia_2):
    '''
    Esta función recibe dos índices y cadenas que indican dos caracteres que coinciden en ambas cadenas. A partir de esas posiciones en las cadenas contamos las bases siguientes que coinciden hasta encontrar una que sea diferente. Eso nos indica la longitud de la subcadena que coincide a partir de esa posición.

    La función devuelve la longitud calculada.
    '''
    numero_letras_iguales = 0

    while (indice_1 < len(secuencia_1)
            and indice_2 < len(secuencia_2)
            and (secuencia_1[indice_1] == secuencia_2[indice_2])):
        numero_letras_iguales += 1
        indice_1 += 1
        indice_2 += 1

    return numero_letras_iguales
