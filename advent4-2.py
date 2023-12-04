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
        return matches


scratch_cards = make_lines("input4.txt")
card_index = [1]
card_index.extend([1] * (len(scratch_cards)-1))
i = 0

while i < len(card_index):
    score = solve_line(scratch_cards[i])
    for j in range(score):
        if i + j + 1 < len(card_index):
            card_index[i + j + 1] += card_index[i]
    i += 1

print(sum(card_index))
