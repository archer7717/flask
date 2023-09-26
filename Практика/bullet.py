import pygame

class Bullet():
    def __init__(self, screen):
        self.size = screen.get_rect() # прямоугольная область
        self.pos_x = self.size.centerx 
        self.pos_y = self.size.bottom -10 
        print(self.x ,self.y )
        self.rect  = pygame.Rect(self.pos_x,self.pos_x, 5, 20)
        self.m_space = False

    def update(self): 
        pass

    def draw(self,screen, color):
        pygame.draw.rect(screen,color, self.rect)
    
    def move(self):
        if self.m_space == True:
            self.y -= 1
            #print(self.y)


