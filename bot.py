import pygame

class Bot:
    def __init__(self,ball,paddle1,paddle2):
        self.ball = ball
        self.paddle1 = paddle1
        self.paddle2 = paddle2

    def run(self):
        if self.ball.direction.x == -1:
            self.paddle1.rect.centery = self.ball.rect.centery
