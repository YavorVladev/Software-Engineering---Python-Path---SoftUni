function signCheck(x, y, z) {
  const totalNegatives = [x, y, z].filter((n) => n < 0).length;
  return totalNegatives % 2 == 0 ? "Positive" : "Negative";
}

console.log(signCheck(-6, -12, 14));
