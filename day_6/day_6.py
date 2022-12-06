with open("input.txt", "r") as f:
    file = f.read()

# Puzzle 1
def check_unique(input: str) -> bool:
    """Checks if all values in input are unique"""
    input_arr = [letter for letter in input]
    for val in input_arr:
        temp_arr = input_arr.copy()
        temp_arr.remove(val)
        if val in temp_arr:
            return False

    return True
    
indx = 0
found_unique = False

while not found_unique:
    string = file[indx:indx+4]
    if check_unique(string):
        found_unique = True
    else:
        indx += 1

print(f"Start of packet: {indx + 4}")

