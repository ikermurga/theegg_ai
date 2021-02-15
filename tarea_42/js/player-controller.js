// Funciones que van a servir para subir y bajar el volumen del video
// así como para cargar el video
function PlayerController() {
    // This code loads the IFrame Player API code asynchronously.
    var tag = document.createElement('script');

    tag.src = 'https://www.youtube.com/iframe_api';
    var firstScriptTag = document.getElementsByTagName('script')[0];
    firstScriptTag.parentNode.insertBefore(tag, firstScriptTag);

    // Función que crea un iframe con el video una vez se ha descargado
    // la API de YouTube para poder modificar el volumen del video.
    var player;
    function onYouTubeIframeAPIReady() {
        player = new YT.Player('player', {
            height: '390',
            width: '640',
            videoId: 'WXuK6gekU1Y',
        });
    }

    // Función para reducir el volumen (en un 30%)
    function lowerPlayerVolume() {
        var volume = player.getVolume();
        volume -= 30;
        if (volume < 0) volume = 0;
        player.setVolume(volume);
    }

    // Función para subir el volumen (en un 30%)
    function raisePlayerVolume() {
        var volume = player.getVolume();
        volume += 30;
        if (volume > 100) volume = 100;
        player.setVolume(volume);
    }

    return {
        onYouTubeIframeAPIReady,
        lowerPlayerVolume,
        raisePlayerVolume,
    };
}
