import pygame,sys

def event(bullet):
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()

        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                bullet.m_space = True
                # bullet.move()
                print("DOWN")

        elif event.type == pygame.KEYUP:
            if event.key == pygame.K_SPACE:
                bullet.m_space = False
                print("UP")


def update_bullet(screen, color,bullet):
    bullet.draw(screen,color)