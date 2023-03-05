function perfectNumber(number) {

    let totalSum = 0;
    let others = 0;

    for (let i = 1; i < number; i ++) {
        number % i == 0 ? totalSum += i : others;

    }

    console.log(totalSum == number ? "We have a perfect number!" : "It's not so perfect.")
}

perfectNumber(1236498)