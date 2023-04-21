function horseRacing(arr) {

    let horseNames = arr.shift();
    horseNames = horseNames.split("|")

    for (let i = 0; i < arr.length; i++) {

        let args = arr[i].split(" ");

        let command = args[0];

        if ( command === "Finish") {
            break;
        } else if ( command === "Retake" ) {
            

            let overTakingHorse = args[1];
            let overTakenHorse = args[2];

            let overTakingIndex = horseNames.indexOf(overTakingHorse);
            let overTakenIndex = horseNames.indexOf(overTakenHorse);

            if ( overTakingIndex < overTakenIndex ) {

                horseNames.splice(overTakenIndex, 1 , overTakingHorse);
                horseNames.splice(overTakingIndex, 1, overTakenHorse);

                console.log(`${overTakingHorse} retakes ${overTakenHorse}.`)
            }

        } else if ( command === "Trouble" ) {
            
            let troubledHorse = args[1];
            let troubledHorseIndex = horseNames.indexOf(troubledHorse);
            let allPositions = horseNames.length - 1;

            if ( troubledHorseIndex !== allPositions ) {

                let overTakingHorse = horseNames[troubledHorseIndex - 1]
                let overTakingIndex = horseNames.indexOf(overTakingHorse);

                horseNames.splice(troubledHorseIndex, 1 , overTakingHorse);
                horseNames.splice(overTakingIndex, 1, troubledHorse);

                console.log(`Trouble for ${troubledHorse} - drops one position.`)

            }

            


        } else if ( command === "Rage" ) {
            console.log('breka');
        } else if ( command === "Miracle" ) {
            break;
        }
    }

}

horseRacing(['Bella|Alexia|Sugar',
'Retake Alexia Sugar',
'Rage Bella',
'Trouble Bella',
'Finish'])
