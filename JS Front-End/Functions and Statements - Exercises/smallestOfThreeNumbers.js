function smallestNumber(x, y, z) {
  let smallest = x < y ? x : y;
  smallest = smallest < z ? smallest : z;
  console.log(smallest);
}

smallestNumber(-2, -5, -3);
