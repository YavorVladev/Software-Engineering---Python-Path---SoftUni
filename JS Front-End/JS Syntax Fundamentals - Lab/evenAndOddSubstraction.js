function evenOrOddSubstraction(data) {

    let evenSum = 0;
    let oddSum = 0;

    for (let i = 0; i < data.length; i++) {
        data[i] % 2 == 0 ? evenSum += data[i] : oddSum += data[i];
    }

    let result = evenSum - oddSum;
    console.log(result);
}

evenOrOddSubstraction([1, 2, 3, 4, 5, 6])