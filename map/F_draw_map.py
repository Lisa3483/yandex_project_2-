TILE_ID_UP_DOWN_CROWN_1 = 96
TILE_ID_RIGHT_LEFT_CROWN_1 = 92
TILE_ID_CROWN_2 = 88
TILE_ID_RIGHT_LEFT_CROWN_3 = 85
TILE_ID_UP_RIGHT_ANGLE = 100
TILE_ID_UP_LEFT_ANGLE = 95


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


def draw_map(tiles, x, y):
    tiles[-3, :] = TILE_ID_UP_DOWN_CROWN_1

    tiles[:, 2] = TILE_ID_RIGHT_LEFT_CROWN_1
    tiles[:, -3] = TILE_ID_RIGHT_LEFT_CROWN_3
    tiles[1, :] = TILE_ID_CROWN_2
    tiles[:, 1] = TILE_ID_CROWN_2
    tiles[:, 0] = TILE_ID_RIGHT_LEFT_CROWN_3
    tiles[:, -2] = TILE_ID_CROWN_2
    tiles[0, :] = TILE_ID_UP_DOWN_CROWN_1
    tiles[:, -1] = TILE_ID_RIGHT_LEFT_CROWN_1
    tiles[0][-1] = TILE_ID_UP_RIGHT_ANGLE
    tiles[0][0] = TILE_ID_UP_LEFT_ANGLE
    tiles[-2, :] = TILE_ID_CROWN_2
    tiles[-1, :] = TILE_ID_CROWN_2
    for i in range(3, len(tiles[0]) - 3, 3):
        tiles[2][i] = 78
        tiles[2][i + 1] = 79
        tiles[2][i + 2] = 80
        tiles[3][i] = 68
        tiles[3][i + 1] = 69
        tiles[3][i + 2] = 70
        tiles[4][i] = 58
        tiles[4][i + 1] = 59
        tiles[4][i + 2] = 60
        tiles[5][i] = 50
        tiles[5][i + 1] = 51
        tiles[5][i + 2] = 52
    for i in range(10):
        x1 = -10
        y1 = 10
        flag = 1
        if flag == 1:
            for j in range(5):
                tiles[x1][y1] = 18
                x1 -= j
            flag = 2
        elif flag == 2:
            for j in range(5):
                tiles[x1][y1] = 18
                y1 += j
            flag = 3
        elif flag == 3:
            for j in range(5):
                tiles[x1][y1] = 18
                x1 += j
            flag = 4
        elif flag == 4:
            for j in range(5):
                tiles[x1][y1] = 18
                y1 -= j
            flag = 1

    write_2d_list_to_file('output.txt', tiles)
    return tiles
