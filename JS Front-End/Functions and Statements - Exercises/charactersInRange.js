function charsInRange(firstChar, secondChar) {
  let firstCharAsValue = firstChar.charCodeAt();
  let secondCharAsValue = secondChar.charCodeAt();
  let characters = [];

  let temp = firstCharAsValue;

  if (firstCharAsValue > secondCharAsValue) {

    firstCharAsValue = secondCharAsValue;
    secondCharAsValue = temp;
  }

  for (let i = firstCharAsValue + 1; i < secondCharAsValue; i++) {
    characters.push(String.fromCharCode(i))
  }

  console.log(characters.join(' '));
}

charsInRange("C", "#");
