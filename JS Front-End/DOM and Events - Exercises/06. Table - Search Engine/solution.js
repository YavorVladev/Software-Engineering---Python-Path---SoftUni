function solve() {
  document.querySelector("#searchBtn").addEventListener("click", onClick);

  function onClick() {
    let searchField = document.getElementById("searchField");
    let tableRows = document.querySelectorAll("tbody tr");
    let searchTerm = searchField.value;

    tableRows.forEach((row) => {
      row.classList.remove("select");
      if (row.textContent.includes(searchTerm)) {
        row.classList.add("select");
      }
    });
    searchField.value = "";
  }
}
