# TODO: Comentar cada método y la función principal, tanto en los archivos secundarios como en el principal!

from inputs_cadenas import pedir_inputs
from extraer_secuencias import obtener_secuencia_comun_mas_larga


def main():
    '''
    '''
    secuencias_a_comparar = pedir_inputs()
    secuencia_comun = obtener_secuencia_comun_mas_larga(secuencias_a_comparar)
    if len(secuencia_comun) > 1:
        print(f'La secuencia común más larga es: {secuencia_comun}')
    else:
        print('No hay secuencia común entre ambas cadenas')


if __name__ == "__main__":
    main()
