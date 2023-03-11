function solve(data) {
  class Song {
    constructor(type, name, time) {
      this.type = type;
      this.name = name;
      this.time = time;
    }
  }

  let songs = [];
  let numberOfSongs = data.shift();
  let typeSong = data.pop();

  for (let i = 0; i < numberOfSongs; i++) {
    let [type, name, time] = data[i].split("_");
    let song = new Song(type, name, time);
    songs.push(song);
  }

  if (typeSong === "all") {
    songs.forEach((s) => console.log(s.name));
  } else {
    let filteredSongs = songs.filter((s) => s.type === typeSong);
    filteredSongs.forEach((s) => console.log(s.name));
  }
}

solve([
  4,
  "favourite_DownTown_3:14",
  "listenLater_Andalouse_3:24",
  "favourite_In To The Night_3:58",
  "favourite_Live It Up_3:48",
  "listenLater",
]);

solve([2, "like_Replay_3:15", "ban_Photoshop_3:48", "all"]);

solve([
  3,
  "favourite_DownTown_3:14",
  "favourite_Kiss_4:16",
  "favourite_Smooth Criminal_4:01",
  "favourite",
]);
