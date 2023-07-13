# print color in Terminal
colorBlue = "\033[104m"
colorEnd = "\033[0m"


def printTask(taskName):
    print(f"{colorBlue}=== {taskName} ==={colorEnd}")


printTask("Task 1")


def find_and_print(messages):
    # write down your judgment rules in comments
    # If a message contains the following keywords, it is considered highly likely that the person is older than 17.
    #     1. "18 years old"
    #     2. "legal age"
    #     3. "college"
    #     4. "vote"

    # your code here, based on your own rules
    MSG_KEYWORDS = {"18 years old", "legal age", "college", "vote"}

    for name in messages:
        for keyword in MSG_KEYWORDS:
            if keyword in messages[name]:
                print(name)


find_and_print(
    {
        "Bob": "My name is Bob. I'm 18 years old.",
        "Mary": "Hello, glad to meet you.",
        "Copper": "I'm a college student. Nice to meet you.",
        "Leslie": "I am of legal age in Taiwan.",
        "Vivian": "I will vote for Donald Trump next week",
        "Jenny": "Good morning.",
    }
)

printTask("Task 2")


def calculate_sum_of_bonus(data):
    # write down your bonus rules in comments
    # 1. First, exchanging currency in data by converting USD to TWD
    # 2. Assuming that I aim to allocate the maximum possible amount to employees within the given budget, I will distribute the budget based on a weighted system. The weight for each employee is calculated by multiplying their performance points by their salary.
    # 2.1. performance point calculation
    #     above average: 1.2
    #     average: 1
    #     below average: 0.8

    # your code here, based on your own rules
    for employee in data["employees"]:
        CURRENCY_EXCHANGE = [{"curr": "USD", "rate": 30}]
        BONUS_LIMIT = 10000
        PERFORM_POINTS = {
            "above average": 1.2,
            "average": 1,
            "below average": 0.8,
        }
        bonusTotalSpent = 0
        weightTotal = 0

        # process data
        salaryStr = str(employee["salary"]).replace(",", "")
        salary = ""
        salaryCurr = ""
        for s in salaryStr:
            if s.isdigit():
                salary += s
            else:
                salaryCurr += s
        salary = int(salary)

        if salaryCurr != "":
            for item in CURRENCY_EXCHANGE:
                if item["curr"] == salaryCurr:
                    salary *= item["rate"]
                    break

        employee["salary"] = salary

    # weight = performance point * salary
    for employee in data["employees"]:
        employee["weight"] = (
            PERFORM_POINTS[employee["performance"]] * employee["salary"] / 10000
        )
        weightTotal += employee["weight"]
    bonusTotalSpent = int(int(BONUS_LIMIT / weightTotal) * weightTotal)
    print(bonusTotalSpent)


calculate_sum_of_bonus(
    {
        "employees": [
            {
                "name": "John",
                "salary": "1000USD",
                "performance": "above average",
                "role": "Engineer",
            },
            {"name": "Bob", "salary": 60000, "performance": "average", "role": "CEO"},
            {
                "name": "Jenny",
                "salary": "50,000",
                "performance": "below average",
                "role": "Sales",
            },
        ]
    }
)  # call calculate_sum_of_bonus function

printTask("Task 3")


def func(*data):
    # your code here
    midNameCount = {}
    for name in data:
        if name[1:2] in midNameCount:
            midNameCount[name[1:2]] += 1
        else:
            midNameCount[name[1:2]] = 1

    uniqueMidName = [n for n in midNameCount if midNameCount[n] == 1]
    if len(uniqueMidName):
        for name in data:
            if name[1:2] in uniqueMidName:
                print(name)
    else:
        print("沒有")


func("彭⼤牆", "王明雅", "吳明")  # print 彭⼤牆
func("郭靜雅", "王立強", "林靜宜", "郭立恆", "林花花")  # print 林花 花
func("郭宣雅", "林靜宜", "郭宣恆", "林靜花")  # print 沒有


printTask("Task 4")


def get_number(index):
    # your code here
    NUM_SEQUENCE = [0, 4, 3, 7, 6, 10, 9, 13, 12, 16, 15]
    print(NUM_SEQUENCE[index])


get_number(1)  # print 4
get_number(5)  # print 10
get_number(10)  # print 15


# Optional
printTask("Task 5")


def find_index_of_car(seats, status, number):
    # your code here
    # find cars are available
    carAvailable = []
    for statIdx, stat in enumerate(status):
        if stat == 1:
            # carAvailable.append(statIdx)
            carAvailable += [statIdx]
    print(carAvailable)

    # find the most suitable car
    carFit = -1
    for car in carAvailable:
        if seats[car] >= number:
            if carFit == -1:
                minGap = seats[car] - number
                carFit = car
            else:
                if (minGap) > seats[car] - number:
                    minGap = seats[car] - number
                    carFit = car
    print(carFit)


find_index_of_car([3, 1, 5, 4, 2], [0, 1, 0, 1, 1], 2)  # print 4
find_index_of_car([1, 0, 5, 1, 3], [0, 1, 0, 1, 1], 4)  # print -1
find_index_of_car([4, 6, 5, 8], [0, 1, 1, 1], 4)  # print 2
