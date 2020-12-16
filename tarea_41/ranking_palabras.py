import re
import locale


def main():
    '''
    Función de inicio del programa, primero intenta extraer el texto del archivo de texto, en caso de que no se obtenga una cadena de texto se acaba la ejecución.

    En caso de que se obtenga el texto, se cuentan los caracteres y despues se muestra el resultado en consola.

    Se muestra en consola una separación (tres guiones intercalados entre dos lineas vacías).

    Finalmente se calcula el número de palabras únicas que hay en el texto junto con el número de veces que aparecen en el texto y se muestran ordenados por el número de veces que aparecen y alfabéticamente.
    '''
    texto = obtener_texto()
    if texto == None:
        return

    conteo = contar_caracteres(texto)
    mostrar_conteos_caracteres(*conteo)

    mostrar_separacion()

    ranking = clasificar_palabras(texto)
    mostrar_palabras(ranking)


def contar_caracteres(texto):
    '''
    Recibe una cadena de texto y devuelve un tuplo con tres valores: el número de caracteres totales, el número de caracteres sin contar caracteres considerados espacios en blanco (espacios, tabuladores, saltos de linea, ...) y el número de palabras.

    Utiliza tres patrones de regex distintos que se ejecutan y se devuelve la longitud del vector, siendo esto el número de matches (resultados) que ha encontrado el regex en el texto.
    '''
    # Creamos los patrones utilizados en los regex
    patron_caracteres = r'.'
    patron_caracteres_sin_espacios_en_blanco = r'[^\s]'
    patron_palabras = r'\w+\b'

    # Utilizamos re.findall() para que se ejecute el regex
    # de los patrones en el texto
    caracteres = re.findall(patron_caracteres, texto)
    caracteres_sin_espacios_en_blanco = re.findall(
        patron_caracteres_sin_espacios_en_blanco, texto)
    palabras = re.findall(patron_palabras, texto)

    # Vemos la longitud de los vectores devueltos para
    # saber el número de coincidencias
    num_caracteres = len(caracteres)
    num_caracteres_sin_espacios_en_blanco = len(
        caracteres_sin_espacios_en_blanco)
    num_palabras = len(palabras)

    return (num_caracteres, num_caracteres_sin_espacios_en_blanco, num_palabras)


def clasificar_palabras(texto):
    '''
    Recibe una cadena de texto y devuelve una lista compuesta por diccionarios. En los diccionarios tenemos dos claves ('palabra' y 'ocurrencias', siendo la primera la palabra en si y la segunda el número de veces que aparece en el texto). La lista tendrá un diccionario por cada palabra única que se encuentre en el texto (se ignoran las diferencias de mayúsculas y minúsuculas) y la palabra se guardará en el formato de título (primera letra en mayúscula el resto en minúscula).

    Utilizamos un patrón de regex que solamente encontrará un resultado si no existe ese mismo texto más adelante (de este modo nos quedaremos con una lista de palabras únicas, es decir solo se guardará una de las palabras que se encuentran repetidas. En un bucle buscamos el número de veces que se repite la palabra en el texto (mirando la longitud del vector que devuelve la búsqueda de la palabra. En ambos casos utilizamos el flag re.IGNORECASE que sería el equivalente a /patrón regex/i en regex puro.

    A la hora de ordenar los resultados, queremos hacerlo en primer lugar por el número de veces que aparecen y en el caso de que el número sea igual en varias palabras ordenarlas alfabéticamente. Es por esto que pasamos una función (en formato lambda) en el key del sort para indicar a python en qué orden queremos que se haga el sort. En este caso queremos que sea orden inverso del número de ocurrencias (por eso lo convertimos en negativo) y después alfabéticamente. Para que python ordene correctamente las palabras con tildes, queremos utilizar la libreria locale, inicializandolo con .setlocale() y utilizando su método strxfrm() que tiene en cuenta precisamente los acentos y los ordena correctamente. Si no hicieramos esto, las letras con acentos se ordenarían despues de la z.
    '''
    # Encontramos las palabras únicas
    patron_palabras_unicas = r'(\w+\b)(?!.*\1\b)'
    palabras_unicas = re.findall(patron_palabras_unicas, texto, re.IGNORECASE)

    # Creamos una lista de palabras únicas con un diccionario con la palabra
    # obtenida y el número de veces que aparece en el texto
    palabras_clasificadas = []
    for palabra in palabras_unicas:
        num_ocurrencias = len(re.findall(f'{palabra}', texto, re.IGNORECASE))
        palabras_clasificadas.append(
            {'palabra': palabra.title(), 'ocurrencias': num_ocurrencias})

    # Ordenamos palabras por número de ocurrencias (de mayor a menor)
    # y después alfabeticamente por la palabra en sí.
    # Se utiliza locale.strxfrm para ordenar alfabeticamente con las
    # tildes etc, para poder utilizar strxfrm correctamente, iniciamos
    # locale con setlocale
    locale.setlocale(locale.LC_ALL, '')
    palabras_clasificadas.sort(
        key=lambda p: (-p['ocurrencias'], locale.strxfrm(p['palabra'])))

    return palabras_clasificadas


def mostrar_palabras(texto):
    '''
    Recibe una lista de diccionarios (con las claves 'palabra' y 'ocurrencias', siendo la primera la palabra en si y la segunda el número de veces que aparece en el texto) y los muestra en consola.
    '''
    for palabra in texto:
        texto_palabra = palabra['palabra']
        num_palabra = palabra['ocurrencias']
        print(
            f'{texto_palabra} aparece {num_palabra} {"veces" if num_palabra > 1 else "vez"}.')


def mostrar_conteos_caracteres(num_caracteres, num_caracteres_sin_espacios_en_blanco, num_palabras):
    '''
    Recibe tres valores: el número de caracteres totales, el número de caracteres sin contar caracteres considerados espacios en blanco (espacios, tabuladores, saltos de linea, ...) y el número de palabras. Muestra los valores en pantalla.
    '''
    print(f'El número de caracteres es: {num_caracteres}.')
    print(
        f'El número de caracteres sin contar los espacios en blanco es: {num_caracteres_sin_espacios_en_blanco}.')
    print(f'El número de palabras es: {num_palabras}.')


def obtener_texto():
    '''
    Obtiene el texto guardado en un archivo de tipo .txt llamado texto.txt que debe estar ubicado en la carpeta donde se esta ejecutando el script. En caso de que el archivo no exista, muestra un mensaje de error y devuelve None, en caso de que exista, devuelve el contenido del archivo como una cadena de texto.
    '''
    try:
        # Utilizamos encoding='utf8' para que muestre correctamente las palabras con tilde etc en consola
        with open('texto.txt', 'r', encoding='utf8') as file:
            texto = file.read()
        return texto
    except FileNotFoundError:
        print('Debes tener un archivo llamado "texto.txt" en la carpeta donde se está ejecutando el programa.')
        return None


def mostrar_separacion():
    '''
    Muestra en consola dos saltos de linea con unos guiones a modo de separación de datos que se muestran.
    '''
    print('\n----\n')


if __name__ == "__main__":
    main()
