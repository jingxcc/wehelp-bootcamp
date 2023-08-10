const checkSignup = () => {
  isEmpty = ["name", "username", "password"].some(
    (item) => document.forms["signUp"][item].value === ""
  );
  if (isEmpty) {
    alert("Please fill in all fields !");
  }

  return !isEmpty;
};

const checkSignIn = () => {
  isEmpty = ["username", "password"].some(
    (item) => document.forms["signIn"][item].value === ""
  );
  if (isEmpty) {
    alert("Please fill in all fields !");
  }

  return !isEmpty;
};
