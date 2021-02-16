# Cómo ejecutar el código

- Necesitamos [Python](https://www.python.org/) para poder ejectuar el código, aunque si no lo tenemos instalado sería recomendable instalar [anaconda](https://www.anaconda.com/products/individual) ya que incluye Python y es más flexible a la hora de añadir y modificar diferentes librerias o versiones para diferentes proyectos.

- Una vez instalado abrir la consola o terminal, dirigirse al directorio donde se encuentra el archivo **lineal_vs_constante.py** y introducir el comando **python lineal_vs_constante.py** y el programa se ejecutará.

# Pasos seguidos para resolver la tarea

- Hemos definido dos funciones para calcular la suma del 1 a n. Una de ellas funciona de modo lineal (es decir, tiene que hacer un número de operaciones constante relativo a el número de entradas, en este caso n) y otro que lo calcula de modo constante (es decir, el número de operaciones que tiene que realizar no varía según la entrada cambie).

- Para calcular la suma de los números enteros entre el 1 y n de modo lineal, sumamos en bucle los números entre el 1 y n. Para ello utilizamos un bucle for con un rango entre 1 y n+1 (ya que range empieza por defecto desde el 0 y acaba en uno menos que el segundo parámetro).

- Para calcular las suma de los números enteros entre el 1 y n de modo constante, dividimos n entre 2 y lo multiplicamos por n más 1.

- Empezamos con el valor de un millón en la variable cantidad. Hacemos un bucle que recorreremos cuatro veces, en el cual guardamos el tiempo inicial (usando [el método time() la librería time de Python](https://docs.python.org/3/library/time.html#time.time)), ejecutamos la suma lineal y vemos la diferencia en el tiempo (obteniendo así el tiempo de computo de ejecutar la función **suma_lineal** cuando la cantidad es de un millón). Después hacemos lo mismo con la función **suma_constante**, y mostramos tanto el resultado de la suma como el tiempo transcurrido en cada una de las funciones. Al final del bucle multiplicamos cantidad por 10 y repetimos el proceso.

- De este modo mostraremos en consola el tiempo necesitado para computar las cantidades de un millón, diez millones, cien millones y mil millones por cada función y vemos cómo la función de **suma_lineal** necesita cada vez diez veces más de tiempo para el cálculo (ya que al ser lineal el tiempo se incrementa de modo lineal relativo a la cantidad), mientras que el tiempo necesario para **suma_constante** no varía (y es más rápida que lo que puede medir la librería **time** de python).
