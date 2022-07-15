import pygame
from settings import *


class Paddle(pygame.sprite.Sprite):
    def __init__(self,paddle_index,color,pos):
        self.screen = pygame.display.get_surface()

        # paddle creation
        self.index = paddle_index
        self.image = pygame.Surface((30,150))
        self.image.fill(color)
        self.rect = self.image.get_rect(center = pos)

        # move
        self.direction = pygame.math.Vector2()
        self.speed = 5

    def input(self):
        keys = pygame.key.get_pressed()
        if self.index == 2:
            if keys[pygame.K_UP]:
                self.direction.y = -1
            elif keys[pygame.K_DOWN]:
                self.direction.y = 1
            else:
                self.direction.y = 0
        else:
            if keys[pygame.K_w]:
                self.direction.y = -1
            elif keys[pygame.K_s]:
                self.direction.y = 1
            else:
                self.direction.y = 0

    def move(self):
        self.rect.y += self.direction.y * self.speed

        if self.rect.top <= 0:
            self.rect.top = 0
        if self.rect.bottom >= HEIGHT:
            self.rect.bottom = HEIGHT

    def draw(self):
        self.screen.blit(self.image,self.rect)

    def update(self):
        self.input()
        self.move()
        self.draw()
