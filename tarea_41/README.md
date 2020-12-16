# Cómo ejecutar el código

-   Necesitamos [Python](https://www.python.org/) para poder ejectuar el código, aunque si no lo tenemos instalado sería recomendable instalar [anaconda](https://www.anaconda.com/products/individual) ya que incluye Python y es más flexible a la hora de añadir y modificar diferentes librerias o versiones para diferentes proyectos.

-   Una vez instalado abrir la consola o terminal, dirigirse al directorio donde se encuentra el archivo **ranking_palabras.py** y introducir el comando **python ranking_palabras.py** y el programa se ejecutará. Es importante ejectuar python desde el mismo directorio donde está el archivo texto.txt ya que el programa cargará el texto a analizar de este archivo.

# Pasos seguidos para resolver la tarea

-   Para poder utilizar expresiones regulares en Python, se ha utilizado la librería _re_ que ya viene en el propio lenguaje. Se han creado patrones de búsqueda de regex que después se han utilizado con _re.findall()_ para encontrar las ocurrencias en el texto. El programa obtiene el texto de un archivo llamado texto.txt que se debe encuentrar en la misma carpeta.

-   La primera parte de la tarea consiste en simplemente contar el número de caracteres y palabras. He optado ya que no estaba seguro por mostrar tanto los caracteres totales y los caracteres sin contar los caracteres de espacios en blanco (espacios, tabulaciones, saltos de línea, ...). Tanto para estos dos como para contar el número de palabras totales es suficiente con expresiones regulares sencillas y después contar la longitud de los resultados.

-   Para la última parte en cambio tenía dos opciones. Por un lado, una vez tenía todas las palabras en python podia utilizar el propio python para contar el número de repeticiones. Por otro lado, podía intentar obtener únicamente una copia única de las palabras y después buscarlo. Para ello he utilizado una expresión de regex más compleja que solamente daba resultado si no encontraba la misma palabra más adelante en el texto. Una vez tenía las palabras únicas he vuelto a hacer otro regex por cada una de las palabras para ver así el número de veces que aparece cada una. De tener que cumplir el objetivo en un programa "real" posiblemente habría utilizado un bucle para recorrer la lista de palabras y apuntar el número de repeticiones, pero al ser un ejercicio sobre expresiones regulares he optado por utilizar este sistema.

-   Uno de los mayores problemas lo encontré al intentar ordenar las palabrás, al ver que palabras como _último_ aparecian despues de palabras como _zona_. Para solucionar esto he utilizado la libreria locale (que viene también con python sin necesidad de instarlo externamente) y he utilizado el método _strxfrm_ para que ordenara las palabras correctamente aún con acentos.
