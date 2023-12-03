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
        return lines


def find_first_int(str):
    for char in str:
        if test_for_num(char) == True:
            return int(char)


def find_last_int(str):
    for char in str[::-1]:
        if test_for_num(char) == True:
            return int(char)


line_list = convert_file("input1.txt")

calibration_total = 0

for line in line_list:
    first_calibration_digit = find_first_int(line)
    second_calibration_digit = find_last_int(line)
    calibration_line_number = make_two_digit(
        first_calibration_digit, second_calibration_digit)
    calibration_total += calibration_line_number

print(calibration_total)
