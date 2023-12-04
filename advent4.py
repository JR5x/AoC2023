import re


def make_lines(file_path):
    with open(file_path, 'r') as file:
        lines = file.readlines()
    return (lines)


def solve_line(line):
    split_line = re.split(r'[:|]', line)
    winning_numbers = [int(num) for num in split_line[1].strip().split()]
    game_numbers = [int(num) for num in split_line[2].strip().split()]
    matches = 0
    for number in winning_numbers:
        if number in game_numbers:
            matches += 1
    if matches == 0:
        return 0
    else:
        return 2 ** (matches - 1)


scratch_cards = make_lines("input4.txt")
total = 0

for line in scratch_cards:
    score = solve_line(line)
    total += score
print(total)
