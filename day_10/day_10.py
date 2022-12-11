import math

with open("input.txt", "r", newline="\n") as f:
    file = f.read().splitlines()

# Puzzle 1
X = 1
cycle = 0
cycles = {20: 0, 60: 0, 100: 0, 140: 0, 180: 0, 220: 0}

for line in file:
    if line == "noop":
        cycle += 1
        if cycle in list(cycles.keys()):
            cycles[cycle] = X
    else:
        split_line = line.split(" ")
        for i in range(0, 2):
            cycle += 1
            if cycle in list(cycles.keys()):
                cycles[cycle] = X
        X += int(split_line[1])


def signal_strength(cycles: dict) -> int:
    """Determines the signal strength given the cycles"""
    signal_strength = 0

    for key in cycles:
        signal_strength += key * cycles[key]

    return signal_strength


print(f"The sum of the signal strengths is {signal_strength(cycles)}")

# Puzzle 2
image = [[], [], [], [], [], [],]
new_cycle = -1
new_X = 1


def sprite_pos(cycle: int, X: int) -> list:
    """Gets the current position of the sprite given the cycle"""
    row = math.floor(cycle / 40)
    offset = 40 * row

    return [(X - 1) + offset, (X) + offset, (X + 1) + offset]


def draw_pixel(sprite: list, cycle: int) -> str:
    """Draws a pixel if the sprite in on the same line as the cycle"""
    if cycle in sprite:
        return "#"
    else:
        return "."


for line in file:
    if line == "noop":
        new_cycle += 1
        row = math.floor(new_cycle / 40)
        image[row].append(draw_pixel(sprite_pos(new_cycle, new_X), new_cycle))
    else:
        split_line = line.split(" ")
        for i in range(0, 2):
            new_cycle += 1
            row = math.floor(new_cycle / 40)
            image[row].append(draw_pixel(sprite_pos(new_cycle, new_X), new_cycle))

        new_X += int(split_line[1])

for row in image:
    print("".join(row))