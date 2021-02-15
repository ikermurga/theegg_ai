# Cómo ejecutar el código

-   Ya que se la tarea consta de crear una página, basta con abrir el archivo index.html con el navegador Chrome o Edge una vez descargados los archivos de la carpeta correspondiente. Ya que se utiliza el API SpeechRecognition de los navegadores, sólo funcionará en uno de los dos. Una vez abrimos el HTML en uno de los dos navegadores indicados, el propio navegador se encaragará de abrir los archivos correspondientes al leer el archivo _html_. Los archivos que utiliza el _html_ son varios, algunos que están incluidos en esta carpeta y otros externos (tales como código que se carga de _Bootstrap_ y utilizando la API de Google el video de YouTube).

-   Si simplemente abrimos el navegador, cada vez que digamos un comando se pedirá al usuario que autorice el uso del micrófono. Para evitar esto, tenemos que ejecutarlo en un servidor local. Para ejecutar un servidor local:

    -   Si tenemos Python instalado, podemos abrir la terminal y en la carpeta donde se encuentra el archivo _index.html_ introducir el comando `python -m http.server 8000` , esto iniciará un servidor local y podremos abrir el navegador y entrar en la dirección _localhost:8000_ para ver la página.
    -   Si utilizamos el editor Visual Studio Code, podemos descargarnos la extensión _Live Server_ y después hacer click derecho en el archivo _index.html_ y seleccionar _Abrir con Live Server_. De este modo se iniciará un servidor local y se abrirá el navegador con la página.

-   Ya que se reconocen los comandos de voz introducidos por micrófono, en caso de que los altavoces estén cerca del micrófono veremos como el audio del video es reconocido. Para evitar esto se pueden usar auriculares.

# Pasos seguidos para resolver la tarea

-   Para la estructura general de la página he utilizado Bootstrap, más específicamente el ejemplo de [Pricing](https://getbootstrap.com/docs/5.0/examples/pricing/) como punto de partida que luego he adaptado modificando el contenido de tanto la cabecera como el footer, y el mayor cambio ha sido en la sección de contenido principal.

-   Para los colores he utilizado colores de fondo y de letra sacados del esquema de colores de la página [Color Palettes](https://colorpalettes.net/color-palette-3535/), junto con el blanco.

-   Para añadir el video de YouTube y poder manejar los controles (para así poder ajustar el volumen) desde JavaScript, he utilizado la información disponible en [esta página de Google](https://developers.google.com/youtube/iframe_api_reference).

-   Para poder reconocer lo dicho por el usuario por micrófono he utilizado la información respecto a Speech Recognition API en [este video de Wes Bos](https://www.youtube.com/watch?v=0mJC0A72Fnw). También he mirado el código en [esta página](https://www.google.com/intl/en/chrome/demos/speech.html) que tiene un ejemplo de uso.
