function solve(data) {
  let inventory = [];

  for (let line of data) {
    const [name, level, itemsStr] = line.split(" / ");
    const items = itemsStr ? itemsStr.split(", ") : [];

    inventory.push({ name, level: Number(level), items });
  }

  inventory.sort((a, b) => a.level - b.level);

  let output = ``;

  for (const hero of inventory) {
    output += `Hero: ${hero.name}\n`;
    output += `level => ${hero.level}\n`;
    output += `items => ${hero.items.join(", ")}\n`;
  }

  return output.trim();
}

console.log(
  solve([
    "Isacc / 25 / Apple, GravityGun",
    "Derek / 12 / BarrelVest, DestructionSword",
    "Hes / 1 / Desolator, Sentinel, Antara",
  ])
);
