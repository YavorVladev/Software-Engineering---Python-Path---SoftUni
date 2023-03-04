function splitPascalCase(str) {
    const words = str.match(/[A-Z][a-z]*/g);
    return words.join(", ");
}

console.log(splitPascalCase('SplitMeIfYouCanHaHaYouCantOrYouCan'));