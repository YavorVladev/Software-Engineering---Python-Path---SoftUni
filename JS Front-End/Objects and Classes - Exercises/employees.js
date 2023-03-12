function solve(data) {
  let employeeInfo = {};

  for (const person of data) {
    employeeInfo[person] = person.length;
  }

  for (const k in employeeInfo) {
    console.log(`Name: ${k} -- Personal Number: ${employeeInfo[k]}`);
  }
}

solve([
  "Silas Butler",
  "Adnaan Buckley",
  "Juan Peterson",
  "Brendan Villarreal",
]);
