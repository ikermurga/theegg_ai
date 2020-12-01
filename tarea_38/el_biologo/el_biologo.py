# TODO: diagrama de flujo!
# TODO: tests con pytest?

# CASOS PARA TESTS COMIENZAN AQUI
# texto_secuencia_1 = 'ATGTCTTCCTCGA'
# texto_secuencia_2 = 'TGCTTCCTATGAC'
# salida correcta = 'CTTCCT'

# texto_secuencia_1 = 'ctgactga'
# texto_secuencia_2 = 'actgagc'
# # salida correcta = actga

# texto_secuencia_1 = 'cgtaattgcgat'
# texto_secuencia_2 = 'cgtacagtagc'
# # salida correcta = cgta
# CASOS PARA TESTS ACABAN AQUI

from inputs_cadenas import pedir_inputs


def obtener_secuencia_comun_mas_larga(secuencias_a_comparar):
    secuencia_1, secuencia_2 = secuencias_a_comparar
    secuencia_comun_max = ''

    for posicion_1, letra_1 in enumerate(secuencia_1):
        for posicion_2, letra_2 in enumerate(secuencia_2):
            if letra_1 == letra_2:

                # cada vez que dos letras coincidan, comprobar longitud de la
                # cadena desde esas posiones (extraer esto a una funcion)
                numero_letras_iguales = 0
                indice_1 = posicion_1
                indice_2 = posicion_2
                while (indice_1 < len(secuencia_1)
                       and indice_2 < len(secuencia_2)
                       and (secuencia_1[indice_1] == secuencia_2[indice_2])):
                    numero_letras_iguales += 1
                    indice_1 += 1
                    indice_2 += 1

                # si la longitud es mayor que la actual, extraer esa secuencia
                # y guardarla como la secuencia_comun_max
                # (poner la parte de extraer una cadena a partir de posicion
                # y longitud como una funcion aparte)
                if numero_letras_iguales > len(secuencia_comun_max):
                    secuencia_comun_max = secuencia_1[posicion_1:posicion_1 +
                                                      numero_letras_iguales]

    return secuencia_comun_max


def main():
    secuencias_a_comparar = pedir_inputs()
    secuencia = obtener_secuencia_comun_mas_larga(secuencias_a_comparar)
    print(f'La secuencia común más larga es: {secuencia}')


if __name__ == "__main__":
    main()
