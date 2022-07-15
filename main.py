import pygame
from sys import exit
import PySimpleGUI as sg
from settings import *
from level import Level


class Game:
    def __init__(self):

        # main setup
        pygame.init()
        self.screen = pygame.display.set_mode((WIDTH, HEIGHT))
        pygame.display.set_caption('Pong')
        self.clock = pygame.time.Clock()

        self.level = Level()

    def run(self):
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    exit()

            self.screen.fill('black')
            self.level.run()
            pygame.display.update()
            self.clock.tick(FPS)

def info():
    layout = [
        [sg.Text('Start/Stop bot: TAB ')],
        [sg.Text('Move right paddle: UP and DOWN arrows')],
        [sg.Frame('If bot is off',[[sg.Text('Move left paddle: W and S')]])],
        [sg.Push(),sg.Button('PLAY'),sg.Push()]
    ]

    window = sg.Window('Binds',layout)

    while True:
        event, values = window.read()

        if event in (sg.WIN_CLOSED, 'PLAY'):
            break

    window.close()

if __name__ == '__main__':
    game = Game()
    info()
    game.run()


