function manageMeetings(meetings) {
  const scheduledMeetings = {};
  const successfulMeetings = [];

  for (let meeting of meetings) {
    const [day, name] = meeting.split(" ");
    if (scheduledMeetings[day]) {
      console.log(`Conflict on ${day}!`);
    } else {
      scheduledMeetings[day] = name;
      successfulMeetings.push(meeting);
      console.log(`Scheduled for ${day}`);
    }
  }

  console.log(
    successfulMeetings
      .map((meeting) => `${meeting.split(" ")[0]} -> ${meeting.split(" ")[1]}`)
      .join("\n")
  );
}

manageMeetings(["Monday Peter", "Wednesday Bill", "Monday Tim", "Friday Tim"]);
