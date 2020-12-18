# Cómo ejecutar el código

-   Ya que se la tarea consta de crear una página, basta con abrir el archivo index.html con el navegador Chrome o Edge una vez descargados los archivos de la carpeta correspondiente. Ya que se utiliza el API SpeechRecognition de los navegadores, sólo funcionará en uno de los dos. Una vez abrimos el HTML en uno de los dos navegadores indicados, el propio navegador se encaragará de abrir los archivos correspondientes al leer el archivo _html_. Los archivos que utiliza el _html_ son varios, algunos que están incluidos en esta carpeta y otros externos (tales como código que se carga de _Bootstrap_ y utilizando la API de Google el video de YouTube).

# Pasos seguidos para resolver la tarea

-   Para la estructura general de la página he utilizado Bootstrap, más específicamente el ejemplo de [Pricing](https://getbootstrap.com/docs/5.0/examples/pricing/) como punto de partida que luego he adaptado modificando el contenido de tanto la cabecera como el footer, y el mayor cambio ha sido en la sección de contenido principal.

-   Para los colores he utilizado colores de fondo y de letra sacados del esquema de colores de la página [Color Palettes](https://colorpalettes.net/color-palette-3535/), junto con el blanco.

-   Para añadir el video de YouTube y poder manejar los controles (para así poder ajustar el volumen) desde JavaScript, he utilizado la información disponible en [esta página de Google](https://developers.google.com/youtube/iframe_api_reference).

-   Para poder reconocer lo dicho por el usuario por micrófono he utilizado la información respecto a Speech Recognition API en [este video de Wes Bos](https://www.youtube.com/watch?v=0mJC0A72Fnw). También he mirado el código en [esta página](https://www.google.com/intl/en/chrome/demos/speech.html) que tiene un ejemplo de uso.

-   Ya que para que para que todo funcione correctamente se tienen que cargar tanto el video de YouTube como el Speech Recognition, he añadido indicadores a la página para saber a partir de qué momento van a funcionar correctamente los comandos de voz.

-   Si se usa no utilizando un servidor local, pide permiso para el micrófono en cada paso. Por lo tanto mejor utilizar un servidor (¿live server en vs code por ejemplo?)(probar en edge y firefox si funciona y si pasa lo mismo)
