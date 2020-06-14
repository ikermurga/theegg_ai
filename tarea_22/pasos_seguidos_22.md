# Cómo ejecutar el código

- Necesitamos [Python](https://www.python.org/) para poder ejectuar el código, aunque si no lo tenemos instalado sería recomendable instalar [anaconda](https://www.anaconda.com/products/individual) ya que incluye Python y es más flexible a la hora de añadir y modificar diferentes librerias o versiones para diferentes proyectos.

- Una vez instalado abrir la consola o terminal, dirigirse al directorio donde se encuentra el archivo _vacas.py_ y introducir el comando **python vacas.py** y el programa se ejecutará.

- Nos pedirá que introduzcamos una serie de valores correpondientes al número de vacas totales, peso máximo del camión y valores individuales de peso por vaca y de litros por vaca. Una vez introducidos todos los valores, se mostrará la cantidad máxima de litros de leche que podemos conseguir con los datos introducidos, y el grupo de vacas con el que se obtiene ese máximo.

# Pasos seguidos para resolver la tarea

- Para la solución, empecé por investigar sobre el problema concreto, encontrando un problema de algoritmos llamado Knapsack o mochila. En [este video](https://www.youtube.com/watch?v=vdVpRjO7g84) hay una explicación sobre una solución posible. Aunque no utilice el agoritmo de ir creando diferentes ramas para crear las diferentes combinaciones posibles, fue una buena pista de que el primer objetivo tenía que ser crear todas las diferentes posibilidades de grupos. Una vez creados los diferentes grupos, simplemente sería cuestión de comprobar que el peso total del grupo no fuera mayor que el peso máximo del camión y obtener el grupo con mayor litros por día (se habla de estos dos aspectos en el video también).

- Investigando sobre cómo hacer las combinaciones posibles en Python, encontre [este enlace](https://realpython.com/python-itertools/) en el que se habla sobre el paquete itertools de Python. Siguiendo los diferentes ejemplos que mencionaba encontre el modo de precisamente crear todas las combinaciones posibles. Siguiendo los ejemplos poco a poco en la página mencionada y combinándolo con las ideas del video mencionado antes es como conseguir llegar a la solución en el programa. Para mayor detalle de partes específicas del programa, leer los comentarios en el propio código.

- Para comprobar que funciona correctamente podemos utilizar los siguientes datos:

  - Datos con 6 vacas, mejor grupo consta de las vacas 1, 4, 5 y 6 con 93 litros

    - Total vacas: 6
    - Peso máximo del camion: 700
    - Vaca 1, 360 kilos, 40 litros por día
    - Vaca 2, 250 kilos, 35 litros por día
    - Vaca 3, 400 kilos, 43 litros por día
    - Vaca 4, 180 kilos, 28 litros por día
    - Vaca 5, 50 kilos, 12 litros por día
    - Vaca 6, 90 kilos, 13 litros por día

  - Datos con 8 vacas, mejor grupo consta de las vacas 2, 3, 4, 5 y 6 con 188 litros

    - Total vacas: 8
    - Peso máximo del camion: 1000
    - Vaca 1, 223 kilos, 30 litros por día
    - Vaca 2, 243 kilos, 34 litros por día
    - Vaca 3, 100 kilos, 28 litros por día
    - Vaca 4, 200 kilos, 45 litros por día
    - Vaca 5, 200 kilos, 31 litros por día
    - Vaca 6, 155 kilos, 50 litros por día
    - Vaca 7, 300 kilos, 29 litros por día
    - Vaca 8, 150 kilos, 1 litros por día

  - Datos con 10 vacas, mejor grupo consta de las vacas 1, 2, 3, 4, 5, 6, 8 y 9 con 320 litros

    - Total vacas: 10
    - Peso máximo del camion: 2000
    - Vaca 1, 340 kilos, 45 litros por día
    - Vaca 2, 355 kilos, 50 litros por día
    - Vaca 3, 223 kilos, 34 litros por día
    - Vaca 4, 243 kilos, 39 litros por día
    - Vaca 5, 130 kilos, 29 litros por día
    - Vaca 6, 240 kilos, 40 litros por día
    - Vaca 7, 260 kilos, 30 litros por día
    - Vaca 8, 155 kilos, 52 litros por día
    - Vaca 9, 302 kilos, 31 litros por día
    - Vaca 10, 130 kilos, 1 litros por día
