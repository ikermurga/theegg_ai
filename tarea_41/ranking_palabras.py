import re


def main():
    texto = obtener_texto()

    conteo = contar_caracteres(texto)
    mostrar_conteos_caracteres(*conteo)

    ranking = clasificar_palabras(texto)
    mostrar_palabras(ranking)


def clasificar_palabras(texto):
    patron_palabras_unicas = r'(\w+\b)(?!.*\1\b)'
    palabras_unicas = re.findall(patron_palabras_unicas, texto, re.IGNORECASE)
    palabras_clasificadas = []
    for palabra in palabras_unicas:
        num_ocurrencias = len(re.findall(f'{palabra}', texto, re.IGNORECASE))
        palabras_clasificadas.append(
            {'palabra': palabra.lower(), 'ocurrencias': num_ocurrencias})

    # Ordenamos palabras por número de ocurrencias (de mayor a menor)
    # y después alfabeticamente por la palabra en sí
    palabras_clasificadas.sort(key=lambda p: (-p['ocurrencias'], p['palabra']))

    return palabras_clasificadas


def mostrar_palabras(texto):
    for palabra in texto:
        texto_palabra = palabra['palabra']
        num_palabra = palabra['ocurrencias']
        print(
            f'{texto_palabra}, aparece {num_palabra} {"veces" if num_palabra > 1 else "vez"}')


def contar_caracteres(texto):
    patron_caracteres = r'.'
    patron_caracteres_sin_espacios_en_blanco = r'[^\s]'
    patron_palabras = r'\w+\b'

    caracteres = re.findall(patron_caracteres, texto)
    caracteres_sin_espacios_en_blanco = re.findall(
        patron_caracteres_sin_espacios_en_blanco, texto)
    palabras = re.findall(patron_palabras, texto)

    num_caracteres = len(caracteres)
    num_caracteres_sin_espacios_en_blanco = len(
        caracteres_sin_espacios_en_blanco)
    num_palabras = len(palabras)

    return (num_caracteres, num_caracteres_sin_espacios_en_blanco, num_palabras)


def mostrar_conteos_caracteres(num_caracteres, num_caracteres_sin_espacios_en_blanco, num_palabras):
    print(f'El número de caracteres es: {num_caracteres}')
    print(
        f'El número de caracteres sin contar los espacios en blanco es: {num_caracteres_sin_espacios_en_blanco}')
    print(f'El número de palabras es: {num_palabras}')
    print()


def obtener_texto():
    # Utilizamos encoding='utf8' para que muestre correctamente las palabras con tilde etc en consola
    with open('texto.txt', 'r', encoding='utf8') as file:
        texto = file.read()
    return texto


if __name__ == "__main__":
    main()
