// Esta función inicializa el reconocimiento de voz
function CommandRecognition(
    languageCode,
    raiseVolumeCommand,
    lowerVolumeCommand,
    raisePlayerVolumeFn,
    lowerPlayerVolumeFn,
    recognizedTextCallback
) {
    // Inicializar el reconocimiento de voz
    window.SpeechRecognition =
        window.SpeechRecognition || window.webkitSpeechRecognition;

    const recognition = new SpeechRecognition();
    recognition.lang = languageCode;
    recognition.interimResults = true;

    // Llevar registro de cuantas veces se han reconocido los
    // comandos de subir o bajar volumen (ya que en un solo comando
    // podrían haberse repetido varias veces)
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

    // Recorre la trascripción del audio e incrementa los valores
    // que se usan para ver las veces que se han reconocido los
    // comandos de subir o bajar el volumen
    function changeVolumeDependingOnTranscript(transcript) {
        let volumeUpCommands = timesTargetTextIsInText(
            transcript,
            raiseVolumeCommand
        );
        let volumeDownCommands = timesTargetTextIsInText(
            transcript,
            lowerVolumeCommand
        );

        // devolver lo que está reconociendo el micrófono,
        // este es el texto que aparecerá en el navegador
        // como comando reconocido
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

    // Esta es la funcionalidad que hace que se pueda cambiar
    // el idioma que se está reconociendo. Ya que lo vamos
    // a querer ejecutar desde otras partes del código, lo
    // devolvemos para poder ejecutarlo desde otras partes
    // del código
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
