function createDictionary(input) {
  const dictionary = {};

  input.forEach((jsonString) => {
    const obj = JSON.parse(jsonString);
    const term = Object.keys(obj)[0];
    const definition = obj[term];
    dictionary[term] = definition;
  });

  const sortedTerms = Object.keys(dictionary).sort();

  sortedTerms.forEach((term) => {
    const definition = dictionary[term];
    console.log(`Term: ${term} => Definition: ${definition}`);
  });
}

