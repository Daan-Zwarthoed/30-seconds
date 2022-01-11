const form = document.querySelector(".makeGroupForm");
const addPersonButton = document.querySelector(".addPersonButton");
const personList = document.querySelector(".personList");
const personInput = document.querySelector(".addPersonInput");
const personListInput = document.querySelector(".personListInput");

form.addEventListener("submit", function (event) {
  if (event.submitter === addPersonButton && personInput.value) {
    event.preventDefault();
    const newListItem = personList.children[0].cloneNode(true);
    newListItem.children[0].textContent = personInput.value;
    const deleteDiv = document.createElement("div");
    deleteDiv.classList.add("delete");
    deleteDiv.textContent = "delete";
    newListItem.appendChild(deleteDiv);
    personList.appendChild(newListItem);
    personListInput.value = `${personListInput.value} ${personInput.value}`;
    personInput.value = "";
  }
});

personList.addEventListener("click", function (event) {
  if (event.target.classList.contains("delete")) {
    const deleteString =
      " " + event.target.parentElement.children[0].textContent + " ";
    personListInput.value = personListInput.value.replace(deleteString, " ");
    event.target.parentElement.remove();
  }
});
