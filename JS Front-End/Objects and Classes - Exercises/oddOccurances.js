function solve(text) {
  let trying = text.toLowerCase().split(" ");
  let counter = {};

  for (let el of trying) {
    if (counter[el]) {
      counter[el] += 1;
    } else {
      counter[el] = 1;
    }
  }

  const oddWords = [];

  Object.entries(counter).forEach(([word, count]) => {
    if (count % 2 !== 0) {
      oddWords.push(word);
    }
  });

  return oddWords.join(" ");
}

console.log(solve("Java C# Php PHP Java PhP 3 C# 3 1 5 C#"));
