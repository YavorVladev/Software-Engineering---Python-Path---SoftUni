function Fruit(food, grams, priceKG) {

    let gramsToKGs = grams / 1000;
    let neededMoney = gramsToKGs * priceKG;

    console.log(`I need $${neededMoney.toFixed(2)} to buy ${gramsToKGs.toFixed(2)} kilograms ${food}.`);

}

Fruit('orange', 2500, 1.80)

