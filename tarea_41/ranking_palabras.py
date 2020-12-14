import re

# Utilizamos encoding='utf8' para que muestre correctamente las palabras con tilde etc en consola
with open('texto.txt', 'r', encoding='utf8') as file:
    texto = file.read()

patron_caracteres = r'.'
patron_caracteres_sin_espacios_en_blanco = r'[^\s]'
patron_palabras = r'\w+\b'

caracteres = re.findall(patron_caracteres, texto)
caracteres_sin_espacios_en_blanco = re.findall(
    patron_caracteres_sin_espacios_en_blanco, texto)
palabras = re.findall(patron_palabras, texto)

print(f'El número de caracteres es: {len(caracteres)}')
print(
    f'El número de caracteres sin contar los espacios en blanco es: {len(caracteres_sin_espacios_en_blanco)}')
print(f'El número de palabras es: {len(palabras)}')
print()

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

for palabra in palabras_clasificadas:
    texto_palabra = palabra['palabra']
    num_palabra = palabra['ocurrencias']
    print(f'{texto_palabra}, aparece {num_palabra} {"veces" if num_palabra > 1 else "vez"}')
