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