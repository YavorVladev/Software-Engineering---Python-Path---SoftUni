function checkWord(word, text) {
    const words = text.split(" ");
    for (let i = 0; i < words.length; i++) {
        const currentWord = words[i];
        if (currentWord.toLowerCase() === word.toLowerCase()) {
            console.log(`${currentWord.toLowerCase()}`);
            return;
        }
    }
    console.log(`${word.toLowerCase()} not found!`);
}
