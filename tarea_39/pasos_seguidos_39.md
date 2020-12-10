# Cómo ejecutar el código

-   Ya que esta tarea pedia crear una serie de archivos de Actividad de Packet Tracer (.pkt). Para poder comprobarlos hace falta tener instalado Packet Tracer. Para instalar Packet Tracer se pueden seguir las instrucciones en [este video](https://www.youtube.com/watch?v=aR032ROLdro) a partir de 4m10s.

# Pasos seguidos para resolver la tarea

-   La tarea consta de cinco ejercicios diferentes, cada uno de ellos se encuentra en su archivo **.pkt** correspondiente, dentro de la carpeta **ejercicios**. Cada uno de los ejercicios constaba del objetivo y también de instrucciones precisas (en forma de texto y video) sobre cómo realizarlo. Por lo tanto, para entender bien los ejercicios se trataba de hacer varias pruebas e investigar el por qué de cada una de las partes de los ejercicios, aunque estas pruebas no aparecen en los archivos resueltos ya que sólo he subido la solución pedida:

    -   Ejercicio a: **Red con servidor web y servidor de DNS** guardado como **a-red-con-servidor-web-y-servidor-de-dns.pkt**. Para comprobar que funcione correctamente, abrirlo, hacer click en tanto PC0 como PC1, en la pestaña _Desktop_ ir a _Web Browser_ e introducir *www.mipagina.com* en el navegador. Debería mostrarse una página que contiene el texto _Página web en el servidor Web_.

    -   Ejercicio b: **Red con servidor DHCP** guardado como **b-red-con-servidor-dhcp.pkt**. Para comprobar que todo funciona correctamente, se pueden enviar paquetes UDP simples entre los pcs haciendo click en el icono del sobre con el + y después clickando en el pc de origen y el de destino. Se puede comprobar que los pcs obtienen su IP a través de DHCP clickando en cualquiera de ellos haciendo click en _Ip Configuration_ y viendo que está seleccionado DHCP. Se puede seleccionar _Static_ para resetear el ip del pc y volver a elegir _DHCP_ para ver cómo se le asigna una ip dinámicamente.

    -   Ejercicio c: **Red VLAN básica** guardado como **c-red-vlan-basica.pkt**. Para comprobar que todo funciona correctamente, se pueden enviar paquetes UDP simples entre los pcs haciendo click en el icono del sobre con el + y después clickando en el pc de origen y el de destino. En esta red deberían poder comunicarse los asignados a la misma VLAN por lo tanto los pcs PC0, PC1, PC4 y PC5 se pueden enviar mensajes entre ellos pero no con los pcs PC2, PC3, PC6 y PC7 (que se podrán también comunicar unicamente entre ellos).

    -   Ejercicio d: **Unir dos redes VLAN con un router** guardado como **d-unir-dos-redes-vlan-con-un-router.pkt**. Para comprobar que todo funciona correctamente, se pueden enviar paquetes UDP simples entre los pcs haciendo click en el icono del sobre con el + y después clickando en el pc de origen y el de destino. En este caso no se comunican solamente entre sí los pcs en la misma VLAN, sino que a través del router se comunica cualquier pc con los demás. Esto se puede apreciar si observamos el camino del paquete en modo simulación en vez de en tiempo real.

    -   Ejercicio e: **Enrutamiento estático** guardado como **e-enrutamiento-estatico.pkt**. Para comprobar que todo funciona correctamente, se pueden enviar paquetes UDP simples entre los pcs haciendo click en el icono del sobre con el + y después clickando en el pc de origen y el de destino. Deberían poder comunicarse todos los PCs entre sí.
