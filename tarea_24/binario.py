def main():
    decimal = int(input("Introduce un número: "))
    bits = convertir_a_binario(decimal)
    for bit in bits:
        print(f'{bit} ', end='')


def convertir_a_binario(decimal):
    # Función que devuelve una lista de números
    # (siendo los números 1 o 0 ) que representan
    # los bits que se tienen que usar para mostrar
    # el valor decimal recibido
    numero_bits = calcular_numero_de_bits(decimal)
    bit_actual = numero_bits - 1
    bits = []
    valor_actual = 0
    while bit_actual >= 0:
        if valor_actual + 2**bit_actual <= decimal:
            valor_actual += 2 ** bit_actual
            bits.append(1)
        else:
            bits.append(0)
        bit_actual -= 1
    return bits


def calcular_numero_de_bits(decimal):
    # Función que calcula el número de bits
    # necesarios para representar el número
    # decimal recibido
    maximo = 0
    posicion_bit = 0
    numero_bits = 0
    while maximo < decimal:
        maximo += 2 ** posicion_bit
        numero_bits += 1
        posicion_bit += 1
    return numero_bits


if __name__ == "__main__":
    main()
