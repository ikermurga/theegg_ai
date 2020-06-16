from conversor_letras_numeros import ConversorLetrasNumeros
from generador import GeneradorSolitario


def main():
    conversor = ConversorLetrasNumeros()
    generador = GeneradorSolitario(conversor)

    # TODO: pedir texto al usuario. antes preguntar si cifrar o descifrar
    # hacer que el resultado se muestre en bloques de 5?
    texto = 'HOLA MUNDO'
    clave = generador.generar_letras_secuencia_de_clave(len(texto))
    cifrado = cifrar(texto, clave, conversor)
    print(cifrado)

    descifrado = descifrar(cifrado, clave, conversor)
    print(descifrado)


def cifrar(texto, clave, conversor):
    numeros_original = lista_numerica_desde_texto(texto, conversor)
    numeros_clave = lista_numerica_desde_texto(clave, conversor)
    numeros_combinados = sumar_numeros(numeros_original, numeros_clave)
    texto_cifrado = texto_desde_lista_numerica(numeros_combinados, conversor)
    return texto_cifrado


def descifrar(texto, clave, conversor):
    numeros_original = lista_numerica_desde_texto(texto, conversor)
    numeros_clave = lista_numerica_desde_texto(clave, conversor)
    numeros_combinados = restar_numeros(numeros_original, numeros_clave)
    texto_cifrado = texto_desde_lista_numerica(numeros_combinados, conversor)
    return texto_cifrado


def texto_desde_lista_numerica(numeros, conversor):
    resultado = ''
    for numero in numeros:
        letra = conversor.transformar_valor_a_letra(numero)
        resultado += letra
    return resultado


def lista_numerica_desde_texto(texto, conversor):
    resultado = []
    for letra in texto:
        if letra != ' ':
            resultado.append(conversor.transformar_letra_a_valor(letra))
    return resultado


def sumar_numeros(lista1, lista2):
    resultado = []
    i = 0
    while i < len(lista1):
        valor = (lista1[i] + lista2[i]) % 26
        resultado.append(valor)
        i += 1
    return resultado


def restar_numeros(lista1, lista2):
    resultado = []
    i = 0
    while i < len(lista1):
        if lista1[i] < lista2[i]:
            lista1[i] += 26
        valor = lista1[i] - lista2[i]
        resultado.append(valor)
        i += 1
    return resultado


if __name__ == "__main__":
    main()
