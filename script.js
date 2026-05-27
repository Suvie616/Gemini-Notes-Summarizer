const textarea = document.querySelector("#noteInput");
const button = document.querySelector("#generateBtn");
const paragraph = document.querySelector("#infoText");

button.addEventListener("click", () => {
  paragraph.textContent = textarea.value;
});