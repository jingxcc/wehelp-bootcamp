const imgShowcaseSmall = document.querySelector("#img-showcase-sm");
const imgShowcase = document.querySelector("#img-showcase");

const getAttractions = async () => {
  const patternImg = /https?:\/\/[^\s]*?\.(?:jpg|JPG)/;
  let url =
    "https://padax.github.io/taipei-day-trip-resources/taipei-attractions-assignment.json";
  let result;

  fetch(url)
    .then((response) => {
      return response.json();
    })
    .then((data) => {
      let imageUrl;

      result = data["result"]["results"];
      result.forEach((item) => {
        imageUrl = item["file"].match(patternImg);
        if (imageUrl !== null) {
          item["image"] = imageUrl[0];
        }
      });
      addElement(result);
    })
    .catch((error) => {
      console.error(error);
    });
};

function addElement(data) {
  const numShowCaseSmall = 3;
  const numShowCase = 12;
  const srcFavoriteIcon = "./img/favorite.svg";

  for (let i = 0; i < numShowCaseSmall + numShowCase; i++) {
    // create elements
    let card = document.createElement("div");
    card.classList.add("card");
    let cardImage = document.createElement("div");
    cardImage.classList.add("card-image");

    let image = document.createElement("img");
    image.setAttribute("src", data[i]["image"]);
    image.setAttribute("alt", "promotion");
    let cardTitle = document.createElement("div");
    cardTitle.classList.add("card-title");
    cardTitle.textContent = data[i]["stitle"];

    // fragment append
    const fragment = document.createDocumentFragment();
    const cardFragment = fragment
      .appendChild(card)
      .appendChild(cardImage)
      .appendChild(image);
    cardImage.insertAdjacentElement("afterend", cardTitle);

    // respectively
    if (i < numShowCaseSmall) {
      imgShowcaseSmall.appendChild(fragment);
    } else {
      // create elements
      let favoriteIcon = document.createElement("img");
      favoriteIcon.classList.add("card-favorite-icon");
      favoriteIcon.setAttribute("src", srcFavoriteIcon);
      favoriteIcon.setAttribute("alt", "promotion");

      cardImage.insertAdjacentElement("afterend", favoriteIcon);

      imgShowcase.appendChild(fragment);
    }
  }
}

getAttractions();
