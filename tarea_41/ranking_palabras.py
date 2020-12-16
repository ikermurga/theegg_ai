import re
import locale
locale.setlocale(locale.LC_ALL, '')


def main():
    texto = obtener_texto()
    if texto == None:
        return

    conteo = contar_caracteres(texto)
    mostrar_conteos_caracteres(*conteo)

    mostrar_separacion()

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
    # Se utiliza locale.strxfrm para ordenar alfabeticamente con las
    # tildes etc
    palabras_clasificadas.sort(
        key=lambda p: (-p['ocurrencias'], locale.strxfrm(p['palabra'])))

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


def obtener_texto():
    try:
        # Utilizamos encoding='utf8' para que muestre correctamente las palabras con tilde etc en consola
        with open('texto.txt', 'r', encoding='utf8') as file:
            texto = file.read()
        return texto
    except FileNotFoundError:
        print('Debes tener un archivo llamado "texto.txt" en la carpeta donde se está ejecutando el programa.')
        return None


def mostrar_separacion():
    print('\n----\n')


if __name__ == "__main__":
    main()
