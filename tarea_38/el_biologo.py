# texto_secuencia_1 = 'ATGTCTTCCTCGA'
# texto_secuencia_2 = 'TGCTTCCTATGAC'
# salida correcta = 'CTTCCT'

# texto_secuencia_1 = 'ctgactga'
# texto_secuencia_2 = 'actgagc'
# # salida correcta = actga

# texto_secuencia_1 = 'cgtaattgcgat'
# texto_secuencia_2 = 'cgtacagtagc'
# # salida correcta = cgta

texto_secuencia_1 = 'ctgggccttgaggaaaactg'
texto_secuencia_2 = 'gtaccagtactgatagt'
# salida correcta = actg

secuencia_comun_max = ''
for posicion_1, letra_1 in enumerate(texto_secuencia_1):
    for posicion_2, letra_2 in enumerate(texto_secuencia_2):
        if letra_1 == letra_2:
            numero_letras_iguales = 0
            indice_1 = posicion_1
            indice_2 = posicion_2
            while indice_1 < len(texto_secuencia_1) and indice_2 < len(texto_secuencia_2) and (texto_secuencia_1[indice_1] == texto_secuencia_2[indice_2]):
                numero_letras_iguales += 1
                indice_1 += 1
                indice_2 += 1
            if numero_letras_iguales > len(secuencia_comun_max):
                secuencia_comun_max = texto_secuencia_1[posicion_1:posicion_1 +
                                                        numero_letras_iguales]
print("Secuencia común más larga es:")
print(secuencia_comun_max)
