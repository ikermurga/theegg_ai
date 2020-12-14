# Cómo ejecutar el código

-   Necesitamos [Python](https://www.python.org/) para poder ejectuar el código, aunque si no lo tenemos instalado sería recomendable instalar [anaconda](https://www.anaconda.com/products/individual) ya que incluye Python y es más flexible a la hora de añadir y modificar diferentes librerias o versiones para diferentes proyectos.

-   Una vez instalado abrir la consola o terminal, dirigirse al directorio donde se encuentra el archivo **ranking_palabras.py** y introducir el comando **python ranking_palabras.py** y el programa se ejecutará.

# Pasos seguidos para resolver la tarea

-   Para poder utilizar expresiones regulares en Python, se utiliza la librería _re_ que ya viene en el propio lenguaje.

-   El programa cogera el texto de un archivo llamado texto.txt que se encuentre en la misma carpeta.

-   La primera parete de la tarea consiste en simplemente contar el número de caracteres y palabras. He optado ya que no estaba seguro por mostrar tanto los caracteres totales y los caracteres sin contar los caracteres de espacios en blanco (espacios, tabulaciones, saltos de línea, ...). Tanto para estos dos como para contar el número de palabras totales es suficiente con expresiones regulares sencillas y después contar la longitud de los resultados.

-   Para la última parte en cambio tenía dos opciones. Por un lado, una vez tenía todas las palabras en python podia utilizar el propio python para contar el número de repeticiones. Por otro lado, podía intentar obtener únicamente una copia única de las palabras y después buscarlo
