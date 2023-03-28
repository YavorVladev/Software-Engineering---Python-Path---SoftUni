function subtract() {
  const firstNumDoc = document.getElementById("firstNumber");
  const secondNumDoc = document.getElementById("secondNumber");
  const result = document.getElementById("result");

  let num1 = Number(firstNumDoc.value);
  let num2 = Number(secondNumDoc.value);

  result.textContent = num1 - num2;
}
