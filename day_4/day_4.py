import numpy as np

with open("input.txt", "r", newline = "\n") as f:
    file = f.read().splitlines()

# Puzzle 1
contained_pairs = 0

for line in file:
    pairs = line.split(",")
    left_pair = pairs[0].split("-")
    right_pair = pairs[1].split("-")
    
    if ((int(left_pair[0]) >= int(right_pair[0])) 
        and (int(left_pair[1]) <= int(right_pair[1]))):
            contained_pairs += 1
    elif ((int(left_pair[0]) <= int(right_pair[0])) 
        and (int(left_pair[1]) >= int(right_pair[1]))):
            contained_pairs += 1

print(f"Number of contained pairs is {contained_pairs}")

# Puzzle 2
overlaps = 0

for line in file:
    pairs = line.split(",")
    left_pair = pairs[0].split("-")
    right_pair = pairs[1].split("-")

    nums = np.linspace(int(left_pair[0]), int(left_pair[1]),
                        int(left_pair[1]) - int(left_pair[0]) + 1)

    for num in nums:
        if ((round(num) >= int(right_pair[0])) 
            and (round(num) <= int(right_pair[1]))):
                overlaps += 1
                break

print(f"Number of any overlaps {overlaps}")
