function replaceWordByLength(words, template) {
    let wordsArr = words.split(', ');
    let templatesArr = template.split(' ');

    for (let i = 0; i < templatesArr.length; i++) {
        if (templatesArr[i].includes('*')) {
            let wordLength = templatesArr[i].length;
            for (let j = 0; j < wordsArr.length; j++) {
                if (wordsArr[j].length === wordLength) {
                    templatesArr[i] = wordsArr[j];
                    break;
                }
            }
        }
    }

    return templatesArr.join(' ');
}

console.log(replaceWordByLength('great',
    'softuni is ***** place for learning new programming languages'
));