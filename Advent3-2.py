import copy


def make_array(file_path):
    with open(file_path, 'r') as file:
        lines = file.readlines()
    array = [list(line.strip()) for line in lines]
    return (array)


def test_for_num(char):
    try:
        num = int(char)
        return True
    except ValueError:
        return False


def replace_with_N(array):
    for i in range(len(array)):
        for j in range(len(array[i])):
            if test_for_num(array[i][j]) == False and array[i][j] != '.':
                array[i][j] = 'N'
    return array


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
                            if n_array[i][j] != 'N':
                                n_array[i][j] = engine_array[i][j]
                                modified = True
                            break
                    if not modified:
                        modified = True
        for i in range(rows):
            for j in range(cols):
                if n_array[i][j] == 'N':
                    continue
                elif not test_for_num(n_array[i][j]) or n_array[i][j] == '.':
                    n_array[i][j] = ' '
    return (n_array)


def flatten_array(array):
    flattened_array = []
    for row in array:
        flattened_array.append(''.join(map(str, row)))
    return flattened_array


def create_smaller_array(original_array, i, j):
    start_row = max(0, i - 1)
    end_row = min(len(original_array), i + 2)
    start_col = max(0, j - 3)
    end_col = min(len(original_array[0]), j + 4)
    smaller_array = []
    for i in range(start_row, end_row):
        row = original_array[i][start_col:end_col]
        if len(row) < 7:
            row.extend([' '] * (7 - len(row)))
        smaller_array.append(row)
    while len(smaller_array) < 3:
        smaller_array.append([' '] * 7)
    smaller_array = smaller_array[:3]
    return smaller_array


def solve_each_n(array):
    n_array = copy.deepcopy(array)
    rows = len(n_array)
    cols = len(n_array[0])
    for i in range(rows):
        for j in range(cols):
            if (i, j) != (1, 3):
                n_array[i][j] = ' '
    working_array = is_next_to_n(n_array, array)
    working_array = is_next_to_int(working_array, array)
    working_array[1][3] = ' '
    working_array = flatten_array(working_array)
    array_ints = []
    for element in working_array:
        integers = [int(num) for num in element.split() if num.strip()]
        for integer in integers:
            array_ints.append(integer)
    if len(array_ints) == 2:
        return array_ints[0]*array_ints[1]
    else:
        return 0


def solve_array(array):
    rows = len(array)
    cols = len(array[0])
    count = 0
    for i in range(rows):
        for j in range(cols):
            if array[i][j] == 'N':
                smaller_array = create_smaller_array(array, i, j)
                answer = solve_each_n(smaller_array)
                count += answer
    return (count)


working_array = make_array('input3.txt')
working_array = replace_with_N(working_array)
answer = solve_array(working_array)
print(answer)
