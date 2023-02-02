import pygame 
from sys import exit


pygame.init()
screen = pygame.display.set_mode((800, 400))
pygame.display.set_caption('runnner')
test_surface = pygame.Surface((100, 200))
test_surface.fill('Red')

pos_x = 800 / 2
pos_y = 200 / 2


while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
    screen.blit(test_surface,(pos_x,pos_y))     
    pygame.display.update()        