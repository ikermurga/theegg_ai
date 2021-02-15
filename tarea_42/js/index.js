// Constantes
const volumeUpEnglishCommand = 'raise';
const volumeDownEnglishCommand = 'lower';
const volumeUpSpanishCommand = 'subir';
const volumeDownSpanishCommand = 'bajar';
const volumeUpBasqueCommand = 'igo';
const volumeDownBasqueCommand = 'jaitsi';

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
// Función para mostrar el texto reconocido en el navegador
const recognizedCommandElement = document.getElementById('recognized-command');
function showRecognizedText(text) {
    recognizedCommandElement.innerText = text;
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

// Función ejecutada al cambiar el idioma de los comandos, modifica
// el idioma del reconocedor de audio y modifica los comandos que
// se muestran en el navegador
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

// Comprueba qué idioma se ha seleccionado en el navegador
// y envía la información a la función de cambiar lenguaje
function languageChangeHandler(event) {
    changeLanguageTo(event.target.value);
}
