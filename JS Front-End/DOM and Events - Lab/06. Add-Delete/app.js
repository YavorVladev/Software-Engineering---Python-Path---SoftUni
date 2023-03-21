function addItem() {
  const liContainer = document.getElementById("items");
  const userInput = document.getElementById("newItemText");

  let newLi = document.createElement("li");
  const newAnchor = document.createElement("a");

  newLi.textContent = userInput.value;

  newAnchor.textContent = "[Delete]";
  newAnchor.setAttribute("href", "#");
  newAnchor.addEventListener("click", deleteHandler);
  newLi.appendChild(newAnchor);
  liContainer.appendChild(newLi);
  userInput.value = "";

  function deleteHandler(event) {
    const liItem = event.currentTarget.parentElement;
    liItem.remove();
  }
}
