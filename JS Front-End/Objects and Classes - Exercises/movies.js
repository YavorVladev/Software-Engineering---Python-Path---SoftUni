function solve(input) {
  let result = [];

  for (const line of input) {
    let tokens = line.split(" ");

    if (tokens[0] === "addMovie") {
      result.push({ name: tokens.slice(1).join(" ") });
    } else {
      let movie = result.find((m) => m.name === tokens[0]);

      if (movie) {
        if (tokens[1] === "directedBy") {
          movie.director = tokens.slice(2).join(" ");
        } else if (tokens[1] === "onDate") {
          movie.date = tokens.slice(2).join(" ");
        }
      }
    }
  }

  result = result.filter((m) => m.name && m.director && m.date);

  for (let i = 0; i < result.length; i++) {
    console.log(`${JSON.stringify(result[i])}`);
  }
}

solve([
  "addMovie Fast and Furious",
  "addMovie Godfather",
  "Inception directedBy Christopher Nolan",
  "Godfather directedBy Francis Ford Coppola",
  "Godfather onDate 29.07.2018",
  "Fast and Furious onDate 30.07.2018",
  "Batman onDate 01.08.2018",
  "Fast and Furious directedBy Rob Cohen",
]);
