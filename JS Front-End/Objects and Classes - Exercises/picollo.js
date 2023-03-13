function parkingLot(input) {
  const carNumbers = new Set();

  input.forEach((entry) => {
    const [direction, carNumber] = entry.split(", ");

    if (direction === "IN") {
      carNumbers.add(carNumber);
    } else {
      carNumbers.delete(carNumber);
    }
  });

  if (carNumbers.size === 0) {
    console.log("Parking Lot is Empty");
  } else {
    const sortedCarNumbers = Array.from(carNumbers).sort();
    sortedCarNumbers.forEach((carNumber) => {
      console.log(carNumber);
    });
  }
}

parkingLot([
  "IN, CA2844AA",
  "IN, CA1234TA",
  "OUT, CA2844AA",
  "IN, CA9999TT",
  "IN, CA2866HI",
  "OUT, CA1234TA",
  "IN, CA2844AA",
  "OUT, CA2866HI",
  "IN, CA9876HH",
  "IN, CA2822UU",
]);
