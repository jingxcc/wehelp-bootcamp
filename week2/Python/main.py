# ANSI color in Terminal
COLOR_BLUE = "\033[104m"
COLOR_END = "\033[0m"


def print_task(task_name):
    print(f"{COLOR_BLUE}=== {task_name} ==={COLOR_END}")


print_task("Task 1")


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
print("--- test ---")
find_and_print(
    {
        "Bob": "My name is Bob. I'm 18 years old.",
        "Mary": "Hello, glad to meet you.",
        "Copper": "I'm a college student. Nice to meet you.",
        "Leslie": "I am of legal age in Taiwan.",
        "Vivian": "I will vote for Donald Trump next week",
        "Jenny": "Good morning.",
        "test1": "hhhh",
        "test2": "vote for teens",
    }
)

print_task("Task 2")


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
        bonus_total = 0
        weight_total = 0

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
        weight_total += employee["weight"]
    bonus_total = int(int(BONUS_LIMIT / weight_total) * weight_total)
    print(bonus_total)


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
                "salary": "40,000",
                "performance": "below average",
                "role": "Sales",
            },
        ]
    }
)  # call calculate_sum_of_bonus function

print("--- test ---")

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
                "name": "test2",
                "salary": "500USD",
                "performance": "below average",
                "role": "Sales",
            },
        ]
    }
)  # call calculate_sum_of_bonus function

print_task("Task 3")


def func(*data):
    # your code here
    mid_name_count = {}
    for name in data:
        if name[1:2] in mid_name_count:
            mid_name_count[name[1:2]] += 1
        else:
            mid_name_count[name[1:2]] = 1

    unique_mid_name = [n for n in mid_name_count if mid_name_count[n] == 1]
    if len(unique_mid_name):
        for name in data:
            if name[1:2] in unique_mid_name:
                print(name)
    else:
        print("沒有")


func("彭⼤牆", "王明雅", "吳明")  # print 彭⼤牆
func("郭靜雅", "王立強", "林靜宜", "郭立恆", "林花花")  # print 林花花
func("郭宣雅", "林靜宜", "郭宣恆", "林靜花")  # print 沒有
print("--- test ---")
func("郭宣雅", "林靜宜", "郭宣恆", "林靜花", "林小花", "林阿花")  # print "林小花", "林阿花"


print_task("Task 4")


def get_number(index):
    # your code here
    NUM_SEQUENCE = [0, 4, 3, 7, 6, 10, 9, 13, 12, 16, 15]
    print(NUM_SEQUENCE[index])


get_number(1)  # print 4
get_number(5)  # print 10
get_number(10)  # print 15


# Optional
print_task("Task 5")


def find_index_of_car(seats, status, number):
    # your code here
    # find cars are available
    car_available = [idx for idx, stat in enumerate(status) if stat == 1]

    # find the most suitable car
    min_gap = float("inf")
    car_fit = -1
    for car in car_available:
        gap = seats[car] - number
        if gap >= 0 and gap < min_gap:
            min_gap = gap
            car_fit = car

    print(car_fit)


find_index_of_car([3, 1, 5, 4, 2], [0, 1, 0, 1, 1], 2)  # print 4
find_index_of_car([1, 0, 5, 1, 3], [0, 1, 0, 1, 1], 4)  # print -1
find_index_of_car([4, 6, 5, 8], [0, 1, 1, 1], 4)  # print 2

print("--- test ---")
find_index_of_car([2, 4, 3, 5], [0, 1, 1, 1], 3)  # print 2
