const checkAgreePolicy = () => {
  let isChecked = document.forms["signIn"]["policy"].checked;
  if (!isChecked) {
    alert("Please check the checkbox first !");
    return false;
  }
};
