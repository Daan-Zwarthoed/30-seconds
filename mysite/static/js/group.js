const form = document.querySelector(".addWordsForm");
const addWordButton = document.querySelector(".addWordButton");
const wordList = document.querySelector(".wordList");
const wordInput = document.querySelector(".addWordInput");
const wordListInput = document.querySelector(".wordListInput");
const saveChangesButton = document.querySelector(".saveChangesButton");
const currentGroupWordList = document.querySelector(".currentGroupWordList");
let allWords = currentGroupWordList.textContent.replace(/\s+/g, " ").trim();
currentGroupWordList.remove();
form.addEventListener("submit", function (event) {
  if (event.submitter === addWordButton) {
    event.preventDefault();
    if (
      wordInput.value &&
      !allWords.includes(wordInput.value + " ") &&
      " " + !allWords.includes(wordInput.value)
    ) {
      const newListItem = document.createElement("li");
      const newListItemText = document.createElement("p");
      const deleteDiv = document.createElement("div");

      newListItem.textContent = wordInput.value;

      deleteDiv.classList.add("delete");
      deleteDiv.textContent = "delete";

      newListItem.appendChild(newListItemText);
      newListItem.appendChild(deleteDiv);
      wordList.appendChild(newListItem);

      allWords = allWords + " " + wordInput.value;
      wordListInput.setAttribute(
        "value",
        `${wordListInput.value} ${wordInput.value}`.replace(/\s+/g, " ").trim()
      );
      wordInput.value = "";
    }
  }
});

wordList.addEventListener("click", function (event) {
  if (event.target.classList.contains("delete")) {
    const deleteString = event.target.parentElement.children[0].textContent;
    allWords = allWords.replace(deleteString, "").replace(/\s+/g, " ").trim();
    wordListInput.setAttribute(
      "value",
      wordListInput.value.replace(deleteString, "").replace(/\s+/g, " ").trim()
    );
    event.target.parentElement.remove();
  }
});
