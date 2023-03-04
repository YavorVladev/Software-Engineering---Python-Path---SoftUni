function cookingByNumbers(number, op1, op2, op3, op4, op5) {
    let result = Number(number);

    const operations = {
        chop: num => num / 2,
        dice: num => Math.sqrt(num),
        spice: num => num + 1,
        bake: num => num * 3,
        fillet: num => num * 0.8
    };

    const performOperation = (num, operation) => operations[operation](num);

    for (let i = 1; i <= 5; i++) {
        switch (i) {
            case 1:
                result = performOperation(result, op1);
                break;
            case 2:
                result = performOperation(result, op2);
                break;
            case 3:
                result = performOperation(result, op3);
                break;
            case 4:
                result = performOperation(result, op4);
                break;
            case 5:
                result = performOperation(result, op5);
                break;
        }

        console.log(result);
    }
}