import random as r
import os
import platform

EMPTY_CLOSED = '000'
EMPTY_OPENED = '010'
BOMB_CLOSED = '-00'
BOMB_OPENED = '-10'

class Place:
    def __init__(self, x_size: int, y_size: int, bombs_amount: int):
        self._place = [[EMPTY_CLOSED for x in range(x_size)] for y in range(y_size)]
        self.x_size = x_size
        self.y_size = y_size
        self.bombs_amount = bombs_amount
        self.lose = False
    
    def get_cell(self, x: int, y: int) -> str:
        return self._place[y][x]
    
    def is_closed(self, x: int, y: int) -> bool:
        return self.get_cell(x, y)[1] == '0'
    
    def is_pinned(self, x: int, y: int) -> bool:
        return self.get_cell(x, y)[2] != '0'
    
    def is_bomb(self, x: int, y: int) -> bool:
        return self.get_cell(x, y)[0] == '-'
    
    def is_fully_safe(self, x: int, y: int) -> bool:
        return self.get_cell(x, y)[0] == '0'
    
    def open_cell(self, x: int, y: int) -> None:
        if self.is_bomb(x, y):
            self._place[y][x] = BOMB_OPENED
            self.lose = True
        elif self.is_fully_safe(x, y):
            self._place[y][x] = EMPTY_OPENED
            self.fill(x, y)
        else:
            self._place[y][x] = f'{self.get_cell(x, y)[0]}10'
    
    def pin_cell(self, x: int, y: int) -> None:
        if self._place[y][x][2] == '0':
            self._place[y][x] = f'{self._place[y][x][:-1]}1'
        else:
            self._place[y][x] = f'{self._place[y][x][:-1]}0'

    def fill(self, x: int, y: int) -> None:
        self._place[y][x] = EMPTY_OPENED
        for dy in [-1, 0, 1]:
            for dx in [-1, 0, 1]:
                if not 0 <= x + dx < self.x_size or not 0 <= y + dy < self.y_size or dx == dy == 0 or not self.is_closed(x + dx, y + dy):
                    continue
                if not self.is_pinned(x + dx, y + dy):
                    if not self.is_fully_safe(x + dx, y + dy):
                        self.open_cell(x + dx, y + dy)
                    else:
                        self.fill(x + dx, y + dy)

    def check_end(self) -> bool:
        count = 0
        for y in range(self.y_size):
            for x in range(self.x_size):
                if not self.is_closed(x, y) and not self.is_bomb(x, y):
                    count += 1
        return count == self.x_size * self.y_size - self.bombs_amount, self.lose

    def generate_place(self, forbidden_x: int, forbidden_y: int) -> None:
        coordinates = set()
        while len(coordinates) < self.bombs_amount:
            x = r.randint(0, self.x_size - 1)
            y = r.randint(0, self.y_size - 1)
            if (x, y) != (forbidden_x, forbidden_y):
                coordinates.add((x, y))
        for x, y in coordinates:
            self._place[y][x] = BOMB_CLOSED
            for dy in [-1, 0, 1]:
                for dx in [-1, 0, 1]:
                    if not 0 <= x + dx < self.x_size or not 0 <= y + dy < self.y_size or dx == dy == 0 or self.is_bomb(x + dx, y + dy):
                        continue
                    self._place[y + dy][x + dx] = f'{int(self.get_cell(x + dx, y + dy)[0]) + 1}00'

class Printer:
    def clear(self) -> None:
        if platform.system() == 'Windows':
            os.system('cls')
        else:
            os.system('clear')
    
    def print_place(self, place: Place) -> None:
        self.clear()
        output = ''
        # print('    1  2  3  4  5  6  7  8  9 10')
        print('   ' + f' {' '.join([f'{x:<2}' for x in range(1, place.x_size + 1)])}')
        for y in range(place.y_size):
            output += f'{y + 1:<2} '
            for x in range(place.x_size):
                if place.is_pinned(x, y):
                    output += '[|]'
                elif place.is_closed(x, y):
                    output += '[#]'
                else:
                    if place.is_bomb(x, y):
                        output += '[X]'
                    else:
                        if place.is_fully_safe(x, y):
                            output += '[ ]'
                        else:
                            output += f'[{place.get_cell(x, y)[0]}]'
            output += '\n'
        print(output)

class Player:
    def make_move(self, x: int, y: int, pinned: int, place: Place) -> None:
        if pinned and place.is_closed(x, y):
            place.pin_cell(x, y)
        if not place.is_pinned(x, y) and place.is_closed(x, y) and not pinned:
            place.open_cell(x, y)

class Engine:
    def __init__(self):
        self.place = Place(10, 10, 10)
        self.printer = Printer()
        self.player = Player()

    def run(self):
        x_move = ''
        y_move = ''
        pin = ''
        self.printer.print_place(self.place)
        while type(x_move) != int and type(y_move) != int and type(pin) != int:
            try:
                x_move, y_move, pin = map(int, input('Enter your move (x, y, pinned): ').split())
                if type(x_move) == int and 0 <= x_move < self.place.x_size or type(y_move) == int and 0 <= y_move < self.place.y_size:
                    continue
            except ValueError:
                continue
        self.place.generate_place(x_move - 1, y_move - 1)
        self.player.make_move(x_move - 1, y_move - 1, pin, self.place)
        while True:
            try:
                self.printer.print_place(self.place)
                x_move, y_move, pin = map(int, input().split())
                self.player.make_move(x_move - 1, y_move - 1, pin, self.place)
                win, lose = self.place.check_end()
                if win or lose:
                    break
            except (ValueError, IndexError):
                continue
        self.printer.print_place(self.place)
        if win:
            print('You win!')
        if lose:
            print('You lose!')

engine = Engine()
engine.run()