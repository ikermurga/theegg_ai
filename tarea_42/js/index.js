// Constantes
const instruccionesCastellano = `En castellano, dí
<strong>volumen arriba</strong> para subir el
volumen y <strong>volumen abajo</strong> para
bajarlo.`;
const instruccionesIngles = `En inglés, dí <strong>volume up</strong> para
subir el volumen y
<strong>volume down</strong> para bajarlo.`;
const instruccionesEuskera = `En euskera, dí <strong>soinua gora</strong> para
subir el volumen y
<strong>soinua behera</strong> para bajarlo.`;

const volumeUpEnglishCommand = 'volume up';
const volumeDownEnglishCommand = 'volume down';
const volumeUpSpanishCommand = 'volumen arriba';
const volumeDownSpanishCommand = 'volumen abajo';
const volumeUpBasqueCommand = 'soinua gora';
const volumeDownBasqueCommand = 'soinua behera';

// Preparando el video y enlazando sus eventos
var playerReadyIndicator = document.getElementById('player-ready-indicator');
const playerController = PlayerController(onPlayerReady);
function onYouTubeIframeAPIReady() {
    playerController.onYouTubeIframeAPIReady();
}
function onPlayerReady() {
    playerReadyIndicator.textContent = 'Video listo';
}

// Preparando el reconocedor de voz y enlazando sus eventos
const recognition = CommandRecognition(
    'spanish',
    playerController.raisePlayerVolume,
    playerController.lowerPlayerVolume,
    showRecognizedText
);
function showRecognizedText(text) {
    console.log(text);
}

// Selector de idiomas de interfaz
document
    .getElementById('lang-castellano')
    .addEventListener('change', languageChangeHandler);
document
    .getElementById('lang-ingles')
    .addEventListener('change', languageChangeHandler);
document
    .getElementById('lang-euskera')
    .addEventListener('change', languageChangeHandler);

const instruccionesContainer = document.getElementById('instrucciones');

function changeLanguageTo(language) {
    switch (language) {
        case 'castellano':
            recognition.changeLanguage('spanish', 'es-ES');
            instruccionesContainer.innerHTML = instruccionesCastellano;
            break;

        case 'euskera':
            recognition.changeLanguage('basque', 'eu-ES');
            instruccionesContainer.innerHTML = instruccionesEuskera;
            break;

        case 'ingles':
            recognition.changeLanguage('english', 'en-US');
            instruccionesContainer.innerHTML = instruccionesIngles;
            break;
    }
}

function languageChangeHandler(event) {
    changeLanguageTo(event.target.value);
}
