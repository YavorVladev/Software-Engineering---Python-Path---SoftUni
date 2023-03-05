function simpleCalc(x,y,op) {

    let outcome = 0;

    switch (op) {
        case "multiply": outcome = x * y; break;
        case "divide": outcome = x / y; break;
        case "add": outcome = x + y; break;
        case "subtract": outcome = x - y; break;
    }

    console.log(outcome);
}

simpleCalc(5,5, "multiply")