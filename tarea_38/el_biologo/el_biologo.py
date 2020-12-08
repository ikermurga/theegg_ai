# TODO: diagrama de flujo!

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

# texto_secuencia_1 = 'CTA'
# texto_secuencia_2 = 'GGG'
# # salida correcta = No hay secuencia común entre ambas cadenas
# CASOS PARA TESTS ACABAN AQUI

from inputs_cadenas import pedir_inputs
from extraer_secuencias import obtener_secuencia_comun_mas_larga


def main():
    secuencias_a_comparar = pedir_inputs()
    secuencia = obtener_secuencia_comun_mas_larga(secuencias_a_comparar)
    if len(secuencia) > 1:
        print(f'La secuencia común más larga es: {secuencia}')
    else:
        print('No hay secuencia común entre ambas cadenas')


if __name__ == "__main__":
    main()
