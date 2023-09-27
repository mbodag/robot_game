import pygame
from constants import *

class RobotSprite(pygame.sprite.Sprite):
    def __init__(self, x, y, color):
        pygame.sprite.Sprite.__init__(self) 
        self.normal_image = pygame.Surface((20,20))
        self.normal_image.fill(color)
        
        self.x = x
        self.y = y
        self.selected = False
        self.click_image = pygame.Surface((30,30))
        click_image_color = (max(color[0] - 40,0), max(color[1] - 40,0), max(color[2] - 40,0))
        self.click_image.fill(click_image_color)
        self.image = self.normal_image
        self.rect = self.image.get_rect(center = (x,y))

    def update(self):
        self.image = self.click_image if self.selected else self.normal_image
        self.rect = self.image.get_rect()
        self.rect.center = (self.x,self.y)
        

    #def update(self, event_list):
        # for event in event_list:
        #     if event.type == pygame.MOUSEBUTTONDOWN:
        #         if self.rect.collidepoint(event.pos):
        #             self.selected = not self.selected
        
        #self.image = self.click_image if self.selected else self.original_image

class Target(pygame.sprite.Sprite):
    def __init__(self, x, y, color):
        pygame.sprite.Sprite.__init__(self) 
        self.image = pygame.Surface((40,40))
        self.image.fill(WHITE)
        pygame.draw.circle(self.image, color, (20,20), 15)
        self.x = x
        self.y = y
        self.rect = self.image.get_rect(center = (x,y))
