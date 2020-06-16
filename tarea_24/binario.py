def main():
    decimal = int(input("Introduce un número: "))
    bits = convertir_a_binario(decimal)
    for bit in bits:
        print(f'{bit} ', end='')


def convertir_a_binario(decimal):
    maximo = 0
    posicion_bit = 0
    numero_bits = 0
    while maximo < decimal:
        maximo += 2 ** posicion_bit
        numero_bits += 1
        posicion_bit += 1

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


if __name__ == "__main__":
    main()
