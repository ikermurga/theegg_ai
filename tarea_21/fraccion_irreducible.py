def main():
    decimal = obtener_numero_decimal_de_usuario()
    (numerador, denominador) = convertir_en_fraccion(decimal)

    factores_numerador = calcular_factores(numerador)
    factores_denominador = calcular_factores(denominador)

    (factores_numerador, factores_denominador) = eliminar_elementos_comunes(
        factores_numerador, factores_denominador)

    numerador_reducido = numero_desde_factores(factores_numerador)
    denominador_reducido = numero_desde_factores(factores_denominador)

    print(numerador_reducido, "/", denominador_reducido)


def obtener_numero_decimal_de_usuario():
    '''
    La función pide un número entre el 0.0001 y el 0.9999 por
    consola al usuario. Si introduce un número que no está
    dentro de este rango le vuelve a pedir el número hasta
    que introduzca uno correcto. Cuando el usuario introduce
    un número correcto, la función devuelve ese número.
    '''
    numero = 0
    while numero < 0.0001 or 0.9999 < numero:
        numero = float(
            input("Introduce un número entre el 0.0001 y el 0.9999: "))
        if numero < 0.0001 or 0.9999 < numero:
            print(
                "El número no se encuentra dentro del rango indicado (4 decimales máximo).\n")
    return numero


def convertir_en_fraccion(decimal):
    '''
    La función recibe un número decimal y devuelve
    un numerador y un denominador de una fracción
    calculada multiplicando el decimal por diez
    elevado a un número equivalente a la cantidad
    de números decimales
    '''
    numeros_decimales = contar_decimales(decimal)
    denominador = 10 ** numeros_decimales
    numerador = int(decimal * denominador)
    return (numerador, denominador)


def contar_decimales(numero):
    ''' 
    Contamos el número de decimales que contiene el número
    a partir de que mientras el numero no sea igual a
    si mismo sin decimales, multiplicamos por 10
    el numero de veces que tengamos que multiplicar por 10
    será el número de decimales que tiene
    '''
    total_decimales = 0
    while numero != numero//1:
        total_decimales += 1
        numero *= 10
    if total_decimales > 4:
        total_decimales = 4
    return total_decimales


def calcular_factores(numero):
    '''
    Obtenemos los factores de las que consta el número
    pasado a la función y los devolvemos en forma de lista
    '''
    factor_actual = 2
    factores = []
    while numero > 1:
        if numero % factor_actual == 0:
            numero /= factor_actual
            factores.append(factor_actual)
        else:
            factor_actual += 1
    return factores


def eliminar_elementos_comunes(lista1, lista2):
    '''
    La función recibe dos listas, quita los elementos
    comunes en ambas y devuelve las dos listas
    '''
    posicion = 0
    while posicion < len(lista1):
        elemento = lista1[posicion]
        if elemento in lista2:
            lista1.remove(elemento)
            lista2.remove(elemento)
            # Ya que hemos quitado un elemento de la lista que
            # estamos recorriendo, restamos uno a la posición
            # para continuar desde el siguiente elemento
            posicion -= 1
        posicion += 1
    return (lista1, lista2)


def numero_desde_factores(factores):
    '''
    La función calcula un número a partir de multiplicar los
    números en la lista de factores que recibe
    '''
    resultado = 1
    for factor in factores:
        resultado *= factor
    return resultado


if __name__ == "__main__":
    main()
