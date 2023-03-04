function getTicketPrice(dayType, age) {
    if (age < 0 || age > 122) {
        console.log("Error!");
        return;
    }
    let price;
    switch (dayType) {
        case "Weekday":
            price = age <= 18 ? 12 : age <= 64 ? 18 : 12;
            break;
        case "Weekend":
            price = age <= 18 ? 15 : age <= 64 ? 20 : 15;
            break;
        case "Holiday":
            price = age <= 18 ? 5 : age <= 64 ? 12 : 10;
            break;
        default:
            console.log("Error!");
            return;
    }
    console.log(`${price}$`);
}