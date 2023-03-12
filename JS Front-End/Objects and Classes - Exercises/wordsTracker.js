function wordTracker(data) {
  const searchedWords = data[0].split(" ");
  const occurrences = {};

  for (let i = 1; i < data.length; i++) {
    const word = data[i];
    if (searchedWords.includes(word)) {
      occurrences[word] = occurrences[word] ? occurrences[word] + 1 : 1;
    }
  }

  const sortedOccurances = Object.entries(occurrences)
    .sort((a, b) => b[1] - a[1])
    .forEach(([word, count]) => console.log(`${word} - ${count}`));
}

wordTracker([
  "this sentence",
  "In",
  "this",
  "sentence",
  "you",
  "have",
  "to",
  "count",
  "the",
  "occurrences",
  "of",
  "the",
  "words",
  "this",
  "and",
  "sentence",
  "because",
  "this",
  "is",
  "your",
  "task",
]);
