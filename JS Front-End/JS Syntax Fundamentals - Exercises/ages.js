function solve(age) {

    let given_age = Number(age);
    let result = ``

    if (given_age >= 0 && given_age <= 2) {
        result = 'baby';
    } else if (given_age >= 3 && given_age <= 13) {
        result = `child`;
    } else if (given_age >= 14 && given_age <= 19) {
        result = `teenager`;
    } else if (given_age >= 20 && given_age <= 65) {
        result = `adult`;
    } else if (given_age >= 66) {
        result = `elder`;
    } else {
        result = `out of bounds`
    }

    console.log(result);
}