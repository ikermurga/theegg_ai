function CommandRecognition(
    languageCode,
    raiseVolumeCommand,
    lowerVolumeCommand,
    raisePlayerVolumeFn,
    lowerPlayerVolumeFn,
    recognizedTextCallback
) {
    window.SpeechRecognition =
        window.SpeechRecognition || window.webkitSpeechRecognition;

    const recognition = new SpeechRecognition();
    recognition.lang = languageCode;
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
            timesRaised = 0;
            timesLowered = 0;
        }
    });

    function changeVolumeDependingOnTranscript(transcript) {
        let volumeUpCommands = timesTargetTextIsInText(
            transcript,
            raiseVolumeCommand
        );
        let volumeDownCommands = timesTargetTextIsInText(
            transcript,
            lowerVolumeCommand
        );

        // devolver lo que está reconociendo el micrófono
        recognizedTextCallback(transcript);

        while (timesRaised < volumeUpCommands) {
            raisePlayerVolumeFn();
            timesRaised++;
        }

        while (timesLowered < volumeDownCommands) {
            lowerPlayerVolumeFn();
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

    function changeLanguage(
        languageCode,
        languageRaiseVolumeCommand,
        languageLowerVolumeCommand
    ) {
        recognition.lang = languageCode;
        raiseVolumeCommand = languageRaiseVolumeCommand;
        lowerVolumeCommand = languageLowerVolumeCommand;
    }

    return {
        changeLanguage,
    };
}
