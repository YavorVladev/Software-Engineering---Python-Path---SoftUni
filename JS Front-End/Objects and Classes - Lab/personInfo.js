function personInfo(firstName, lastName, age) {
  age = Number(age);

  let person = { firstName: firstName, lastName: lastName, age: age };

  return person;
}

softwareArchitecture = personInfo("Yavor", "Vladev", "22");

console.log(softwareArchitecture.firstName);
