with open("input.txt", "r", newline="\n") as f:
    file = f.read().splitlines()

elf_array = []
temp_arr = []
cal_sums = []

for cal in file:
    if cal:
        temp_arr.append(cal)
    else:
        elf_array.append(temp_arr)
        temp_arr = []

for elf in elf_array:
    total_cal = 0
    for cal in elf:
        total_cal += int(cal)
    cal_sums.append(total_cal)

print("Max calories: {}".format(max(cal_sums)))

sorted_cals = sorted(cal_sums, reverse = True)
cals_of_max = sum(sorted_cals[0:3])

print("Calories of top 3 elves: {}".format(cals_of_max))
