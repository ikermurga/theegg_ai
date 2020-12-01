def comprobar_secuencia(secuencia):
    if len(secuencia) < 1:
        return False

    for base in secuencia:
        if base != 'A' and base != 'C' and base != 'G' and base != 'T':
            return False
    return True


def obtener_secuencia_de_usuario():
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


def pedir_inputs():
    secuencia_1 = obtener_secuencia_de_usuario()
    secuencia_2 = obtener_secuencia_de_usuario()
    return (secuencia_1, secuencia_2)
