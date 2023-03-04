function solve(people, type, day) {



    if (type == "Business" && people >= 100) {
        people -= 10;
    }

    if (type === "Students") {
        switch (day) {
            case 'Friday': final_price = people * 8.45; break;
            case 'Saturday': final_price = people * 9.80; break;
            case 'Sunday': final_price = people * 10.46; break;

        }
    } else if (type === "Business") {
        switch (day) {
            case 'Friday': final_price = people * 10.90; break;
            case 'Saturday': final_price = people * 15.60; break;
            case 'Sunday': final_price = people * 16; break;

        }
    } else if (type === "Regular") {
        switch (day) {
            case 'Friday': final_price = people * 15; break;
            case 'Saturday': final_price = people * 20; break;
            case 'Sunday': final_price = people * 22.50; break;

        }
    }

    if (type === "Students" && people >= 30) {
        final_price *= 0.85;
    } else if (type == "Regular" && people >= 10 && people <= 20) {
        final_price *= 0.95;
    }

    console.log(`Total price: ${final_price.toFixed(2)}`)
}