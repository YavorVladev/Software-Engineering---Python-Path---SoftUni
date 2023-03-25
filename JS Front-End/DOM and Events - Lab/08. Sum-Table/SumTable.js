function sumTable() {
  let table = document.querySelector("table");
  let rows = table.querySelectorAll("tr");
  let sum = 0;
  for (let i = 1; i < rows.length - 1; i++) {
    let cells = rows[i].querySelectorAll("td");
    sum += parseFloat(cells[cells.length - 1].textContent);
  }
  document.querySelector("#sum").textContent = sum.toFixed(2);
}
