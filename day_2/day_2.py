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

# Puzzle 1
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

# Puzzle 2
# X: lose
# Y: draw
# Z: win
op_option_index_map = {"X": 0, "Y": 1, "Z": 2}
# how many points you would get given what outcome you want and what the
# opponents hand is e.g. if you want to lose and the opponent has X (rock), then
# you would want to play Z (scissors) == 3 points
win_point_map = {"X": [3, 1 ,2], "Y": [1, 2, 3], "Z": [2, 3 ,1]}
adjusted_scores = []
win_hand_map = {"X": 0, "Y": 3, "Z": 6}

for round in rounds:
    score = win_hand_map[round[2]]
    score += win_point_map[round[2]][op_option_index_map[op_to_me_map[round[0]]]]
    adjusted_scores.append(score)

print(f"Total adjusted score is: {sum(adjusted_scores)}")