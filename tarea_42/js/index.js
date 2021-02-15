// Constantes
const volumeUpEnglishCommand = 'raise';
const volumeDownEnglishCommand = 'lower';
const volumeUpSpanishCommand = 'subir';
const volumeDownSpanishCommand = 'bajar';
const volumeUpBasqueCommand = 'igo';
const volumeDownBasqueCommand = 'jeitsi';

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
    'es-ES',
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
    .getElementById('lang-spanish')
    .addEventListener('change', languageChangeHandler);
document
    .getElementById('lang-english')
    .addEventListener('change', languageChangeHandler);
document
    .getElementById('lang-basque')
    .addEventListener('change', languageChangeHandler);

const instructionsContainer = document.getElementById('instructions');

function changeLanguageTo(language) {
    switch (language) {
        case 'spanish':
            recognition.changeLanguage(
                'es-ES',
                volumeUpSpanishCommand,
                volumeDownSpanishCommand
            );
            instructionsContainer.innerHTML = spanishInstructions;
            break;

        case 'basque':
            recognition.changeLanguage(
                'eu-ES',
                volumeUpBasqueCommand,
                volumeDownBasqueCommand
            );
            instructionsContainer.innerHTML = basqueInstructions;
            break;

        case 'english':
            recognition.changeLanguage(
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
