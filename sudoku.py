import sys, pygame
from solver import solve, is_valid, find_empty
#from solvetest import solve, valid, find_empty

pygame.init()
pygame.display.set_caption('Sudoku')

size = width, height = 1500, 1500
speed = [2, 2]
white = 255, 255, 255
grey = 128, 128, 128
black = 0, 0, 0
board_size = b_width, b_height = 3, 3
box_width = width // b_width // 3
box_height = height // b_height // 3

#example board data
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

#screen to draw everything on
screen = pygame.display.set_mode(size)
screen.fill(white)

myfont = pygame.font.SysFont("monospace", int(width / 10))

# create grid from rectangles
for x in range(2, width, box_width):
    for y in range(2, height, box_height):
        rect = pygame.Rect(x, y, width / b_width, height / b_height)
        pygame.draw.rect(screen, grey, rect, 3)

# draw strong lines
for x in range(0, width, int(width/b_width)):
    for y in range(0, height, int(height/b_height)):
        if x > y:
            pygame.draw.line(screen, black, (x,y), (x, y+height), 7)
        elif y > x:
            pygame.draw.line(screen, black, (x,y), (x+width, y), 7)


# game loop
while 1:
    for event in pygame.event.get():
        if event.type == pygame.QUIT: 
            sys.exit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_s: # press S to solve
                solve(board)
            if event.key == pygame.K_ESCAPE:
                sys.exit()
            
    
    # draws numbers to screen that aren't 0 in board
    for x in range(b_width*3):
        for y in range(b_height*3):
            number = str(board[y][x])
            if number != "0":
                label = myfont.render(number, 1, black)
                # draw numbers in the middle of the box by offsetting
                screen.blit(label, (x*box_width + box_width / 4 + width/80, y*box_height + box_height / 4))

    pygame.display.update()