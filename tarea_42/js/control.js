// This code loads the IFrame Player API code asynchronously.
var tag = document.createElement('script');

tag.src = 'https://www.youtube.com/iframe_api';
var firstScriptTag = document.getElementsByTagName('script')[0];
firstScriptTag.parentNode.insertBefore(tag, firstScriptTag);

// This function creates an <iframe> (and YouTube player)
// after the API code downloads.
var player;
function onYouTubeIframeAPIReady() {
    player = new YT.Player('player', {
        height: '390',
        width: '640',
        videoId: 'M7lc1UVf-VE',
        events: {
            onReady: onPlayerReady,
        },
    });
}

var playerReadyIndicator = document.getElementById('player-ready-indicator');
function onPlayerReady(event) {
    playerReadyIndicator.textContent = 'Video listo';
}

function lowerPlayerVolume() {
    var volume = player.getVolume();
    volume -= 20;
    if (volume < 0) volume = 0;
    player.setVolume(volume);
}

function raisePlayerVolume() {
    var volume = player.getVolume();
    volume += 20;
    if (volume > 100) volume = 100;
    player.setVolume(volume);
}

window.SpeechRecognition =
    window.SpeechRecognition || window.webkitSpeechRecognition;

const recognition = new SpeechRecognition();
recognition.lang = 'es-ES';
recognition.interimResults = true;

let timesRaised = 0;
let timesLowered = 0;
recognition.addEventListener('result', function (event) {
    const transcript = Array.from(event.results)
        .map((result) => result[0])
        .map((result) => result.transcript)
        .join('');

    changeVolumeDependingOnTranscript(transcript);

    if (event.results[0].isFinal) {
        changeVolumeDependingOnTranscript(transcript);

        timesRaised = 0;
        timesLowered = 0;
    }
});

function changeVolumeDependingOnTranscript(transcript) {
    let volumeUpCommand = '';
    let volumeDownCommand = '';
    if (selectedLanguage === 'english') {
        volumeUpCommand = volumeUpEnglishCommand;
        volumeDownCommand = volumeDownEnglishCommand;
    } else if (selectedLanguage === 'spanish') {
        volumeUpCommand = volumeUpSpanishCommand;
        volumeDownCommand = volumeDownSpanishCommand;
    } else if (selectedLanguage === 'basque') {
        volumeUpCommand = volumeUpBasqueCommand;
        volumeDownCommand = volumeDownBasqueCommand;
    }
    let volumeUpCommands = timesTargetTextIsInText(transcript, volumeUpCommand);
    let volumeDownCommands = timesTargetTextIsInText(
        transcript,
        volumeDownCommand
    );

    // descomentar para ver lo que está reconociendo el micrófono
    // console.log(transcript);

    while (timesRaised < volumeUpCommands) {
        raisePlayerVolume();
        timesRaised++;
    }

    while (timesLowered < volumeDownCommands) {
        lowerPlayerVolume();
        timesLowered++;
    }
}

function timesTargetTextIsInText(text, target) {
    let times = 0;
    let index = 0;
    while (text.includes(target, index)) {
        times++;
        index = text.indexOf(target, index) + 1;
    }
    return times;
}

recognition.addEventListener('end', recognition.start);

recognition.start();

document
    .getElementById('lang-castellano')
    .addEventListener('change', cambiarOpcionIdioma);
document
    .getElementById('lang-ingles')
    .addEventListener('change', cambiarOpcionIdioma);
document
    .getElementById('lang-euskera')
    .addEventListener('change', cambiarOpcionIdioma);

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

let selectedLanguage = 'spanish';

const instruccionesContainer = document.getElementById('instrucciones');
function cambiarIdiomaA(idioma) {
    if (idioma === 'castellano') {
        selectedLanguage = 'spanish';
        recognition.lang = 'es-ES';
        instruccionesContainer.innerHTML = instruccionesCastellano;
    } else if (idioma == 'euskera') {
        selectedLanguage = 'basque';
        recognition.lang = 'eu-ES';
        instruccionesContainer.innerHTML = instruccionesEuskera;
    } else if (idioma == 'ingles') {
        selectedLanguage = 'english';
        recognition.lang = 'en-US';
        instruccionesContainer.innerHTML = instruccionesIngles;
    }
}

function cambiarOpcionIdioma(event) {
    cambiarIdiomaA(event.target.value);
}
