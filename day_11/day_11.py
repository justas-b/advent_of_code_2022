import math

with open("input.txt", "r", newline="\n") as f:
    file = f.read().splitlines()

# Puzzle 1
monkeys_items = {}
monkey_rules = {}
monkey_checks = {}
current_monkey = 0

for line in file:
    line = line.strip()
    if line.startswith("Monkey"):
        current_monkey = int(line.split(":")[0].split(" ")[-1])
        monkeys_items[current_monkey] = []
        monkey_rules[current_monkey] = []
        monkey_checks[current_monkey] = 0
    elif line.startswith("Starting"):
        items = line.split(":")
        monkeys_items[current_monkey] = [int(val) for val in items[-1].strip().split(", ")]
    elif line.startswith("Operation"):
        monkey_rules[current_monkey].append(line.split("= ")[-1])
    elif line.startswith("Test"):
        monkey_rules[current_monkey].append(line.split("by ")[-1])
    elif line.startswith("If true"):
        monkey_rules[current_monkey].append(line.split("monkey ")[-1])
    elif line.startswith("If false"):
        monkey_rules[current_monkey].append(line.split("monkey ")[-1])


def do_operation(operation: str, input: int) -> int:
    """Do the operation on the input according to the monkeys rule"""
    output = input
    op_list = operation.split(" ")
    op = op_list[1]
    operate_on = op_list[2]

    if op == "+":
        if operate_on == "old":
            return math.floor((output + input) / 3)
        else:
            return math.floor((output + int(operate_on)) / 3)
    elif op == "-":
        if operate_on == "old":
            return math.floor((output - input) / 3)
        else:
            return math.floor((output - int(operate_on)) / 3)
    elif op == "*":
        if operate_on == "old":
            return math.floor((output * input) / 3)
        else:
            return math.floor((output * int(operate_on)) / 3)


def check_divisible(worry:int, by: int, true: int, false: int) -> int:
    """Checks whether worry level is divisible and what monkey it is thrown to"""
    return true if (worry % by == 0) else false


for i in range(20):
    for monkey in monkeys_items:
        rules = monkey_rules[monkey]
        for item in list(monkeys_items[monkey]):
            monkey_checks[monkey] += 1
            monkeys_items[monkey].remove(item)
            worry = do_operation(rules[0], int(item))
            throw_to = check_divisible(worry, int(rules[1]), int(rules[2]), int(rules[3]))
            monkeys_items[throw_to].append(worry)

checks = list(monkey_checks.values())
checks.sort(reverse=True)
print(f"Level of monkey business: {checks[0] * checks[1]}")