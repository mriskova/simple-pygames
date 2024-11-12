import pygame

width = 20
height = 20
margin = 5
size = 20

pygame.init()
display = pygame.display.set_mode((size*(height+margin)+margin,size*(width+margin)+margin))
screen = pygame.Surface(display.get_size())
white        = (255,255,255)
light_yellow = (255,255,102)
light_pink   = (255,182,193)
red          = (255,  0,  0)
orange       = (255,140,  0)
green        = (0  ,255,  0)
purple       = (148,  0,211)
blue         = (0  ,  0,255)
black        = (0  ,  0,  0)
border_width = 2
COLORS = [white, light_yellow, orange, green, blue, purple, light_pink, red,  black] 

grid = [[0 for x in range(size)] for y in range(size)]
clock = pygame.time.Clock()

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYUP:
            if event.key == pygame.K_q:
                running = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            x = event.pos[1] // (width+margin)
            y = event.pos[0] // (height+margin)
            grid[x][y] = (grid[x][y] + 1) % len(COLORS)       
    for column in range(size):
        for row in range(size):
            pygame.draw.rect(screen, 
                             COLORS[grid[row][column]], 
                             (margin+column*(width+margin), margin+row*(height+margin),width,height))
    display.blit(screen, (0, 0))
    clock.tick(60)    
    pygame.display.update()
pygame.quit()
exit()