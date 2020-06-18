# Cómo ejecutar el código

- Necesitamos [Python](https://www.python.org/) para poder ejectuar el código, aunque si no lo tenemos instalado sería recomendable instalar [anaconda](https://www.anaconda.com/products/individual) ya que incluye Python y es más flexible a la hora de añadir y modificar diferentes librerias o versiones para diferentes proyectos.

- Una vez instalado abrir la consola o terminal, dirigirse al directorio donde se encuentra el archivo _binario.py_ y introducir el comando **python binario.py** y el programa se ejecutará.

- Nos pedirá que introduzcamos un número decimal, y se mostrará en la consola los 1s y 0s de un número binario que es equivalente al decimal introducido.

# Pasos seguidos para resolver la tarea

- Para poder encontrar el equivalente de un número decimal en binario, debemos primero saber cuantos bits son necesarios para representar el valor decimal dado. Ya que cada bit es equivalente a 2^posición (si empezamos a contar la posición desde la derecha y empezando con el número cero), el programa suma los números desde la derecha y cuando el valor que representan es igual o mayor al número introducido, paramos y sabemos que los bits contados son suficientes para representar el número.

- Para ver cuales de los bits tienen que estar encendidos (1) o apagados (0), empezamos desde la izquierda. Mantendremos una suma del valor de los bits que hemos puesto a 1, empezando desde 0. Si poniendo el bit actual la suma es mayor al número introducido, lo dejamos a 0, en caso contrario, lo ponemos a 0. Al llegar al bit de la derecha, hemos puesto los bits en su posición necesaria para representar el valor.
