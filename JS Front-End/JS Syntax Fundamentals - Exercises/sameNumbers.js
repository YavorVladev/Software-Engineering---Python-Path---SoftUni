function sameDigits(number) {
    const digits = Array.from(String(number), Number);
    const sum = digits.reduce((acc, curr) => acc + curr, 0);
    const firstDigit = digits[0];
    const allSame = digits.every((digit) => digit === firstDigit);
    console.log(allSame);
    console.log(sum);
}
