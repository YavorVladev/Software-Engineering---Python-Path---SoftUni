function loadCommits() {
  const usernameContainer = document.getElementById("username");
  const repoContainer = document.getElementById("repo");
  const dataContainer = document.getElementById("commits");

  const BASE_URL = `https://api.github.com/repos/${usernameContainer.value}/${repoContainer.value}/commits`;

  fetch(BASE_URL, { method: "GET" })
    .then((res) => res.json())
    .then((data) => {
      data.forEach(({ commit }) => {
        const liElement = document.createElement("li");
        liElement.textContent = `${commit.author.name}: ${commit.message}`;
        dataContainer.appendChild(liElement);
      });
    })
    .catch((err) => {
      console.log(err);
    });
}
