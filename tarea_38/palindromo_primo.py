# TODO: diagrama de flujo!
# TODO: memoization para optimizar
# TODO: tests con pytest?

def esPrimo(numero):
    factor = 2
    while factor < numero/2:
        if numero % factor == 0:
            return False
        factor += 1
    return True


def esPalindromo(numero):
    numero_texto = str(numero)
    numero_invertido = numero_texto[::-1]
    if numero_texto == numero_invertido:
        return True
    else:
        return False


numero = int(input("Introduce el número: "))
while True:
    if esPalindromo(numero) and esPrimo(numero):
        print(numero)
        break
    print(f'{numero} descartado')
    numero += 1
