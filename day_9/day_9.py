with open("test2.txt", "r", newline="\n") as f:
    file = f.read().splitlines()

# Puzzle 1
h_pos = [[0, 0]]
t_pos = [[0, 0]]
unique_visits = [[0, 0]]


def move_head(direction: str, pos: list) -> list:
    """Move the head in a given direction by an increment of 1"""
    movements = {"R": 1, "L": -1, "U": 1, "D": -1}
    new_pos = pos.copy()

    if direction in ["R", "L"]:
        new_pos[0] += movements[direction]
    else:
        new_pos[1] += movements[direction]

    return new_pos


def surrounds(pos: list) -> list[list]:
    """Positions surrounding the current position"""
    displacement = [-1, 0, 1]
    surrounds_pos = []

    for i in displacement:
        for j in displacement:
            surrounds_pos.append([pos[0] + i, pos[1] + j])

    return surrounds_pos


def check_touching(h_pos: list, t_pos: list) -> bool:
    """Checks if the head and tail are touching"""
    surround = surrounds(h_pos)

    return True if t_pos in surround else False


def move_tail(prev_h: list, h_pos: list, t_pos: list) -> list:
    """Moves the tail towards the head"""
    if not check_touching(h_pos, t_pos):
        return prev_h
    else:
        return t_pos


for move in file:
    dir_step = move.split(" ")
    for step in range(1, int(dir_step[1]) + 1):
        h_pos.append(move_head(dir_step[0], h_pos[-1]))
        t_pos.append(move_tail(h_pos[-2], h_pos[-1], t_pos[-1]))

        if t_pos[-1] not in unique_visits:
            unique_visits.append(t_pos[-1])

print(f"Number of unique visit is {len(unique_visits)}")

# Puzzle 2
prev = [[0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], 
        [0, 0], [0, 0]]
cur = [[0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], 
        [0, 0], [0, 0]]
new_unique = []


def move_rope(prev: list[list], h_pos: list) -> list[list]:
    """Moves the new rope"""
    new_rope = prev.copy()
    new_rope[-1] = h_pos
    
    for i in range(2, 11):
        new_rope[-i] = move_tail(prev[-i + 1], new_rope[-i + 1], prev[-i])
    
    return new_rope


for move in file:
    dir_step = move.split(" ")
    for step in range(1, int(dir_step[1]) + 1):
        new_head = move_head(dir_step[0], prev[-1])
        cur = move_rope(prev, new_head)
        prev = cur.copy()

        if cur[0] not in new_unique:
            new_unique.append(cur[0])

print(len(new_unique))