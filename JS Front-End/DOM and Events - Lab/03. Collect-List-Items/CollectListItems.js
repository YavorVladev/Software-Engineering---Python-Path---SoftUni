function extractText() {
  const allItems = Array.from(document.querySelectorAll("#items > li"));
  const result = document.getElementById("result");

  allItems.forEach((item) => {
    result.textContent += item.textContent + "\n";
  });
}
