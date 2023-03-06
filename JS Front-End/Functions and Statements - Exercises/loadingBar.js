function loadingBar(num) {
  const percent = num / 10;
  let bar = "[";
  for (let i = 0; i < 10; i++) {
    if (i < percent) {
      bar += "%";
    } else {
      bar += ".";
    }
  }
  bar += "]";
  if (num < 100) {
    console.log(`${num}% ${bar}`);
    console.log("Still loading...");
  } else {
    console.log(`100% Complete!`);
    console.log("[%%%%%%%%%%]");
  }
}
