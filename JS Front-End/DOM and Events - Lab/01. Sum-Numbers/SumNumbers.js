function calc() {
    const firstNumStr = document.getElementById("num1");
    const secondNumStr = document.getElementById("num2");
    const resultStr = document.getElementById("sum");

    let firstNum = Number(firstNumStr.value);
    let secondNum = Number(secondNumStr.value);
    let result = firstNum + secondNum;

    resultStr.value = result;
    
}

