function convertToJson(name, lastName, hairColor) {
  let person = { name, lastName, hairColor };
  let data = JSON.stringify(person);

  console.log(data);
}

convertToJson("George", "Jones", "Brown");
