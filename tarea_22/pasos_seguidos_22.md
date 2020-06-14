# Cómo ejecutar el código

- Necesitamos [Python](https://www.python.org/) para poder ejectuar el código, aunque si no lo tenemos instalado sería recomendable instalar [anaconda](https://www.anaconda.com/products/individual) ya que incluye Python y es más flexible a la hora de añadir y modificar diferentes librerias o versiones para diferentes proyectos.

- Una vez instalado abrir la consola o terminal, dirigirse al directorio donde se encuentra el archivo _vacas.py_ y introducir el comando **python vacas.py** y el programa se ejecutará.

- Nos pedirá que introduzcamos una serie de valores correpondientes al número de vacas totales, peso máximo del camión y valores individuales de peso por vaca y de litros por vaca. Una vez introducidos todos los valores, se mostrará la cantidad máxima de litros de leche que podemos conseguir con los datos introducidos, y el grupo de vacas con el que se obtiene ese máximo.

# Pasos seguidos para resolver la tarea

- Para la solución, empecé por investigar sobre el problema concreto, encontrando un problema de algoritmos llamado Knapsack o mochila. En [este video](https://www.youtube.com/watch?v=vdVpRjO7g84) hay una explicación sobre una solución posible. Aunque no utilice el agoritmo de ir creando diferentes ramas para crear las diferentes combinaciones posibles, fue una buena pista de que el primer objetivo tenía que ser crear todas las diferentes posibilidades de grupos. Una vez creados los diferentes grupos, simplemente sería cuestión de comprobar que el peso total del grupo no fuera mayor que el peso máximo del camión y obtener el grupo con mayor litros por día (se habla de estos dos aspectos en el video también).

- Investingando sobre cómo hacer las combinaciones posibles en Python, encontre [este enlace](https://realpython.com/python-itertools/) en el que se habla sobre el paquete itertools de Python. Siguiendo los diferentes ejemplos que mencionaba encontre el modo de precisamente crear todas las combinaciones posibles. Siguiendo los ejemplos poco a poco en la página mencionada y combinándolo con las ideas del video mencionado antes es como conseguir llegar a la solución en el programa. Para mayor detalle de partes específicas del programa, leer los comentarios en el propio código.
