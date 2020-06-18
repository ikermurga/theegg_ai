# Cómo ejecutar el código

- Necesitamos [Python](https://www.python.org/) para poder ejectuar el código, aunque si no lo tenemos instalado sería recomendable instalar [anaconda](https://www.anaconda.com/products/individual) ya que incluye Python y es más flexible a la hora de añadir y modificar diferentes librerias o versiones para diferentes proyectos.

- Una vez instalado abrir la consola o terminal, dirigirse al directorio donde se encuentra el archivo _solitario.py_ (y que en el mismo directorio se encuentren también los archivos baraja.py, conversor_letras_numeros.py y generador.py y introducir el comando **python solitario.py** y el programa se ejecutará.

- Nos pedirá que eligamos si queremos cifrar o descifrar un mensaje (introduciendo C o D respectivamente) y después nos pedirá el texto que queremos cifrar o descifrar.

# Pasos seguidos para resolver la tarea

- El proceso que he seguido para llegar a la solución a sido desde el principio crear una 'baraja' (una lista con los números del 1-52 y 'A' y 'B'. Después escribí el código de cada paso y comprobaba que la baraja estaba en la posición que tendría que estar al acabar el paso (para algunos pasos usaba una lista con menos números para comprobar más fácilmente que los pasos se seguían correctamente). De este modo ha sido un proceso de ir comprobando cada paso hasta que funcionaba correctamente y pasar al siguiente, hasta llegar al último paso.

- Para comprobar que funciona correctamente podemos pedir cifrar e introducir un texto. Ver el texto que sale como resultado. Después volver a ejecutar el programa pero esta vez elegir descifrar e introducir el resultado del anterior. Debería darnos el texto original que hemos introducido al cifrar.
