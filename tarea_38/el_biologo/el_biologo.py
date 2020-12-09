from inputs_cadenas import pedir_inputs
from extraer_secuencias import obtener_secuencia_comun_mas_larga


def main():
    '''
    El programa de El Biólogo se divide en dos partes principales, por un lado obtener los input del usuario (las cadenas de las bases A, C, G ó T) y por otro encontrar la secuencia común más larga entre ambas. Se han extraido las funciones que corresponden a cada parte a pedir_inputs() y obtener_secuencia_comun_mas_larga(). Por lo tanto esta función obtiene dos cadenas de bases mediante inputs al usuario y después calcula la secuencia común más larga entre ellos.

    Finalmente, mostramos el resultado del cálculo de la secuencia común más larga. Antes de mostrar la cadena más larga que coincide, comprobamos que la cadena no sea una cadena vacía ya que eso indicaría que no hay ningún tipo de secuencia que coincida y mostramos un mensaje correspondiente.
    '''
    secuencias_a_comparar = pedir_inputs()
    secuencia_comun = obtener_secuencia_comun_mas_larga(secuencias_a_comparar)
    if len(secuencia_comun) > 1:
        print(f'La secuencia común más larga es: {secuencia_comun}')
    else:
        print('No hay secuencia común entre ambas cadenas')


if __name__ == "__main__":
    main()
