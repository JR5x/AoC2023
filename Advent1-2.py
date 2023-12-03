import re


def test_for_num(char):
    try:
        num = int(char)
        return True
    except ValueError:
        return False


def make_two_digit(first_int, second_int):
    return 10*first_int + second_int


def convert_file(file_name):
    with open(file_name, 'r') as file:
        lines = file.readlines()
        lines = [line.strip() for line in lines]
        return lines


def find_first_int(str):
    for char in str:
        if test_for_num(char) == True:
            return int(char)


def replace_first_text_number(text):
    replacements = {
        "one": "1",
        "two": "2",
        "three": "3",
        "four": "4",
        "five": "5",
        "six": "6",
        "seven": "7",
        "eight": "8",
        "nine": "9"
    }

    pattern = re.compile(
        r'(one|two|three|four|five|six|seven|eight|nine)', re.IGNORECASE)

    match = pattern.search(text)

    if match:
        word = match.group().lower()
        return text[:match.start()] + replacements[word] + text[match.end():]

    return text


def replace_last_text_number(text):
    replacements = {
        "eno": "1",
        "owt": "2",
        "eerht": "3",
        "ruof": "4",
        "evif": "5",
        "xis": "6",
        "neves": "7",
        "thgie": "8",
        "enin": "9"
    }

    pattern = re.compile(
        r'(eno|owt|eerht|ruof|evif|xis|neves|thgie|enin)', re.IGNORECASE)

    match = pattern.search(text)

    if match:
        word = match.group().lower()
        return text[:match.start()] + replacements[word] + text[match.end():]

    return text


def reverse_string(input_string):
    return input_string[::-1]


line_list = convert_file("input1.txt")

calibration_total = 0

for line in line_list:
    line1 = replace_first_text_number(line)
    line2 = reverse_string(line)
    line3 = replace_last_text_number(line2)
    first_calibration_digit = find_first_int(line1)
    second_calibration_digit = find_first_int(line3)
    calibration_line_number = make_two_digit(
        first_calibration_digit, second_calibration_digit)
    calibration_total += calibration_line_number

print(calibration_total)
