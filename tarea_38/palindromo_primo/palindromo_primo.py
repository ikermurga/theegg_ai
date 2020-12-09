def main():
    numero = obtener_valor_inicial()

    while True:
        if es_palindromo(numero) and es_primo(numero):
            print(numero)
            break
        numero += 1


def es_palindromo(numero):
    numero_texto = str(numero)
    numero_invertido = numero_texto[::-1]
    return numero_texto == numero_invertido


def es_primo(numero):
    factor = 2
    while factor < numero:
        if numero % factor == 0:
            return False
        factor += 1
    return True


def obtener_valor_inicial():
    while True:
        try:
            numero = int(input("Introduce el número: "))
            if numero < 1:
                print('Se debe introducir un número mayor a cero.')
            else:
                return numero
        except ValueError:
            print('Se debe introducir un número entero.')


if __name__ == "__main__":
    main()
