function orders(product, quantity) {

    let orderTotal = 0;

    switch (product) {
        case "coffee": orderTotal = quantity * 1.50; break;
        case "water": orderTotal = quantity * 1.00; break;
        case "coke": orderTotal = quantity * 1.40; break;
        case "snacks": orderTotal = quantity * 2.00; break;
    }

    console.log(orderTotal.toFixed(2));
}

orders("water", 5)