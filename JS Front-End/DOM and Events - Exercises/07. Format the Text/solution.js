function solve() {
  const input = document.getElementById("input").value;
  const sentences = input.split(".").filter((sentence) => sentence.trim().length > 0);
  const output = document.getElementById("output");
  output.innerHTML = "";
  let paragraph = "";
  let sentenceCount = 0;
  for (let i = 0; i < sentences.length; i++) {
    const sentence = sentences[i].trim() + ".";
    paragraph += sentence;
    sentenceCount++;
    if (sentenceCount >= 3 || i === sentences.length - 1) {
      output.innerHTML += `<p>${paragraph}</p>`;
      paragraph = "";
      sentenceCount = 0;
    }
  }
}