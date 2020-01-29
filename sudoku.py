import sys, pygame
pygame.init()

size = width, height = 960, 960
speed = [2, 2]
white = 255, 255, 255
black = 0, 0, 0
boardsize = bwidth, bheight = 3, 3

#example board data
board = [
    [3,8,0,4,0,0,1,2,0],
    [6,0,0,0,7,5,0,0,9],
    [0,0,0,6,0,1,0,7,8],
    [0,0,7,0,4,0,2,6,0],
    [0,0,1,0,5,0,9,3,0],
    [9,0,4,0,6,0,0,0,5],
    [0,7,0,3,0,0,0,1,2],
    [1,2,0,0,0,7,4,0,0],
    [0,4,3,2,0,6,0,0,7]
]

#screen to draw everything on
screen = pygame.display.set_mode(size)
screen.fill(white)

#create grid from rectangles
for x in range(0, width, int(width/(bwidth*3))):
    for y in range(0, height, int(height/(bheight*3))):
        rect = pygame.Rect(x, y, width / bwidth, height / bheight)
        pygame.draw.rect(screen, black, rect, 1)

#draw strong lines
for x in range(0, width, int(width/bwidth)):
    for y in range(0, height, int(height/bheight)):
        if x > y:
            pygame.draw.line(screen, black, (x,y), (x, y+height), 5)
        elif y > x:
            pygame.draw.line(screen, black, (x,y), (x+width, y), 5)

#game loop
while 1:
    for event in pygame.event.get():
        if event.type == pygame.QUIT: sys.exit()

    pygame.display.flip()