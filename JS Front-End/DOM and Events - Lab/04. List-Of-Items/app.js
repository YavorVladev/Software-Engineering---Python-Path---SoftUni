function addItem() {
  const userInput = document.getElementById("newItemText");
  const storage = document.getElementById("items");
  const newLi = document.createElement("li");
  newLi.textContent = userInput.value;

  storage.appendChild(newLi);
  userInput.value = "";
}
