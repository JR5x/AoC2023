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


def get_max(scores):
    power_set = []
    for i in range(1, 4):
        max_score = 0
        for score in scores[i]:
            if score > max_score:
                max_score = score
        power_set.append(max_score)
    answer = 1
    for number in power_set:
        answer *= number
    return answer


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
    game_power = get_max(line_scores)
    answer += game_power


print(answer)
