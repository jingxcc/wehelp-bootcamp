const searchNameInput = document.getElementById("searchNameInput");
const searchNameBtn = document.getElementById("searchNameBtn");
const searchNameResult = document.getElementById("searchNameResult");

const memberName = document.getElementById("memberName");
const updateNameInput = document.getElementById("updateNameInput");
const updateNameBtn = document.getElementById("updateNameBtn");
const updateNameResult = document.getElementById("updateNameResult");

searchNameBtn.addEventListener("click", () => {
  if (searchNameInput.value !== "") {
    const urlParameter = new URLSearchParams({
      username: searchNameInput.value,
    });
    const styleResult = ["text-14", "color-red"];

    fetch(`/api/member?${urlParameter}`)
      .then((res) => res.json())
      .then((result) => {
        if (result["data"] !== null) {
          searchNameResult.classList.remove(...styleResult);
          searchNameResult.textContent = `${result["data"]["name"]} (${result["data"]["username"]})`;
        } else {
          searchNameResult.classList.add(...styleResult);
          searchNameResult.textContent = "Username Not Found";
        }
      })
      .catch((error) => {
        console.error("Error:", error);
      });
  }
});

updateNameBtn.addEventListener("click", () => {
  if (updateNameInput.value !== "") {
    let requestBody = {
      name: updateNameInput.value,
    };
    fetch(`/api/member`, {
      method: "PATCH",
      headers: {
        "Content-Type": "application/json",
      },
      body: JSON.stringify(requestBody),
    })
      .then((res) => res.json())
      .then((result) => {
        if (result["ok"]) {
          updateNameResult.textContent = `Update Successfully`;
          memberName.textContent = requestBody["name"];
        }
      })
      .catch((error) => {
        console.error("Error:", error);
      });
  }
});
