function mathOperations(x,y,op) {
    let result = 0;
    switch (op) {
        case "+": result = x + y; break;
        case "-": result = x - y; break;
        case "*": result = x * y; break;
        case "/": result = x / y; break;
        case "%": result = x % y; break;
        case "**": result = Math.pow(x, y); break;
        
    }

    console.log(result);
}

