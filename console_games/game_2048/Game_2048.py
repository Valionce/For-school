import random as r
import os
import platform

place_x = ''
place_y = ''
while type(place_x) != int:
    try:
        place_x = int(input('Enter size of the place (x): '))
    except ValueError:
        continue
while type(place_y) != int:
    try:
        place_y = int(input('Enter size of the place (y): '))
    except ValueError:
        continue
place = [[0 for x in range(place_x)] for y in range(place_y)]
move = ''

def get_new_numbers(matrix: list, repeats: int) -> None:
    count = 0
    while count != repeats:
        x = r.randint(0, 4)
        y = r.randint(0, 4)
        chance = r.randint(1, 10)
        if matrix[y][x] == 0:
            if chance != 10:
                matrix[y][x] = 1
            else:
                matrix[y][x] = 2
            count += 1

def clear() -> None:
    if platform.system() == "Windows":
        os.system('cls')
    else:
        os.system('clear')

def print_place(matrix: list) -> None:
    clear()
    for y in range(len(matrix)):
        for x in range(len(matrix[y])):
            if matrix[y][x] != 0:
                if x < len(matrix[y]) - 1:
                    print(f'[{matrix[y][x]}]', end='')
                else:
                    print(f'[{matrix[y][x]}]')
            else:
                if x < len(matrix[y]) - 1:
                    print(f'[ ]', end='')
                else:
                    print(f'[ ]')

def moving(matrix: list, move: str) -> bool:
    if move == 'u':
        if y > 0 and (matrix[y - 1][x] == 0 or matrix[y - 1][x] == matrix[y][x]):
            return True
        else:
            return False
    elif move == 'r':
        if x < len(matrix[0]) - 1 and (matrix[y][x + 1] == 0 or matrix[y][x + 1] == matrix[y][x]):
            return True
        else:
            return False
    elif move == 'd':
        if y < len(matrix[0]) - 1 and (matrix[y + 1][x] == 0 or matrix[y + 1][x] == matrix[y][x]):
            return True
        else:
            return False
    elif move == 'l':
        if x > 0 and (matrix[y][x - 1] == 0 or matrix[y][x - 1] == matrix[y][x]):
            return True
        else:
            return False
    else:
        return False

def check_win(matrix: list) -> bool:
    for y in range(len(matrix)):
        for x in range(len(matrix[y])):
            if matrix[y][x] == 9:
                return True
    return False

get_new_numbers(place, 2)

while True:
    print_place(place)
    if check_win(place):
            break

    while move.lower() != 'u' and move.lower() != 'd' and move.lower() != 'l' and move.lower() != 'r':
        move = input('Enter your move (u, d, l, r): ')
        if move == 'u':
            for i in range(len(place)):
                for y in range(len(place)):
                    for x in range(len(place[y])):
                        if moving(place, move):
                            if place[y - 1][x] == 0:
                                place[y - 1][x] = place[y][x]
                                place[y][x] = 0
                            elif place[y - 1][x] == place[y][x]:
                                place[y - 1][x] += 1
                                place[y][x] = 0
        elif move == 'r':
            for i in range(len(place[0])):
                for y in range(len(place)):
                    for x in range(len(place[y])):
                        if moving(place, move):
                            if place[y][x + 1] == 0:
                                place[y][x + 1] = place[y][x]
                                place[y][x] = 0
                            elif place[y][x + 1] == place[y][x]:
                                place[y][x + 1] += 1
                                place[y][x] = 0
        elif move == 'd':
            for i in range(len(place)):
                for y in range(len(place)):
                    for x in range(len(place[y])):
                        if moving(place, move):
                            if place[y + 1][x] == 0:
                                place[y + 1][x] = place[y][x]
                                place[y][x] = 0
                            elif place[y + 1][x] == place[y][x]:
                                place[y + 1][x] += 1
                                place[y][x] = 0
        elif move == 'l':
            for i in range(len(place[0])):
                for y in range(len(place)):
                    for x in range(len(place[y])):
                        if moving(place, move):
                            if place[y][x - 1] == 0:
                                place[y][x - 1] = place[y][x]
                                place[y][x] = 0
                            elif place[y][x - 1] == place[y][x]:
                                place[y][x - 1] += 1
                                place[y][x] = 0

        if move.lower() != 'u' and move.lower() != 'd' and move.lower() != 'l' and move.lower() != 'r':
            print('Incorrect move!')
        
        get_new_numbers(place, 1)

    move = ''

if check_win(place):
    print('You win!')