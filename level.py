import pygame
from settings import *
from paddle import Paddle
from ball import Ball
from bot import Bot


class Level:
    def __init__(self):
        pygame.font.init()
        self.screen = pygame.display.get_surface()
        self.startgame = False

        self.paddle1 = Paddle(1,'white',(WIDTH / 40,HEIGHT / 2))
        self.paddle2 = Paddle(2,'white',(WIDTH - (WIDTH / 40),HEIGHT / 2))

        self.ball = Ball('white')

        self.bot = Bot(self.ball,self.paddle1,self.paddle2)
        self.bot_index = 1
        self.bot_status = 'ON'
        self.can_start_bot = True
        self.push_time = None
        self.push_cooldown = 400

        self.score1 = 0
        self.score2 = 0

    def collision(self):
        # ball bounce
        if self.ball.rect.y >= HEIGHT:
            self.ball.direction.y = -1
        elif self.ball.rect.y <= 0:
            self.ball.direction.y = 1
        if self.ball.rect.colliderect(self.paddle1):
            self.ball.direction.x = 1
        elif self.ball.rect.colliderect(self.paddle2):
            self.ball.direction.x = -1

        # ball score
        if self.ball.rect.x >= WIDTH:
            self.ball.rect.center = (WIDTH / 2, HEIGHT / 2)
            self.ball.direction.x = -1

            self.score1 += 1

        elif self.ball.rect.x <= 0:
            self.ball.rect.center = (WIDTH / 2, HEIGHT / 2)
            self.ball.direction.x = 1

            self.score2 += 1

    def start_game(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_SPACE]:
            self.startgame = True

    def show_text(self):
        font = pygame.font.Font('font.ttf', 50)
        score_font = pygame.font.Font('font.ttf', 100)
        bot_font = pygame.font.Font('font.ttf', 25)

        start_txt = font.render('Press Space To Play', False, (225,225,225))
        start_txt_rect = start_txt.get_rect(midtop = (WIDTH / 2, HEIGHT - (HEIGHT * 0.7)))

        score_txt = score_font.render(f'{self.score1} : {self.score2}', False, (225,225,225))
        score_txt_rect = score_txt.get_rect(midtop = (WIDTH / 2,HEIGHT - (HEIGHT * 0.9)))

        bot_txt = bot_font.render('Press TAB to run/stop Bot', False, (225,225,225))
        bot_txt_rect = bot_txt.get_rect(midbottom=(WIDTH / 2, HEIGHT - (HEIGHT * 0.93)))

        boton_txt = bot_font.render(f'Bot is {self.bot_status}', False, (225, 225, 225))
        boton_txt_rect = boton_txt.get_rect(midbottom=(WIDTH * 0.1, HEIGHT - (HEIGHT * 0.93)))

        if not self.startgame:
            self.screen.blit(start_txt,start_txt_rect)



        self.screen.blit(score_txt,score_txt_rect)
        self.screen.blit(bot_txt,bot_txt_rect)
        self.screen.blit(boton_txt,boton_txt_rect)

    def turn_on_bot(self):
        keys =pygame.key.get_pressed()
        if keys[pygame.K_TAB] and self.can_start_bot:
            self.can_start_bot = False
            self.push_time = pygame.time.get_ticks()
            self.bot_index += 1

        if self.bot_index == 1:
            self.bot.run()
            self.bot_status = 'ON'
        elif self.bot_index == 0:
            self.bot_status = 'OFF'

        #cooldown
        current_time = pygame.time.get_ticks()
        if not self.can_start_bot:
            if current_time - self.push_time >= self.push_cooldown:
                self.can_start_bot = True

        if self.bot_index >= 2:
            self.bot_index = 0

    def run(self):
        self.paddle1.update()
        self.paddle2.update()
        if self.startgame:
            self.ball.move()
        self.ball.draw()
        self.collision()
        self.start_game()
        self.show_text()
        self.turn_on_bot()


