import pygame
from settings import *

class Ball(pygame.sprite.Sprite):
    def __init__(self,color):
        self.screen = pygame.display.get_surface()

        self.image = pygame.Surface((30, 30))
        self.image.fill(color)
        self.rect = self.image.get_rect(center = (WIDTH / 2, HEIGHT / 2))

        self.direction = pygame.math.Vector2()
        self.direction.x = 1
        self.direction.y = 1
        self.speed = 5

    def move(self):
        self.rect.x += self.direction.x * self.speed
        self.rect.y += self.direction.y * self.speed

    def draw(self):
        self.screen.blit(self.image,self.rect)



