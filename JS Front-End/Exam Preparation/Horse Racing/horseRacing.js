function horseRacing(arr) {

    let horseNames = arr.shift();
    horseNames = horseNames.split("|")

    for (let i = 0; i < arr.length; i++) {

        let args = arr[i].split(" ");

        let command = args[0];

        if ( command === "Finish") {

            let winner = horseNames[horseNames.length - 1];
            console.log(`${horseNames.join('->')}`);
            console.log(`The winner is: ${winner}`);
            break;

        } else if ( command === "Retake" ) {
            

            let overTakingHorse = args[1];
            let overTakenHorse = args[2];

            let overTakingIndex = horseNames.indexOf(overTakingHorse);
            let overTakenIndex = horseNames.indexOf(overTakenHorse);

            if ( overTakingIndex < overTakenIndex ) {

                // horseNames.splice(overTakenIndex, 1 , overTakingHorse);
                // horseNames.splice(overTakingIndex, 1, overTakenHorse);

                horseNames.splice(overTakingIndex, 1);
                horseNames.splice(overTakenIndex + 1, 0, overTakingHorse);

                console.log(`${overTakingHorse} retakes ${overTakenHorse}.`)


            }

        } else if ( command === "Trouble" ) {
            
            let troubledHorse = args[1];
            let troubledHorseIndex = horseNames.indexOf(troubledHorse);

            if ( troubledHorseIndex !== 0 ) {

                let overTakingHorse = horseNames[troubledHorseIndex - 1]
                let overTakingIndex = horseNames.indexOf(overTakingHorse);

                horseNames.splice(troubledHorseIndex, 1);
                horseNames.splice(troubledHorseIndex - 1, 0, troubledHorse);

                console.log(`Trouble for ${troubledHorse} - drops one position.`);


            }

            


        } else if ( command === "Rage" ) {
            
            let overTakingHorse = args[1];
            let overTakingIndex = horseNames.indexOf(overTakingHorse);


            if ( overTakingIndex === 0) {



                // let overTakenHorse = horseNames[overTakingIndex + 2];
                // let overTakenIndex = horseNames.indexOf(overTakenHorse);

                // horseNames.splice(overTakenIndex, 1, overTakingHorse);
                // horseNames.splice(overTakingIndex, 1, overTakenHorse);

                horseNames.splice(overTakingIndex, 1);
                horseNames.splice(overTakingIndex + 2, 0 , overTakingHorse);

                console.log(`${overTakingHorse} rages 2 positions ahead.`);



                



            } else if ( overTakingIndex === 1) {

                horseNames.splice(overTakingIndex, 1);
                horseNames.splice(overTakingIndex + 1, 0 , overTakingHorse);

                console.log(`${overTakingHorse} rages 2 positions ahead.`);


            }


        } else if ( command === "Miracle" ) {
            
            let overTakingHorse = horseNames[0];
            let overTakingIndex = horseNames.indexOf(overTakingHorse);

            let numHorses = horseNames.length - 1;

            let firstHorse = horseNames[numHorses];
            let overTakenIndex = horseNames.indexOf(firstHorse);

            horseNames.splice(overTakenIndex, 1, overTakingHorse);
            horseNames.splice(overTakingIndex, 1, firstHorse);

            console.log(`What a miracle - ${overTakingHorse} becomes first.`);



        }
    }

}

horseRacing(['Bella|Alexia|Sugar',
'Retake Alexia Sugar',
'Rage Bella',
'Trouble Bella',
'Finish'])






// BAS
// BSA
// SAB 