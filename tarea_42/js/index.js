// Constantes
const spanishInstructions = `En castellano, dí
<strong>volumen arriba</strong> para subir el
volumen y <strong>volumen abajo</strong> para
bajarlo.`;
const englishInstructions = `En inglés, dí <strong>volume up</strong> para
subir el volumen y
<strong>volume down</strong> para bajarlo.`;
const basqueInstructions = `En euskera, dí <strong>soinua gora</strong> para
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
    volumeUpSpanishCommand,
    volumeDownSpanishCommand,
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

const instructionsContainer = document.getElementById('instrucciones');

function changeLanguageTo(language) {
    switch (language) {
        case 'castellano':
            recognition.changeLanguage(
                'spanish',
                'es-ES',
                volumeUpSpanishCommand,
                volumeDownSpanishCommand
            );
            instructionsContainer.innerHTML = spanishInstructions;
            break;

        case 'euskera':
            recognition.changeLanguage(
                'basque',
                'eu-ES',
                volumeUpBasqueCommand,
                volumeDownBasqueCommand
            );
            instructionsContainer.innerHTML = basqueInstructions;
            break;

        case 'ingles':
            recognition.changeLanguage(
                'english',
                'en-US',
                volumeUpEnglishCommand,
                volumeDownEnglishCommand
            );
            instructionsContainer.innerHTML = englishInstructions;
            break;
    }
}

function languageChangeHandler(event) {
    changeLanguageTo(event.target.value);
}
