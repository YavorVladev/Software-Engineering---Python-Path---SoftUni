function solve(products, delivery) {
  let productsData = {};

  for (let i = 0; i < products.length; i += 2) {
    const product = products[i];
    const quantity = Number(products[i + 1]);
    productsData[product] = quantity;
  }

  for (let i = 0; i < delivery.length; i += 2) {
    const product = delivery[i];
    const quantity = Number(delivery[i + 1]);
    if (productsData.hasOwnProperty(product)) {
      productsData[product] += quantity;
    } else {
      productsData[product] = quantity;
    }
  }

  for (const k in productsData) {
    console.log(`${k} -> ${productsData[k]}`);
  }
}

solve(
  ["Chips", "5", "CocaCola", "9", "Bananas", "14", "Pasta", "4", "Beer", "2"],
  ["Flour", "44", "Oil", "12", "Pasta", "7", "Tomatoes", "70", "Bananas", "30"]
);
