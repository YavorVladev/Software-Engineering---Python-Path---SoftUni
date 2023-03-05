function checkPalindrome(numbers) {
  numbers.forEach((number) => {
    const numString = number.toString();
    const reversedNumString = numString.split("").reverse().join("");
    const isPalindrome = numString === reversedNumString;
    console.log(isPalindrome ? "true" : "false");
  });
}

checkPalindrome([123, 323, 421, 121]);
