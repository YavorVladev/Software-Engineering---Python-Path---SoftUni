function solve(data) {
  let myObject = { town: "", latitude: 0, longitude: 0 };

  for (const el of data) {
    let [town_, latitude_, longitude_] = el.split(" | ");
    myObject["town"] = town_;
    myObject["latitude"] = Number(latitude_).toFixed(2);
    myObject["longitude"] = Number(longitude_).toFixed(2);

    console.log(myObject);
  }
}

solve(["Madrid | 42.696552 | 23.32601", "Beijing | 39.913818 | 116.363625"]);
