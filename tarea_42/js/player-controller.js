function PlayerController(onReadyCb) {
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

    function onPlayerReady() {
        onReadyCb();
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

    return {
        onYouTubeIframeAPIReady,
        lowerPlayerVolume,
        raisePlayerVolume,
    };
}
