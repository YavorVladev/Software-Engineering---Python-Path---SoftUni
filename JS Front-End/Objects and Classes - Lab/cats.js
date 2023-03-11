function solve(data) {
  let cats = [];

  class Cats {
    constructor(name, age) {
      this.name = name;
      this.age = age;
    }

    meow() {
      console.log(`${this.name}, age ${this.age} says Meow`);
    }
  }
  for (let i = 0; i < data.length; i++) {
    let [name, age] = data[i].split(" ");
    let cat = new Cats(name, Number(age));
    cats.push(cat);
  }

  for (const cat of cats) {
    cat.meow();
  }
}

solve(["Candy 1", "Poppy 3", "Nyx 2"]);
