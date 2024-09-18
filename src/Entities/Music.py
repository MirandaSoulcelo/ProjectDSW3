import pygame

class Music:
    def __init__(self):
        pygame.init()
        pygame.mixer.init()
        self.get_ost()
    def get_ost(self):
        self.music = pygame.mixer.music.load('audio/song.mp3')
        pygame.mixer.music.play(-1)

      