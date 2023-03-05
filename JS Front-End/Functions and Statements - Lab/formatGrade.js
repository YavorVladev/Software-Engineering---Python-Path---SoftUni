function formatGrade(grade) {
  let result = "";

  if (grade >= 3 && grade < 3.5) {
    result = "Poor";
  } else if (grade >= 3.5 && grade < 4.5) {
    result = "Good";
  } else if (grade >= 4.5 && grade < 5.5) {
    result = "Very good";
  } else {
    result = "Excellent";
  }

  if (grade < 3) {
    console.log(`Fail (2)`);
  } else {
    console.log(`${result} (${grade.toFixed(2)})`);
  }
}

formatGrade(2.99);
