function solve(x, y) {

    let sum = 0
    let same_row = ''
    for (let i = x; i <= y; i++) {
        sum += i
        same_row += i + " ";

    }
    console.log(same_row);
    console.log(`Sum: ${sum}`);
}