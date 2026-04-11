import random as r
import os
import platform

while True:
    try:
        size = int(input('Размер поля: '))
        break
    except ValueError:
        print('Указан неверный размер поля!')
place = [[0] * size for _ in range(size)]
bomb_x = -1
bomb_y = -1
bombs = (size ** 2) // 10
bombs_placed = 0
end_check = 1
end = -1

EMPTY = 0
EMPTY_HIDDEN = 100
BOMB = -1
BOMB_HIDDEN = 1000

def clear() -> None:
    if platform.system() == "Windows":
        os.system('cls')
    else:
        os.system('clear')

def numbers(matrix: list, xn: int, yn: int) -> list:
    for dy2 in [-1, 0, 1]:
        for dx2 in [-1, 0, 1]:
            if dx2 == 0 and dy2 == 0:
                continue
            if matrix[yn][xn] != BOMB:
                if 0 <= xn + dx2 < len(matrix[0]) and 0 <= yn + dy2 < len(matrix):
                    if matrix[yn + dy2][xn + dx2] == BOMB:
                        matrix[yn][xn] += 1
    return matrix

def fill(matrix: list, x_fill: int, y_fill: int, value) -> list:
    for dy3 in [-1, 0, 1]:
        for dx3 in [-1, 0, 1]:
            if dy3 == 0 and dx3 == 0:
                continue
            if 0 <= y_fill + dy3 < len(matrix) and 0 <= x_fill + dx3 < len(matrix[0]):
                if matrix[y_fill + dy3][x_fill + dx3] == EMPTY_HIDDEN:
                    matrix[y_fill + dy3][x_fill + dx3] = value
                    fill(place, x_fill + dx3, y_fill + dy3, 0)
                elif 10 <= matrix[y_fill + dy3][x_fill + dx3] <= 80:
                    matrix[y_fill + dy3][x_fill + dx3] //= 10
    return matrix

# Bomb Places
while bombs_placed != bombs:
    bomb_x = r.randint(0, len(place[0]) - 1)
    bomb_y = r.randint(0, len(place) - 1)
    if place[bomb_y][bomb_x] == EMPTY:
        place[bomb_y][bomb_x] = BOMB
        bombs_placed += 1

# Numbers Places
for y1 in range(len(place)):
    for x1 in range(len(place[0])):
        numbers(place, x1, y1)

# Beginning
for y2 in range(len(place)):
    for x2 in range(len(place[0])):
        if place[y2][x2] == BOMB:
            place[y2][x2] = BOMB_HIDDEN
        elif place[y2][x2] == EMPTY:
            place[y2][x2] = EMPTY_HIDDEN
        else:
            place[y2][x2] *= 10

# Print
while end == -1:
    clear()
    for ypr in range(len(place)):
        for xpr in range(len(place[0])):
            if place[ypr][xpr] == EMPTY:
                if xpr < len(place) - 1:
                    print(f'[ ]', end='')
                else:
                    print(f'[ ]')
            elif place[ypr][xpr] < 0:
                if xpr < len(place) - 1:
                    print(f'[¶]', end='')
                else:
                    print(f'[¶]')
            elif place[ypr][xpr] > 9:
                if xpr < len(place) - 1:
                    print(f'[#]', end='')
                else:
                    print(f'[#]')
            else:
                if xpr < len(place) - 1:
                    print(f'[{place[ypr][xpr]}]', end='')
                else:
                    print(f'[{place[ypr][xpr]}]')
    try:
        x, y, flag = map(int, input().split())
        if 1 <= x <= len(place[0]) and 1 <= y <= len(place):
            if flag == 1:
                if not (1 <= place[y - 1][x - 1] <= 8):
                    place[y - 1][x - 1] *= -1
            if place[y - 1][x - 1] > 9 and flag != 1 and place[y - 1][x - 1] > -2:
                if place[y - 1][x - 1] == EMPTY_HIDDEN:
                    place[y - 1][x - 1] = EMPTY
                    fill(place, x - 1, y - 1, EMPTY)
                elif place[y - 1][x - 1] == BOMB_HIDDEN:
                    end = 1
                else:
                    place[y - 1][x - 1] = int((str(place[y - 1][x - 1]))[:-1])
    except ValueError:
        continue

    # End Check
    for cy in range(len(place)):
        for cx in range(len(place[0])):
            if 10 <= place[cy][cx] <= EMPTY_HIDDEN or -EMPTY_HIDDEN <= place[cy][cx] <= -10:
                end_check = 0
    if end_check == 1:
        end = 0
    end_check = 1

# End
if end == 0:
    print('Вы выиграли!')
if end == 1:
    print('Вы проиграли!')