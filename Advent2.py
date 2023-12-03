import re


def parse_games(line):
    line = line.replace(" ", "")
    game = line.split(":")
    game[1] = re.split(r'[;,]', game[1])
    return game


def compile_scores(game):
    result = [0, [], [], []]
    result[0] += int(game[0][4:])
    for count in game[1]:
        if count[-1] == "d":
            result[1].append(int(count[:-3]))
        elif count[-1] == "e":
            result[3].append(int(count[:-4]))
        else:
            result[2].append(int(count[:-5]))
    return result


def check_game(scores):
    possible = True
    for i in range(1, 4):
        for score in scores[i]:
            if score > (11 + i):
                possible = False
                break
    return possible


def convert_file(file_name):
    with open(file_name, 'r') as file:
        lines = file.readlines()
        lines = [line.strip() for line in lines]
        return lines


lines = convert_file("input2.txt")
answer = 0
for line in lines:
    split_line = parse_games(line)
    line_scores = compile_scores(split_line)
    possible_test = check_game(line_scores)
    if possible_test == True:
        answer += line_scores[0]
print(answer)
