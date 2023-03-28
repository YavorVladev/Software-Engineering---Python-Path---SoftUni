function toggle() {
  const docButtons = document.getElementsByClassName("button")[0];
  const extraTextDocumnet = document.getElementById("extra");

  if (docButtons.textContent == "More") {
    addEventListener("click", () => {
      docButtons.textContent = "Less";
      extraTextDocumnet.style.display = "block";
    });
  } else if (docButtons.textContent == "Less") {
    addEventListener("click", () => {
      docButtons.textContent = "More";
      extraTextDocumnet.style.display = "none";
    });
  }
}
