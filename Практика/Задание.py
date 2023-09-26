import pygame
import sys

from controls import event




pygame.init()
bg_color = (0,0,0)
screen = pygame.display.set_mode((440, 300))
done = False

S = screen.get_rect()#Размер нашего окна
bottom = S.bottom
centerx  = S.centerx

rect = pygame.Rect(0,0,15,30) # left top weight height 
color = 156,100,200
rect.centerx = centerx
rect.bottom = bottom




def event():
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()

    





def event(  ):
    #обработка событий мышь,клава
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()




pygame.draw.rect(screen,color,rect)



while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
    rect.y -= 1 
    pygame.display.flip()