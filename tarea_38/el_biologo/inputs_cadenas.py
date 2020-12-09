def pedir_inputs():
    '''
    Función que pide por input dos cadenas de bases al usuario y las devuelve como un tuplo. Para pedir cada una de ellas se utiliza la función obtener_secuencia_de_usuario()
    '''
    secuencia_1 = obtener_secuencia_de_usuario()
    secuencia_2 = obtener_secuencia_de_usuario()
    return (secuencia_1, secuencia_2)


def obtener_secuencia_de_usuario():
    '''
    Al pedir al usuario las cadenas que se analizarán, se convierten en mayúsculas y se comprueba que la secuencia cumpla los requisitos del progamar (utilizando la función comprobar_secuencia()). Mientras la cadena sea incorrecta, se le volverá a pedir al usuario que la introduzca. Una vez se introduzca una cadena correcta, la función devolverá la misma.
    '''
    while True:
        secuencia = input('Introduce una secuencia como una cadena '
                          'de caracteres de sus bases(compuesto '
                          'por A, C, G o T):')
        secuencia = secuencia.upper()
        if comprobar_secuencia(secuencia):
            break
        print('Cada secuencia debe ser una cadena de texto de al menos un'
              'caracter y compuesta únicamente por los caracteres A, C, G o T')
    return secuencia


def comprobar_secuencia(secuencia):
    '''
    Función que comprueba que el string recibido no sea un string vacío y que ninguno de los caracteres sea diferente de A, C, G y T, ya que esos son los únicos caracteres que admitimos. En el caso de que se incumpla alguna normal la función devuelve False, en caso contrario True.
    '''
    if len(secuencia) < 1:
        return False

    for base in secuencia:
        if base != 'A' and base != 'C' and base != 'G' and base != 'T':
            return False
    return True
