const checkAgreePolicy = () => {
  let isChecked = document.forms["signIn"]["policy"].checked;
  if (!isChecked) {
    alert("Please check the checkbox first !");
    return false;
  }
};

const checkPositiveInt = () => {
  const positiveInt = document.getElementById("positiveInt");
  // let positiveInt = document.getElementsByName("positiveInt");
  let intValue = positiveInt.value;
  console.dir("hello");
  console.dir(intValue);
  //   const square_url = {{url_for('square')}};
  //   fetch
  //   {% block javascript %}
  //   const graphURL = {{ url_for('main.graph') }};
  //   {% endblock %}
  // let intValue = document.forms["square"]["positiveInt"].value;

  if (intValue <= 0) {
    alert("Please enter a positive number !");
    // console.dir(document.forms["square"]["positiveInt"]);
    // return false;
  } else {
    let data = {
      positive_num: intValue,
    };
    // fetch({{url_for("square",positive_num=intValue|tojson)}}, {
    //     "method": "POST",
    //     "headers": {"Content-Type": "application/json"},
    //     "body": JSON.stringify(data),
    // }).then(...)
    // document.forms["square"]["action"] = `/square/${intValue}`;
    // document.forms["square"]["action"] = {{url_for('index')}};
    // document.forms["square"].setAttributes["action"] += intValue;
    // console.log(document.forms["square"]["action"]);
  }
};
