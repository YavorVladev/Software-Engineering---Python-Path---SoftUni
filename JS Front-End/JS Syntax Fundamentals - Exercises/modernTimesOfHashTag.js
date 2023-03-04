function solve(str) {
    const words = str.split(' ');
    const regex = /^[A-Za-z]+$/; 
    const specialWords = [];
  
    for (let i = 0; i < words.length; i++) {
      const word = words[i];
      if (word.startsWith('#')) {
        const specialWord = word.slice(1); 
        if (regex.test(specialWord)) {
          specialWords.push(specialWord);
        }
      }
    }
  
    console.log(specialWords.join('\n'));
  }
  

solve('Nowadays everyone uses # to tag a #special word in #socialMedia')