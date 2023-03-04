function largestNumber(x, y, z) {

    let result = 0;

    if (x > y && x > z) {
        result = x;
    } else if (y > x && y > z) {
        result = y;
    } else {
        result = z;
    }

    console.log(`The largest number is ${result}.`);
}

largestNumber(5, -3, 16)