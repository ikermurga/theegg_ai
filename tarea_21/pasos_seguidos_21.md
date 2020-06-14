# Cómo ejecutar el código

- Necesitamos [Python](https://www.python.org/) para poder ejectuar el código, aunque si no lo tenemos instalado sería recomendable instalar [anaconda](https://www.anaconda.com/products/individual) ya que incluye Python y es más flexible a la hora de añadir y modificar diferentes librerias o versiones para diferentes proyectos.

- Una vez instalado abrir la consola o terminal, dirigirse al directorio donde se encuentra el archivo _fraccion_irreducible.py_ y introducir el comando **python fraccion_irreducible.py** y el programa se ejecutará. Nos pedirá que introduzcamos un número en la consola y si introducimos uno en el rango correcto nos devolverá la fracción irreducible equivalente al número decimal introducido.

# Pasos seguidos para resolver la tarea

- Pedimos al usuario un número entre 0,0001 y 0,9999. Hacemos un bucle para que si introduce un número que no está en ese rango volvamos a pedir otro número hasta que introduzca un número en el rango correcto.

- Vemos cuantos números decimales a introducido. Empezaremos creando una fracción inicial que después reduciremos. Para crear esta fracción inicial, crearemos el numerador multiplicando el número por una potencia de 10 que eliminará los decimales (si por ejemplo introduce el 0,25 lo multiplicaremos por 100 y tendremos el 25 de numerador). Para mantener el mismo número el denominador será la misma potencia de diez por el que hemos multiplicado el número (siguiendo el ejemplo de 0,25 el numerador será el 25 y el denominador el 100).

- Una vez creada esta fracción inicial, calcularemos los factores tanto del numerador como del denominador. Para ello veremos si dividir el número por dos no da un resto (utilizando el operador de módulo). En caso de que sea así, añadimos el número a la lista de factores y dividimos el número por ese factor. En caso contrario, pasamos al siguiente número (al 3, 4, ...) y volvemos a repetir la operación, hasta que el número que estamos diviendo sea igual a 1 (en este momento ya no quedan más factores).

- Cuando tenemos los factores tanto del numerador como el denominador en dos listas, queremos comparar las listas y eliminar los números que aparezcan en ambas. De este modo, estamos simplificando los factores de los números y eliminandolos llegaremos a sus factores comunes más pequeños.

- Finalmente, una vez tenemos los factores más simples tanto del numerador como del denominador, los multiplicamos entre ellos para obtener tanto el numerador reducido como el denominador reducido, y obtenemos así la fracción reducida.
