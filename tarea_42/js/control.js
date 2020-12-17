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
var volDownBtn = document.getElementById('vol-down-btn');
volDownBtn.addEventListener('click', lowerPlayerVolume);
function raisePlayerVolume() {
    var volume = player.getVolume();
    volume += 20;
    if (volume > 100) volume = 100;
    player.setVolume(volume);
}
var volUpBtn = document.getElementById('vol-up-btn');
volUpBtn.addEventListener('click', raisePlayerVolume);

window.SpeechRecognition =
    window.SpeechRecognition || window.webkitSpeechRecognition;

const recognition = new SpeechRecognition();
recognition.interimResults = true;

recognition.addEventListener('result', function (event) {
    // console.log(event);
    const transcript = Array.from(event.results)
        .map((result) => result[0])
        .map((result) => result.transcript)
        .join('');

    if (event.results[0].isFinal) {
        if (transcript.includes('volume up')) {
            console.log(transcript);
            raisePlayerVolume();
        }
        if (transcript.includes('volume down')) {
            console.log(transcript);
            lowerPlayerVolume();
        }
    }
});

recognition.addEventListener('end', recognition.start);

recognition.start();
