# Libraries
import os
import platform

# Variables
board = [
    ['r', 'n', 'b', 'q', 'k', 'b', 'n', 'r'],
    ['p', 'p', 'p', 'p', 'p', 'p', 'p', 'p'],
    ['.', '.', '.', '.', '.', '.', '.', '.'],
    ['.', '.', '.', '.', '.', '.', '.', '.'],
    ['.', '.', '.', '.', '.', '.', '.', '.'],
    ['.', '.', '.', '.', '.', '.', '.', '.'],
    ['P', 'P', 'P', 'P', 'P', 'P', 'P', 'P'],
    ['R', 'N', 'B', 'Q', 'K', 'B', 'N', 'R']
]
player = 1
promotion = ''
passage = ''
white_oo = True
white_ooo = True
black_oo = True
black_ooo = True
white_check = False
black_check = False

# Constants
KING = 'K'
QUEEN = 'Q'
ROOK = 'R'
KNIGHT = 'N'
BISHOP = 'B'
PAWN = 'P'
king = 'k'
queen = 'q'
rook = 'r'
knight = 'n'
bishop = 'b'
pawn = 'p'
empty = '.'

# Functions
def clear() -> None:
    if platform.system() == 'Windows':
        os.system('cls')
    else:
        os.system('clear')

def print_board(matrix: list) -> None: # Print of the board
    clear()
    for y in range(len(matrix)):
        for x in range(len(matrix[0])):
            if x == 0:
                if matrix[y][x] != empty:
                    print(f'{8 - y} [{matrix[y][x]}]', end='')
                else:
                    print(f'{8 - y} [ ]', end='')
            elif x < len(matrix[0]) - 1:
                if matrix[y][x] != empty:
                    print(f'[{matrix[y][x]}]', end='')
                else:
                    print(f'[ ]', end='')
            else:
                if matrix[y][x] != empty:
                    print(f'[{matrix[y][x]}]')
                else:
                    print(f'[ ]')
    print('   a  b  c  d  e  f  g  h')
    print(f'Очередь игрока: {player}')

def abc(move: str) -> int: # Letters to numbers
    if move[0] == 'a':
        return 0
    elif move[0] == 'b':
        return 1
    elif move[0] == 'c':
        return 2
    elif move[0] == 'd':
        return 3
    elif move[0] == 'e':
        return 4
    elif move[0] == 'f':
        return 5
    elif move[0] == 'g':
        return 6
    elif move[0] == 'h':
        return 7
    else:
        return -1

def piece_move(pos1: str, pos2: str, matrix: list) -> None:
    matrix[8 - int(pos2[1])][abc(pos2)] = matrix[8 - int(pos1[1])][abc(pos1)]
    matrix[8 - int(pos1[1])][abc(pos1)] = empty

def piece_set(pos: str, matrix: list, piece: str) -> None:
    matrix[8 - int(pos[1])][abc(pos)] = piece

def rook_path(pos1: str, pos2: str, matrix: list) -> bool: # Rook's path
    x1 = abc(pos1)
    y1 = 8 - int(pos1[1])
    x2 = abc(pos2)
    y2 = 8 - int(pos2[1])
    
    if x1 == x2:
        if y2 > y1:
            step = 1
        else:
            step = -1
        for y in range(y1 + step, y2, step):
            if matrix[y][x1] != empty:
                return False
    elif y1 == y2:
        if x2 > x1:
            step = 1
        else:
            step = -1
        for x in range(x1 + step, x2, step):
            if matrix[y1][x] != empty:
                return False
    else:
        return False
    
    return True

def bishop_path(pos1: str, pos2: str, matrix: list) -> bool: # Bishop's path
    x1 = abc(pos1)
    y1 = 8 - int(pos1[1])
    x2 = abc(pos2)
    y2 = 8 - int(pos2[1])

    if abs(x1 - x2) != abs(y1 - y2):
        return False

    if x2 > x1:
        step_x = 1
    else:
        step_x = -1
    if y2 > y1:
        step_y = 1
    else:
        step_y = -1

    x = x1 + step_x
    y = y1 + step_y

    while x != x2 and y != y2:
        if matrix[y][x] != empty:
            return False
        x += step_x
        y += step_y

    return True

def king_move(pos1: str, pos2: str) -> bool: # King's logic
    if abs(abc(pos1) - abc(pos2)) > 1 and ((player == 1 and (white_oo == True or white_ooo == True)) or (player == 2 and black_oo == True or black_ooo == True)):
        return True
    elif abs(int(pos1[1]) - int(pos2[1])) <= 1 and abs(abc(pos1) - abc(pos2)) <= 1:
        return True
    else:
        return False

def rook_move(pos1: str, pos2: str) -> bool: # Rook's logic
    if abc(pos1) == abc(pos2) or int(pos1[1]) == int(pos2[1]):
        return True
    else:
        return False

def knight_move(pos1: str, pos2: str) -> bool: # Knight's logic
    if (abs(abc(pos1) - abc(pos2)) == 2 and abs(int(pos1[1]) - int(pos2[1])) == 1) or (abs(abc(pos1) - abc(pos2)) == 1 and abs(int(pos1[1]) - int(pos2[1])) == 2):
        return True
    else:
        return False

def bishop_move(pos1: str, pos2: str) -> bool: # Bishop's logic
    if abs(abc(pos1) - abc(pos2)) == abs(int(pos1[1]) - int(pos2[1])):
        return True
    else:
        return False

def queen_move(pos1: str, pos2: str) -> bool: # Queen's logic
    if rook_move(pos1, pos2) or bishop_move(pos1, pos2):
        return True
    else:
        return False

def pawn_move(pos1: str, pos2: str, matrix: list) -> bool: # Pawn's logic
    if abc(pos1) == abc(pos2): # Default move
        if player == 1:
            if (int(pos2[1]) - int(pos1[1]) == 1 or (int(pos1[1]) == 2 and 3 <= int(pos2[1]) <= 4 and matrix[9 - int(pos2[1])][abc(pos2)] == empty)) and matrix[8 - int(pos2[1])][abc(pos2)] == empty:
                return True
            else:
                return False
        elif player == 2:
            if (int(pos1[1]) - int(pos2[1]) == 1 or (int(pos1[1]) == 7 and 5 <= int(pos2[1]) <= 6 and matrix[7 - int(pos2[1])][abc(pos2)] == empty)) and matrix[8 - int(pos2[1])][abc(pos2)] == empty:
                return True
            else:
                return False
    elif abs(abc(pos1) - abc(pos2)) == 1: # Pawn takes
        if player == 1:
            if (int(pos2[1]) - int(pos1[1]) == 1) and matrix[8 - int(pos2[1])][abc(pos2)] != empty:
                return True
            elif int(pos1[1]) == int(passage[1]) and abs(int(pos2[1]) - int(passage[1])) == 1 and abc(pos2) == abc(passage):
                board[8 - int(passage[1])][abc(passage)] = empty
                return True
            else:
                return False
        elif player == 2:
            if (int(pos1[1]) - int(pos2[1]) == 1) and matrix[8 - int(pos2[1])][abc(pos2)] != empty:
                return True
            elif int(pos1[1]) == int(passage[1]) and abs(int(pos2[1]) - int(passage[1])) == 1 and abc(pos2) == abc(passage):
                board[8 - int(passage[1])][abc(passage)] = empty
                return True
            else:
                return False
    else:
        return False

def move_check(move: str) -> bool: # Legality check
    if len(move) == 2 and move[0].isalpha() and move[1].isdigit() and 0 <= abc(move) <= 7 and 1 <= int(move[1]) <= 8:
        return True
    else:
        return False

def check_win(matrix: list) -> int: # Win check
    white_exists = False
    black_exists = False
    for y in range(len(matrix)):
        for x in range(len(matrix[0])):
            if matrix[y][x] == KING:
                white_exists = True
            elif matrix[y][x] == king:
                black_exists = True
    if white_exists == black_exists == True:
        return 0
    elif white_exists == False:
        return 2
    elif black_exists == False:
        return 1



# Game
while check_win(board) == 0:
    promotion = ''
    print_board(board)
    pos1 = input('From: ')
    pos2 = input('To: ')
    if move_check(pos1) and move_check(pos2) and pos1 != pos2 and board[8 - int(pos1[1])][abc(pos1)] != empty:
        if (player == 1 and board[8 - int(pos1[1])][abc(pos1)].isupper()) or (player == 2 and board[8 - int(pos1[1])][abc(pos1)].islower()): # Can't move opponent's pieces
            if (player == 1 and board[8 - int(pos2[1])][abc(pos2)].islower()) or (player == 2 and board[8 - int(pos2[1])][abc(pos2)].isupper()) or board[8 - int(pos2[1])][abc(pos2)] == empty: # Can't take your own pieces
                
                if board[8 - int(pos1[1])][abc(pos1)].lower() == king and king_move(pos1, pos2): # King's moves
                    if abs(abc(pos1) - abc(pos2)) > 1:
                        if player == 1:
                            if abc(pos2) < abc(pos1) and white_ooo == True and board[7][1] == empty and board[7][2] == empty and board[7][3] == empty:
                                board[7][2] = KING
                                board[7][3] = ROOK
                                board[7][4] = empty
                                board[7][0] = empty
                            elif abc(pos1) < abc(pos2) and white_oo == True and board[7][5] == empty and board[7][6] == empty:
                                board[7][6] = KING
                                board[7][5] = ROOK
                                board[7][4] = empty
                                board[7][7] = empty
                            white_oo = False
                            white_ooo = False
                        elif player == 2:
                            if abc(pos2) < abc(pos1) and black_ooo == True and board[0][1] == empty and board[0][2] == empty and board[0][3] == empty:
                                board[0][2] = king
                                board[0][3] = rook
                                board[0][4] = empty
                                board[0][0] = empty
                            elif abc(pos1) < abc(pos2) and black_oo == True and board[0][5] == empty and board[0][6] == empty:
                                board[0][6] = king
                                board[0][5] = rook
                                board[0][4] = empty
                                board[0][7] = empty
                            black_oo = False
                            black_ooo = False
                    else:
                        piece_move(pos1, pos2, board)
                    
                    if player == 1:
                        white_oo = False
                        white_ooo = False
                    elif player == 2:
                        black_oo = False
                        black_ooo = False
                    player = 3 - player

                elif board[8 - int(pos1[1])][abc(pos1)].lower() == rook and rook_move(pos1, pos2) and rook_path(pos1, pos2, board): # Rook's moves
                    if player == 1 and pos1 == 'a1':
                        white_ooo = False
                    elif player == 1 and pos1 == 'h1':
                        white_oo = False
                    elif player == 2 and pos1 == 'a8':
                        black_ooo = False
                    elif player == 2 and pos1 == 'h8':
                        black_oo = False
                    piece_move(pos1, pos2, board)
                    player = 3 - player
                
                elif board[8 - int(pos1[1])][abc(pos1)].lower() == knight and knight_move(pos1, pos2): # Knight's moves
                    piece_move(pos1, pos2, board)
                    player = 3 - player
                
                elif board[8 - int(pos1[1])][abc(pos1)].lower() == bishop and bishop_move(pos1, pos2) and bishop_path(pos1, pos2, board): # Bishop's moves
                    piece_move(pos1, pos2, board)
                    player = 3 - player
                
                elif board[8 - int(pos1[1])][abc(pos1)].lower() == queen and queen_move(pos1, pos2): # Queen's moves
                    if (((abc(pos1) == abc(pos2) or 8 - int(pos1[1]) == 8 - int(pos2[1]))) and rook_path(pos1, pos2, board)) or (abs(abc(pos1) - abc(pos2)) == abs(int(pos1[1]) - int(pos2[1])) and bishop_path(pos1, pos2, board)):
                        piece_move(pos1, pos2, board)
                        player = 3 - player
                
                elif board[8 - int(pos1[1])][abc(pos1)].lower() == pawn and pawn_move(pos1, pos2, board): # Pawn's moves
                    piece_move(pos1, pos2, board)
                    
                    # Pawn Promotions
                    if player == 1 and int(pos2[1]) == 8:
                        while promotion.lower() != rook and promotion.lower() != knight and promotion.lower() != bishop and promotion.lower() != queen:
                            promotion = input('Select a piece to promote (r, n, b, q): ')
                            if promotion.lower() != rook and promotion.lower() != knight and promotion.lower() != bishop and promotion.lower() != queen:
                                print('Impossible move!')
                        piece_set(pos2, board, promotion.upper())
                    if player == 2 and int(pos2[1]) == 1:
                        while promotion.lower() != rook and promotion.lower() != knight and promotion.lower() != bishop and promotion.lower() != queen:
                            promotion = input('Select a piece to promote (r, n, b, q): ')
                            if promotion.lower() != rook and promotion.lower() != knight and promotion.lower() != bishop and promotion.lower() != queen:
                                print('Impossible move!')
                        piece_set(pos2, board, promotion.lower())
                    
                    if passage != '':
                        passage = ''
                    if (player == 1 and int(pos1[1]) == 2 and int(pos2[1]) == 4) or (player == 2 and int(pos1[1]) == 7 and int(pos2[1]) == 5):
                        passage = pos2
                    
                    player = 3 - player
    else:
        continue
    
    if check_win(board) == 1:
        print('White wins!')
        break
    elif check_win(board) == 2:
        print('Black wins!')
        break