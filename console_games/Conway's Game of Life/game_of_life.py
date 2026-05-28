import time as t

X_SIZE = 10
Y_SIZE = 10
DEAD = ' '
ALIVE = '#'
place = [[DEAD for x in range(X_SIZE)] for y in range(Y_SIZE)]

def print_matrix(matrix: list) -> None:
    output = ''
    for y in range(len(matrix)):
        for x in range(len(matrix[y])):
            output += f'[{matrix[y][x]}]'
        output += '\n'
    print(output)

def next_generation(matrix: list) -> list:
    new_place = [[DEAD for x in range(len(matrix[0]))] for y in range(len(matrix))]
    count = 0
    for y in range(len(matrix)):
        for x in range(len(matrix[y])):
            for dy in [-1, 0, 1]:
                for dx in [-1, 0, 1]:
                    if dx == dy == 0:
                        continue
                    if matrix[(y + dy) % len(matrix)][(x + dx) % len(matrix[y])] == ALIVE:
                        count += 1
            if count == 3 and matrix[y][x] == DEAD or 2 <= count <= 3 and matrix[y][x] == ALIVE:
                new_place[y][x] = ALIVE
            else:
                new_place[y][x] = DEAD
            count = 0
    return new_place

place[1][6] = ALIVE
place[2][7] = ALIVE
place[2][8] = ALIVE
place[3][7] = ALIVE
place[3][6] = ALIVE

place[5][1] = ALIVE
place[6][2] = ALIVE
place[6][3] = ALIVE
place[7][2] = ALIVE
place[7][1] = ALIVE

print_matrix(place)
while True:
    place = next_generation(place)
    print_matrix(place)
    t.sleep(0.1)