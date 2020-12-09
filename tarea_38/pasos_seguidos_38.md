# Cómo ejecutar el código

-   Necesitamos [Python](https://www.python.org/) para poder ejectuar el código, aunque si no lo tenemos instalado sería recomendable instalar [anaconda](https://www.anaconda.com/products/individual) ya que incluye Python y es más flexible a la hora de añadir y modificar diferentes librerias o versiones para diferentes proyectos.

-   Ya que la tarea consta de tres ejercicios diferentes, cada uno de ellos se encuentra en su carpeta correspondiente (el_biologo, invertir_palabras y palindromo_primo).

-   Una vez instalado Python, abrir la consola o terminal, dirigirse al directorio donde se encuentra el archivo principal del proyecto (**el_biologo.py** en el caso de el_biologo, **invertir_palabras.py** en el caso de invertir_palabras y **palindromo_primo** en el caso de palindromo_primo) y introducir el comando **python nombre_archivo_principal.py** para ejecutar el programa correspondiente.

# Pasos seguidos para resolver la tarea

-   En todos los casos realicé el diagrama de flujo utilizando la página de [Flowchart Maker](https://app.diagrams.net/). Estos diagramas se muestran en este archivo .md dentro de la sección en la que se mencionan los pasos seguidos para resolver cada tarea, pero se puede hacer click en el mismo para poder ver una versión ampliada.

# Pasos seguidos para resolver la sub-tarea El Biólogo

-   El programa de El Biólogo se divide en dos partes principales, por un lado obtener los input del usuario (las cadenas de las bases A, C, G ó T) y por otro encontrar la secuencia común más larga entre ambas. Se han extraido las funciones de esas partes a sus archivos correspondientes (**inputs_cadenas.py** para los inputs y **extraer_secuencias.py** para encontrar la secuencia común más larga).

-   Al pedir al usuario las cadenas que se analizarán, se convierten en mayúsculas y se comprueba que ningún caracter de la cadena sea diferente de A, C, G y T, ya que esos son los únicos caracteres que admitimos. Mientras no se cumpla esta condición, siempre se volverá a pedir al usuario que introduzca la cadena otra vez. Una vez el usuario haya introducido dos cadenas de bases correctas, podemos utilizar estas cadenas para encontrar su sub-cadena común más larga.

-   Al analizar las cadenas queremos encontrar el mayor número de caracteres continuos que sean iguales en ambas. Para comenzar decimos que la cadena que coincide es '', es decir una cadena vacía, con longitud cero. Se hacen dos bucles, por un lado empezando desde la primera base (o primer caracter) de la primera cadena y por cada base de la primera cadena lo comparamos a las bases de la segunda cadena. Si en algún momento encontramos dos bases que coinciden, hemos encontrado dos "sub-cadenas" que coinciden (aunque sólo sea de longitude de una base). Por lo tanto, a partir de esas posiciones en las cadenas contamos las bases siguientes que coinciden hasta encontrar una que sea diferente. Eso nos indica la longitud de la subcadena que coincide a partir de esa posición. Si la longitud calculada es más larga que la guardada anteriormente (que al inicio del programa es '' y longitud cero) se sobreescribe la cadena guardad. Este proceso continua hasta que hayamos recorrido completamente ambas cadenas, y de este modo al finalizar los bucles tendríamos la cadena más larga guardada.

-   Finalmente, mostramos el resultado de haber la función explicada en el punto anterior. Antes de mostrar la cadena más larga que coincide, comprobamos que la cadena no sea una cadena vacía ya que eso indicaría que no hay ningún tipo de secuencia que coincida y mostramos un mensaje correspondiente.

-   Este es el diagrama de flujo correspondiente al programa:

![Diagrama de flujo del programa El Biólogo](diagrama-el-biologo.png)

-   Para comprobar el correcto funcionamiento del programa, he utilizado estos inputs que se mostraban en el enunciado del ejercicio, añadiendo uno más en el que no hay una cadena que coincida.

    -   Entrada y salidas 1:

        -   texto_secuencia_1 = 'ATGTCTTCCTCGA'
        -   texto_secuencia_2 = 'TGCTTCCTATGAC'
        -   salida correcta = 'CTTCCT'

    -   Entrada y salidas 2:

        -   texto_secuencia_1 = 'ctgactga'
        -   texto_secuencia_2 = 'actgagc'
        -   salida correcta = actga

    -   Entrada y salidas 3:

        -   texto_secuencia_1 = 'cgtaattgcgat'
        -   texto_secuencia_2 = 'cgtacagtagc'
        -   salida correcta = cgta

    -   Entrada y salidas 4:
        -   texto_secuencia_1 = 'CTA'
        -   texto_secuencia_2 = 'GGG'
        -   salida correcta = No hay secuencia común entre ambas cadenas

# Pasos seguidos para resolver la sub-tarea Invertir Palabras

# Pasos seguidos para resolver la sub-tarea Palíndromo Primo
