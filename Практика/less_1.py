# 1 - Создать класс сняряд
# 2 - Создать прямоугольник по центру экрана 
# 3 - Задать направление движения по оси y
# 4 - если касается края экрана освобождать пямять, тоесть 
# удалять обьект сняряд
# 1.0 Начинаем с шаблона проекта , создаём обьект screen
# создаем игровой цикл обработки событий
# создаём файл controls для управления 

import pygame
import sys 
from bullet import Bullet
import controls

pygame.init()
screen = pygame.display.set_mode((400, 400))
pygame.display.set_caption("Создание сняряда")
color = (255,0,0)
# Создание снаряда
bullet = Bullet(screen)  

print(bullet.y + 200)


while True:
    controls.event(bullet)
    screen.fill((0,0,0))
    controls.update_bullet(screen, color ,bullet)
    # print(bullet.m_space)
    pygame.display.flip()




