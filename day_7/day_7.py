with open("input.txt", "r", newline = "\n") as f:
    file = f.read().splitlines()

# Puzzle 1
directories = []
directories_dict = {}

for line in file:
    if line[:4] == "$ cd" and line[5:] != "..":
        directories.append(line[5:])
        directories_dict[line[5:]] = []

dir = ""
for line in file:
    if line[:4] == "$ cd" and line[5:] != "..":
        dir = line[5:]
    
    if line[:3] == "dir":
        directories_dict[dir].append(line[4:])

print(directories_dict)