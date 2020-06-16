from conversor_letras_numeros import ConversorLetrasNumeros
from generador import GeneradorSolitario


def main():
    conversor = ConversorLetrasNumeros()
    generador = GeneradorSolitario(conversor)

    texto_original = 'HOLA MUNDO'
    ristra = generador.generar_letras_secuencia_de_clave(len(texto_original))

    numeros_original = lista_numerica_desde_texto(texto_original, conversor)
    numeros_ristra = lista_numerica_desde_texto(ristra, conversor)
    numeros_combinados = sumar_numeros(numeros_original, numeros_ristra)
    texto_cifrado = texto_desde_lista_numerica(numeros_combinados, conversor)
    print(texto_cifrado)


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


if __name__ == "__main__":
    main()
