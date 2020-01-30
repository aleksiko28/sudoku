import pygame

def solve(board):

    solved = find_empty(board) # returns True when board has no zeros

    if not solved:
        return True
    else:
        coords = row, col = solved
    
    # recursively try solutions and backtrack when invalid
    for i in range(1, 10):
        if is_valid(board, coords, i):
            board[row][col] = i

            if solve(board):
                return True

            board[row][col] = 0

    return False


def is_valid(board, coords, number):
    r = coords[0]
    c = coords[1]
    # checks the row
    for i in range(len(board[0])):
        if board[r][i] == number and c != i:
            return False

    # checks the column
    for i in range(len(board[0])):
        if board[i][c] == number and r != i:
            return False

    # checks the corresponding box
    x = c // 3
    y = r // 3
    for i in range(y*3, y*3 + 3):
        for j in range(x*3, x*3 + 3):
            if board[i][j] == number and (i, j) != coords:
                return False
    return True

def find_empty(board):
    for i in range(len(board)):
        for j in range(len(board[0])):
            if board[i][j] == 0:
                return (i, j)
    return None