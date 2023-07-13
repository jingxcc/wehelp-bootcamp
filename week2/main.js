function printTask(taskName) {
  console.log(`%c=== ${taskName} ===`, "background-color: orange");
}

printTask("Task 1");
function findAndPrint(messages) {
  // write down your judgment rules in comments
  // If a message contains the following keywords, it is considered highly likely that the person is older than 17.
  //   1. "18 years old"
  //   2. "legal age"
  //   3. "college"
  //   4. "vote"

  // your code here, based on your own rules
  const msgKeywords = ["18 years old", "legal age", "college", "vote"];

  for (const name in messages) {
    msgKeywords.map((keyword) => {
      if (messages[name].includes(keyword)) {
        console.log(name);
      }
    });
  }
}
findAndPrint({
  Bob: "My name is Bob. I'm 18 years old.",
  Mary: "Hello, glad to meet you.",
  Copper: "I'm a college student. Nice to meet you.",
  Leslie: "I am of legal age in Taiwan.",
  Vivian: "I will vote for Donald Trump next week",
  Jenny: "Good morning.",
});

printTask("Task 2");
function calculateSumOfBonus(data) {
  // write down your bonus rule in comments
  // 1. First, exchanging currency in data by converting USD to TWD
  // 2. Assuming that I aim to allocate the maximum possible amount to employees within the given budget, I will distribute the budget based on a weighted system. The weight for each employee is calculated by multiplying their performance points by their salary.
  // 2.1. performance point calculation
  //   above average: 1.2
  //   average: 1
  //   below average: 0.8

  // your code here, based on your own rules
  const currencyExchange = [{ curr: "USD", rate: 30 }];
  const bonusLimit = 10000;
  const performancePoints = {
    "above average": 1.2,
    average: 1,
    "below average": 0.8,
  };
  let bonusTotalSpent = 0;
  let weightTotal = 0;

  // process data
  data.employees.map((employee) => {
    let salaryStr = employee.salary.toString().replaceAll(",", "");
    let salaryCurr = salaryStr.match(/[a-zA-Z]+/);
    let salary = 0;

    if (salaryStr) {
      salary = salaryStr.match(/\d+/g)[0];
    }
    if (salaryCurr) {
      let rate = 1;
      salaryCurr = salaryCurr[0].toUpperCase();

      rate = currencyExchange.find((item) => item.curr === salaryCurr).rate;
      salary *= rate;
    }
    employee.salary = parseInt(salary, 10);
  });

  // weight = performance point * salary
  data.employees.map((employee) => {
    employee.weight =
      (performancePoints[`${employee.performance}`] * employee.salary) / 10000;
    weightTotal += employee.weight;
  });
  bonusTotalSpent = parseInt(bonusLimit / weightTotal) * weightTotal;
  console.log(bonusTotalSpent);
}

calculateSumOfBonus({
  employees: [
    {
      name: "John",
      salary: "1000USD",
      performance: "above average",
      role: "Engineer",
    },
    {
      name: "Bob",
      salary: 60000,
      performance: "average",
      role: "CEO",
    },
    {
      name: "Jenny",
      salary: "50,000",
      performance: "below average",
      role: "Sales",
    },
  ],
}); // call calculateSumOfBonus function

printTask("Task 3");
function func(...data) {
  // your code here
  let uniqueMidName;
  let midNameCount = {};
  for (let i = 0; i < data.length; i++) {
    let midName = data[i].substring(1, 2);
    if (midName) {
      if (midName in midNameCount) {
        midNameCount[midName]++;
      } else {
        midNameCount[midName] = 1;
      }
    }
  }
  uniqueMidName = Object.keys(midNameCount).filter(
    (name) => midNameCount[name] === 1
  );

  if (uniqueMidName.length > 0) {
    for (let i = 0; i < data.length; i++) {
      if (uniqueMidName.includes(data[i].substring(1, 2))) {
        console.log(data[i]);
      }
    }
  } else {
    console.log("沒有");
  }
}
func("彭⼤牆", "王明雅", "吳明"); // print 彭⼤牆
func("郭靜雅", "王立強", "林靜宜", "郭立恆", "林花花"); // print 林花花
func("郭宣雅", "林靜宜", "郭宣恆", "林靜花"); // print 沒有

printTask("Task 4");
function getNumber(index) {
  // your code here
  const numSequence = [0, 4, 3, 7, 6, 10, 9, 13, 12, 16, 15];
  console.log(numSequence[index]);
}
getNumber(1); // print 4
getNumber(5); // print 10
getNumber(10); // print 15

// Optional
printTask("Task 5");

function findIndexOfCar(seats, status, number) {
  // your code here
  // find cars are available
  let carAvailable = [];
  status.map((stat, statIdx) => {
    if (stat) {
      carAvailable.push(statIdx);
    }
  });

  // find the most suitable car
  let minGap;
  let carFit = -1;
  carAvailable.map((car) => {
    if (seats[car] >= number) {
      if (carFit == -1) {
        minGap = seats[car] - number;
        carFit = car;
      } else {
        if (minGap > seats[car] - number) {
          minGap = seats[car] - number;
          carFit = car;
        }
      }
    }
  });
  console.log(carFit);
}
findIndexOfCar([3, 1, 5, 4, 2], [0, 1, 0, 1, 1], 2); // print 4
findIndexOfCar([1, 0, 5, 1, 3], [0, 1, 0, 1, 1], 4); // print -1
findIndexOfCar([4, 6, 5, 8], [0, 1, 1, 1], 4); // print 2
