def make_array(file_path):
    with open(file_path, 'r') as file:
        lines = file.readlines()
    array = [list(line.strip()) for line in lines]
    return (array)


def make_empty_array(arr):
    rows = len(arr)
    cols = len(arr[0]) if rows > 0 else 0
    blank_array = [[' ' for _ in range(cols)] for _ in range(rows)]
    return blank_array


def test_for_num(char):
    try:
        num = int(char)
        return True
    except ValueError:
        return False


def replace_with_N(original, blank):
    for i in range(len(original)):
        for j in range(len(original[i])):
            if test_for_num(original[i][j]) == False and original[i][j] != '.':
                blank[i][j] = 'N'
    return blank


def find_neighbours(i, j, x, y):
    neighbours = []
    if i > 0:
        neighbours.append([i-1, j])
    if i < x-1:
        neighbours.append([i+1, j])
    if j > 0:
        neighbours.append([i, j-1])
    if j < y-1:
        neighbours.append([i, j+1])
    if i > 0 and j > 0:
        neighbours.append([i-1, j-1])
    if i > 0 and j < y-1:
        neighbours.append([i-1, j+1])
    if i < x-1 and j > 0:
        neighbours.append([i+1, j-1])
    if i < x-1 and j < y-1:
        neighbours.append([i+1, j+1])
    return neighbours


def is_next_to_n(n_array, engine_array):
    rows = len(n_array)
    cols = len(n_array[0])
    for i in range(rows):
        for j in range(cols):
            neighbour_elements = find_neighbours(i, j, rows, cols)
            if test_for_num(engine_array[i][j]) == True:
                modified = False
                while not modified:
                    for cell in neighbour_elements:
                        if n_array[cell[0]][cell[1]] == 'N':
                            n_array[i][j] = engine_array[i][j]
                            modified = True
                    if not modified:
                        n_array[i][j] = " "
                        modified = True
            elif n_array[i][j] != "N":
                n_array[i][j] = " "
    return n_array


def find_row_neighbours(i, j, y):
    neighbours = []
    if j > 0:
        neighbours.append([i, j-1])
    if j < y-1:
        neighbours.append([i, j+1])
    return neighbours


def is_next_to_int(n_array, engine_array):
    rows = len(n_array)
    cols = len(n_array[0])
    for _ in range(3):
        for i in range(rows):
            for j in range(cols):
                if not test_for_num(n_array[i][j]):
                    neighbour_elements = find_row_neighbours(i, j, cols)
                    modified = False
                    for cell in neighbour_elements:
                        x, y = cell[0], cell[1]
                        if x >= 0 and x < rows and y >= 0 and y < cols and test_for_num(n_array[x][y]):
                            n_array[i][j] = engine_array[i][j]
                            modified = True
                            break
                    if not modified:
                        modified = True
        for i in range(rows):
            for j in range(cols):
                if not test_for_num(n_array[i][j]) or n_array[i][j] == '.':
                    n_array[i][j] = ' '
    return (n_array)


def flatten_array(array):
    flattened_array = []
    for row in array:
        flattened_array.append(''.join(map(str, row)))
    return flattened_array


def split_and_convert(array):
    all_integers = []
    for element in array:
        integers = [int(num) for num in element.split() if num.strip()]
        all_integers.extend(integers)
    return all_integers


given_array = make_array('input3.txt')
working_array = make_empty_array(given_array)
working_array = replace_with_N(given_array, working_array)
working_array = is_next_to_n(working_array, given_array)
working_array = is_next_to_int(working_array, given_array)
working_array = flatten_array(working_array)
toxic_int_list = split_and_convert(working_array)
print(sum(toxic_int_list))
