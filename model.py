import random

def initialize_board():
    _board ={}

    for x in range(25):
        for y in range(25):
            _board[(x,y)] = None
    return _board

def initialize_snake(_board):
    _snake = [(random.randint(8,12), random.randint(8,12))] # miedzy 8 a 12 posrodku wystartuje snake
    #  print(_snake[0])
    _board[_snake[0]] = "Snakehead"
    return _snake

def initialize_apple(_board):
    apple = (random.randint(0,19), random.randint(0,19))  # jablko pojawi sie  losowo miedzy 0 a 19
    while _board[apple] is not None:
        apple = (random.randint(0, 19), random.randint(0, 19))  # jablko pojawi sie  losowo miedzy 0 a 19
    _board[apple]= "Apple"
    return apple

def set_new_position(direction, snake, board):
    head_x, head_y = snake[0]
    board[(head_x, head_y)] = None

    if direction == 0: # w gore
        head_y = head_y - 1
    if direction == 1: # w prawo
        head_x = head_x + 1
    if direction == 2: # w dol
        head_y = head_y + 1
    if direction == 3: # w lewo
        head_x = head_x - 1

    board[(head_x, head_y)] = "Snakehead"
    snake[0] = (head_x, head_y)

def eat_apple(board, snake, apple):
    if snake[0] == apple:
        return initialize_apple(board)
    return apple