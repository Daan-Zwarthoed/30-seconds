const form = document.querySelector(".makeGroupForm");
const addPersonButton = document.querySelector(".addPersonButton");
const personList = document.querySelector(".personList");
const personInput = document.querySelector(".addPersonInput");
const personListInput = document.querySelector(".personListInput");

form.addEventListener("submit", function (event) {
  if (event.submitter === addPersonButton) {
    event.preventDefault();
    const newListItem = personList.children[0].cloneNode(true);
    newListItem.children[0].textContent = personInput.value;
    personList.appendChild(newListItem);
    console.log(`${personListInput.value} ${personInput.value}`);
    personListInput.value = `${personListInput.value} ${personInput.value}`;
  }
});

personList.addEventListener("click", function (event) {
  if (event.target.classList.contains("delete")) {
    const removeString =
      " " + event.target.parentElement.children[0].textContent + " ";
    personListInput.value = personListInput.value.replace(removeString, " ");
    event.target.parentElement.remove();
  }
});
