import numpy as np

with open("input.txt", "r", newline = "\n") as f:
    file = f.read().splitlines()

# Puzzle 1
letters = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
priorities = np.linspace(1, 52, 52)
total_sum = 0
matching_letters = []

letter_priority_map = dict(zip(letters, priorities))

for item in file:
    first_compartment = item[:round(len(item) / 2)]
    second_compartment = item[round(len(item) / 2):]

    for first_letter in first_compartment:
        found_letter = False
        for second_letter in second_compartment:
            if first_letter == second_letter:
                matching_letters.append(first_letter)
                total_sum += letter_priority_map[first_letter]
                found_letter = True
                break
        if found_letter:
            break

print(f"The total sum is {round(total_sum)}") # 7795

# Puzzle 2
groups = []
group_sum = 0

group = 0
while group != (len(file) / 3):
    bag_1 = file[group * 3]
    bag_2 = file[(group * 3) + 1]
    bag_3 = file[(group * 3) + 2]

    for letter in bag_1:
        if (letter in bag_2) & (letter in bag_3):
            groups.append(letter)
            group_sum += letter_priority_map[letter]
            break
    
    group += 1

print(f"The sum of the groups is {round(group_sum)}")

