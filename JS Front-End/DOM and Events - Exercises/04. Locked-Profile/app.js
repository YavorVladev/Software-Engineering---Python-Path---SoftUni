function lockedProfile() {
  // get all profile containers
  const profiles = Array.from(document.querySelectorAll(".profile"));

  // loop through each profile and attach click event listener to its button
  profiles.forEach((profile) => {
    const button = profile.querySelector("button");
    button.addEventListener("click", () => {
      const isLocked =
        profile.querySelector('input[name$="Locked"]:checked').value === "lock";
      const hiddenFields = profile.querySelector(
        "#" + button.previousElementSibling.id
      );

      // if profile is locked, do nothing
      if (isLocked) {
        return;
      }

      // otherwise, toggle visibility of hidden fields
      hiddenFields.style.display =
        hiddenFields.style.display === "none" ? "block" : "none";
      button.textContent =
        hiddenFields.style.display === "none" ? "Show more" : "Hide it";
    });
  });
}
