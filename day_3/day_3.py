# split the item into compartments (half)
# loop through both compartments and look for identical items
# calculate priority of the item
# sum all the priorities
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

print(f"The total sum is {round(total_sum)}")


    
