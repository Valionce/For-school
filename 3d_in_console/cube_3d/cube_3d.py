import math
import time

def clear_matrix_3d(matrix: list) -> None:
    for z in range(len(matrix)):
        for y in range(len(matrix[z])):
            for x in range(len(matrix[z][y])):
                matrix[z][y][x] = '  '

class Cube:
    def __init__(self, x1: int, y1: int, z1: int, x2: int, y2: int, z2: int, x_pos: int, y_pos: int, z_pos: int) -> None:
        self.x1 = x1
        self.y1 = y1
        self.z1 = z1
        self.x2 = x2
        self.y2 = y2
        self.z2 = z2
        self.angle_x = 0
        self.angle_y = 0
        self.angle_z = 0
        self.x_pos = x_pos
        self.y_pos = y_pos
        self.z_pos = z_pos

    def get_points(self) -> list:
        points = []
        for x in range(self.x1, self.x2 + 1):
            points.append((x, self.y1, self.z1))
            points.append((x, self.y1, self.z2))
            points.append((x, self.y2, self.z1))
            points.append((x, self.y2, self.z2))
        for y in range(self.y1, self.y2 + 1):
            points.append((self.x1, y, self.z1))
            points.append((self.x1, y, self.z2))
            points.append((self.x2, y, self.z1))
            points.append((self.x2, y, self.z2))
        for z in range(self.z1, self.z2 + 1):
            points.append((self.x1, self.y1, z))
            points.append((self.x1, self.y2, z))
            points.append((self.x2, self.y1, z))
            points.append((self.x2, self.y2, z))
        return points
    
    def rotate(self, x: float, y: float, z: float) -> None:
        self.angle_x += x
        self.angle_y += y
        self.angle_z += z

class Drawer:
    def draw(self, object, matrix: list, symbol: str) -> None:
        points = object.get_points()
        width_x = 60
        height_y = 60
        length_z = 60
        x_pos = object.x_pos
        y_pos = object.y_pos
        z_pos = object.z_pos
        for i in points:
            # Z
            x1 = i[0] * math.cos(object.angle_z) - i[1] * math.sin(object.angle_z)
            y1 = i[0] * math.sin(object.angle_z) + i[1] * math.cos(object.angle_z)
            z1 = i[2]
            # X
            x2 = x1
            y2 = y1 * math.cos(object.angle_x) - z1 * math.sin(object.angle_x)
            z2 = y1 * math.sin(object.angle_x) + z1 * math.cos(object.angle_x)
            # Y
            x3 = x2 * math.cos(object.angle_y) + z2 * math.sin(object.angle_y)
            y3 = y2
            z3 = -x2 * math.sin(object.angle_y) + z2 * math.cos(object.angle_y)

            x = round(x3 + x_pos)
            y = round(y3 + y_pos)
            z = round(z3 + z_pos)

            if 0 <= x < width_x and 0 <= y < height_y and 0 <= z < length_z:
                matrix[z][y][x] = symbol

class Printer:
    def print_3d(self, matrix) -> None:
        width_x = len(matrix[0][0])
        height_y = len(matrix[0])
        length_z = len(matrix)
        output = ''
        for y in range(height_y):
            for x in range(width_x):
                for z in range(length_z):
                    if matrix[z][y][x] == '.':
                        output += '  '
                        break
                    elif matrix[z][y][x] != '  ':
                        output += matrix[z][y][x]
                        break
                else:
                    output += '  '
            output += '\n'
        print(output)

cube1 = Cube(-15, -15, -15, 15, 15, 15, 30, 30, 30)

class Engine:
    def __init__(self) -> None:
        self.printer = Printer()
        self.drawer = Drawer()
        self.objects = [cube1]
        self.matrix = [[['  ' for z in range(60)] for y in range(60)] for z in range(60)]
    
    def run(self) -> None:
        while True:
            clear_matrix_3d(self.matrix)
            for i in self.objects:
                self.drawer.draw(i, self.matrix, '01')
                i.rotate(0.1, 0.1, 0.1)
            self.printer.print_3d(self.matrix)
            time.sleep(0.05)

engine = Engine()
engine.run()
