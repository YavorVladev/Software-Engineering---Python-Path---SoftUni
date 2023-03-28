function create(words) {
  const content = document.getElementById("content");

  words.forEach((word) => {
    const newDiv = document.createElement("div");
    const newP = document.createElement("p");

    newP.textContent = word;
    newP.style.display = "none";

    newDiv.appendChild(newP);
    newDiv.addEventListener("click", () => {
      newP.style.display = "block";
    });

    content.appendChild(newDiv);
  });
}
