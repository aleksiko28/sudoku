import sys, pygame

pygame.init()
pygame.display.set_caption('Sudoku')

size = width, height = 1500, 1500
white = 255, 255, 255
grey = 160, 160, 160
black = 0, 0, 0
blue = 51, 224, 255
red = 219, 37, 104
b_width, b_height = 3, 3
board_size = b_height * b_width
box_width = width // b_width // 3
box_height = height // b_height // 3

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
            pygame.time.delay(100)
            draw_numbers(board)
            draw_change(col, row, True)
            pygame.display.update()

            if solve(board):
                return True

            board[row][col] = 0
            draw_change(col, row, False)
            pygame.display.update()

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

# example board data
board = [
    [7,8,0,4,0,0,1,2,0],
    [6,0,0,0,7,5,0,0,9],
    [0,0,0,6,0,1,0,7,8],
    [0,0,7,0,4,0,2,6,0],
    [0,0,1,0,5,0,9,3,0],
    [9,0,4,0,6,0,0,0,5],
    [0,7,0,3,0,0,0,1,2],
    [1,2,0,0,0,7,4,0,0],
    [0,4,9,2,0,6,0,0,7]
]

# screen to draw everything on
screen = pygame.display.set_mode(size)
screen.fill(white)

myfont = pygame.font.SysFont("monospace", int(width / 10))

def draw_grid():

    # create grid from rectangles
    for x in range(2, width, box_width):
        for y in range(2, height, box_height):
            rect = pygame.Rect(x, y, width / b_width, height / b_height)
            pygame.draw.rect(screen, grey, rect, 3)

    # draw strong lines
    for x in range(0, width, width // b_width):
        for y in range(0, height, height // b_height):
            if x > y:
                pygame.draw.line(screen, black, (x,y), (x, y+height), 7)
            elif y > x:
                pygame.draw.line(screen, black, (x,y), (x+width, y), 7)


# draws changes to board as solver solves it
def draw_change(col, row, new):

    spacing = width / board_size
    x = spacing * col + 5
    y = spacing * row + 5

    # if new number, clear box and draw blue rectangle
    if new:
        pygame.draw.rect(screen, white, (x, y, spacing - width / 50, spacing - height / 50), 0)
        pygame.draw.rect(screen, blue, (x, y, spacing, spacing), 5)
        
    # if wrong number, clear box and draw red rectangle
    else:
        pygame.draw.rect(screen, white, (x, y, spacing - width / 50, spacing - height / 50), 0)
        pygame.draw.rect(screen, red, (x, y, spacing, spacing), 5)
        label = myfont.render("0", 1, black)
        screen.blit(label, (x + box_width / 4 + width/80, y + box_height / 4))

        
def draw_numbers(board):

    # draws numbers to screen that aren't 0 in board
    for x in range(b_width*3):
        for y in range(b_height*3):
            number = str(board[y][x])
            if number != "0":
                label = myfont.render(number, 1, black)
                # draw numbers in the middle of the box by offsetting
                screen.blit(label, (x*box_width + box_width / 4 + width/80, y*box_height + box_height / 4))


# game loop
while 1:
    for event in pygame.event.get():
        if event.type == pygame.QUIT: 
            sys.exit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_s: # press S to solve
                solve(board)
                screen.fill(white)
                draw_grid()
                draw_numbers(board)
            if event.key == pygame.K_ESCAPE: # escape to exit
                sys.exit()
    
    draw_grid()
    draw_numbers(board)
    pygame.display.update()

