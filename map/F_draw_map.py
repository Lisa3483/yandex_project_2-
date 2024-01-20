def read_tiles(file_name):
    numbers = []
    with open(file_name, 'r') as file:
        for line in file:
            row = [int(num) for num in line.split()]
            numbers.append(row)
    return numbers


def write_2d_list_to_file(filename, two_dimensional_list):
    with open(filename, 'w') as file:
        for row in two_dimensional_list:
            file.write('\t'.join(map(str, row)) + '\n')


def read_col_tiles(file_name):
    numbers = []
    with open(file_name, 'r') as file:
        for line in file:
            row = [int(num) for num in line.split()]
            numbers.append(row)
    return numbers
