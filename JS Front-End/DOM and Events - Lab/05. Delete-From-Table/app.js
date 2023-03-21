function deleteByEmail() {
  const userInput = document.querySelector("input[name='email']");
  const finalResult = document.getElementById("result");
  const emailForm = Array.from(document.querySelectorAll("td:nth-child(even)"));

  let emailInput = userInput.value;

  let foundEmail = emailForm.find(
    (element) => element.textContent === emailInput
  );

  if (foundEmail) {
    foundEmail.parentElement.remove();
    finalResult.textContent = `Deleted.`;
  } else {
    finalResult.textContent = `Not found.`;
  }
}
