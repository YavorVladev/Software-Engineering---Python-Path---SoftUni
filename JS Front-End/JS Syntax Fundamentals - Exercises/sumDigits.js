function sumDigits(num) {
    const digits = num.toString().split('').map(Number);
    return digits.reduce((acc, curr) => acc + curr, 0);
}
