with open("input.txt", "r", newline = "\n") as f:
    file = f.read().splitlines()

crates = [["B", "L", "D", "T", "W", "C", "F", "M"], ["N", "B", "L"],
          ["J", "C", "H", "T", "L", "V"], ["S", "P", "J", "W"],
          ["Z", "S", "C", "F", "T", "L", "R"], 
          ["W", "D", "G", "B", "H", "N", "Z"], 
          ["F", "M", "S", "P", "V", "G", "C", "N"], 
          ["W", "Q", "R", "J", "F", "V", "C", "Z"], ["R", "P", "M", "L", "H"]]

moves = file[10:]

# Puzzle 1
for move in moves:
    movement = move.split(" ")
    crates_to_move = int(movement[1])
    original_crate = int(movement[3]) - 1
    new_crate = int(movement[5]) - 1
    
    while crates_to_move > 0:
        crate = crates[original_crate].pop()
        crates[new_crate].append(crate)
        crates_to_move -= 1

top_crates = ""

for crate in crates:
    top_crates += crate[-1]

print(f"The top crates are: {top_crates}")

# Puzzle 2
new_crates = [["B", "L", "D", "T", "W", "C", "F", "M"], ["N", "B", "L"],
          ["J", "C", "H", "T", "L", "V"], ["S", "P", "J", "W"],
          ["Z", "S", "C", "F", "T", "L", "R"], 
          ["W", "D", "G", "B", "H", "N", "Z"], 
          ["F", "M", "S", "P", "V", "G", "C", "N"], 
          ["W", "Q", "R", "J", "F", "V", "C", "Z"], ["R", "P", "M", "L", "H"]]

for move in moves:
    movement = move.split(" ")
    crates_to_move = int(movement[1])
    original_crate = int(movement[3]) - 1
    new_crate = int(movement[5]) - 1

    new_crates[new_crate] += new_crates[original_crate][len(new_crates[original_crate]) - crates_to_move:]
    new_crates[original_crate] = new_crates[original_crate][0:len(new_crates[original_crate]) - crates_to_move]

top_new_crates = ""

for crate in new_crates:
    top_new_crates += crate[-1]

print(f"The top crates are: {top_new_crates}")