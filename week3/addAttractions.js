const srcFavoriteIcon = "./img/favorite.svg";
const imgShowcaseSmall = document.querySelector("#img-showcase-sm");
const imgShowcase = document.querySelector("#img-showcase");
const showcaseMoreBtn = document.querySelector("#showcase-more-btn");
const numImgShowCaseSmall = 3;
const numImgShowCase = 12;
let result;
let countResult = 0;

const getAttractions = async () => {
  const patternImg = /https?:\/\/[^\s]*?\.(?:jpg|JPG)/;
  let url =
    "https://padax.github.io/taipei-day-trip-resources/taipei-attractions-assignment.json";

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
      console.log(result);

      addShowCaseSmall();
      addShowCase();
    })
    .catch((error) => {
      console.error(error);
    });
};

function addShowCaseSmall() {
  let data = result.slice(countResult);
  for (let i = 0; i < numImgShowCaseSmall; i++) {
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

    imgShowcaseSmall.appendChild(fragment);
    countResult++;
  }
}

function addShowCase() {
  let data = result.slice(countResult);
  let numImg =
    numImgShowCase < result.length - countResult
      ? numImgShowCase
      : result.length - countResult;

  for (let i = 0; i < numImg; i++) {
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

    let favoriteIcon = document.createElement("img");
    favoriteIcon.classList.add("card-favorite-icon");
    favoriteIcon.setAttribute("src", srcFavoriteIcon);
    favoriteIcon.setAttribute("alt", "promotion");

    // fragment append
    const fragment = document.createDocumentFragment();
    const cardFragment = fragment
      .appendChild(card)
      .appendChild(cardImage)
      .appendChild(image);
    cardImage.insertAdjacentElement("afterend", cardTitle);
    cardImage.insertAdjacentElement("afterend", favoriteIcon);

    imgShowcase.appendChild(fragment);
    countResult++;
  }
  if (countResult >= result.length) {
    showcaseMoreBtn.style.display = "none";
  }
}

getAttractions();
