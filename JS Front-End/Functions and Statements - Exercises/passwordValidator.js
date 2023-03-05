function checkPassword(password) {
  const length = password.length;
  const digits = password.match(/\d/g);
  const alphanumeric = /^[a-z0-9]+$/i.test(password);

  if (length < 6 || length > 10) {
    console.log("Password must be between 6 and 10 characters");
  }
  if (!alphanumeric) {
    console.log("Password must consist only of letters and digits");
  }
  if (!digits || digits.length < 2) {
    console.log("Password must have at least 2 digits");
  }
  if (
    length >= 6 &&
    length <= 10 &&
    alphanumeric &&
    digits &&
    digits.length >= 2
  ) {
    console.log("Password is valid");
  }
}

checkPassword("logIn")