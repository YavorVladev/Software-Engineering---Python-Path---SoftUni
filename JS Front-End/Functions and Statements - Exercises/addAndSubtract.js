function calc(x, y, z) {
  const sum = (x, y) => x + y;
  const subtract = (sum, z) => sum - z;

  return subtract(sum(x, y), z);
}

console.log(calc(23,6,10));