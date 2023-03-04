function monthPrinter(monthNumber) {
    console.log(
        monthNumber < 1 || monthNumber > 12
            ? "Error!"
            : ["January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December"][monthNumber - 1]
    );
}

