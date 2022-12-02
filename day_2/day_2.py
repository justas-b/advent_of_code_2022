# A: rock
# B: paper
# C: scissors

# X: rock
# Y: paper
# Z: scissors

# rock: 1
# paper: 2
# scissors: 3

# loss: 0
# draw: 3
# win: 6

rounds = []
scores = []
option_scores = {"X": 1, "Y": 2, "Z": 3}
op_to_me_map = {"A": "X", "B": "Y", "C": "Z"}

for line in open("input.txt", "r"):
    rounds.append(line.strip())

for round in rounds:
    op_option = op_to_me_map[round[0]]
    my_option = round[2]
    score = option_scores[my_option]

    if op_option == my_option:
        score += 3
    elif op_option == "X" and my_option == "Y":
        score += 6
    elif op_option == "Y" and my_option == "Z":
        score +=6
    elif op_option == "Z" and my_option == "X":
        score +=6

    scores.append(score)

print(f"Total score is: {sum(scores)}")
