const dropdown = document.querySelector("#dropdown");
const dropdownMenu = document.querySelector("#dropdownMenu");

document.addEventListener("click", (e) => {
  if (!dropdown.contains(e.target)) {
    dropdownMenu.classList.remove("show");
  }
});

dropdownMenu.addEventListener("click", (e) => {
  if (dropdownMenu.contains(e.target) && dropdownMenu !== e.target) {
    dropdownMenu.classList.remove("show");
  }
});

function showDropdownMenu() {
  dropdownMenu.classList.add("show");
}
