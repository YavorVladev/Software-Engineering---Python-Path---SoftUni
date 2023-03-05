function oddAndEvenSum(n) {
  let evenSum = 0;
  let oddSum = 0;

  let nAsString = n.toString();

  for (let i = 0; i < nAsString.length; i++) {
    Number(nAsString[i]) % 2 == 0
      ? (evenSum += Number(nAsString[i]))
      : (oddSum += Number(nAsString[i]));
  }

  console.log(`Odd sum = ${oddSum}, Even sum = ${evenSum}`);
}

oddAndEvenSum(1000435);
