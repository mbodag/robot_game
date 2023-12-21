import pygame
from constants import *


pygame.init()

screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Sprite Groups")

clock = pygame.time.Clock()
FPS = 20

class Square(pygame.sprite.Sprite):
    def __init__(self, col, x,y) -> None:
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface((10,10))
        self.image.fill(col)
        self.rect = self.image.get_rect()
        self.rect.center = (x,y)
    def update(self):
        x = self.rect.center[0]
        y = self.rect.center[1]
        self.rect.center = (x+1, y)

squares = pygame.sprite.Group()



run = True
while run:
    clock.tick(FPS)

    screen.fill('cyan')
    squares.update()

    squares.draw(screen)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            pos = pygame.mouse.get_pos()
            square = Square(WHITE, pos[0], pos[1])
            squares.add((square))


        pygame.display.flip()
pygame.quit()


