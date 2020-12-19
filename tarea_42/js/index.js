// Constantes
const volumeUpEnglishCommand = 'volume up';
const volumeDownEnglishCommand = 'volume down';
const volumeUpSpanishCommand = 'volumen arriba';
const volumeDownSpanishCommand = 'volumen abajo';
const volumeUpBasqueCommand = 'igo bolumena';
const volumeDownBasqueCommand = 'jaitsi bolumena';

const spanishInstructions = `En castellano, dí
<strong>${volumeUpSpanishCommand}</strong> para subir el
volumen y <strong>${volumeDownSpanishCommand}</strong> para
bajarlo.`;
const englishInstructions = `En inglés, dí <strong>${volumeUpEnglishCommand}</strong> para
subir el volumen y
<strong>${volumeDownEnglishCommand}</strong> para bajarlo.`;
const basqueInstructions = `En euskera, dí <strong>${volumeUpBasqueCommand}</strong> para
subir el volumen y
<strong>${volumeDownBasqueCommand}</strong> para bajarlo.`;

// Preparando el video y enlazando sus eventos
const playerController = PlayerController();
function onYouTubeIframeAPIReady() {
    playerController.onYouTubeIframeAPIReady();
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
