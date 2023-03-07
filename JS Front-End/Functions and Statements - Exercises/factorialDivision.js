function calculateFactorialDivision(num1, num2) {
  const factorial = (num) => (num === 0 ? 1 : num * factorial(num - 1));
  const fact1 = factorial(num1);
  const fact2 = factorial(num2);
  const division = fact1 / fact2;
  return division.toFixed(2);
}
