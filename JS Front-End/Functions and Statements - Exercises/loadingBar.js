function loadingBar(percentage) {

    let result = '';

    switch (percentage) {
        case 0 : result = "0% [..........]\nStill loading..."; break;
        case 10 : result = "10% [%.........]\nStill loading..."; break;
        case 20 : result = "20% [%%........]\nStill loading..."; break;
        case 30 : result = "30% [%%%.......]\nStill loading..."; break;
        case 40 : result = "40% [%%%%......]\nStill loading..."; break;
        case 50 : result = "50% [%%%%%.....]\nStill loading..."; break;
        case 60 : result = "60% [%%%%%%....]\nStill loading..."; break;
        case 70 : result = "70% [%%%%%%%...]\nStill loading..."; break;
        case 80 : result = "80% [%%%%%%%%..]\nStill loading..."; break;
        case 90 : result = "90% [%%%%%%%%%.]\nStill loading..."; break;
        case 100 : result = "100% Complete!\n[%%%%%%%%%%]"; break;

    }

    console.log(result);
}

loadingBar(100)