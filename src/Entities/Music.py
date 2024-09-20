import pygame
import time

class Music:
    def __init__(self):

        pygame.mixer.init()
        self.get_ost()
        

    def get_ost(self):
        pygame.mixer.music.load('audio/song.mp3')
        pygame.mixer.music.set_volume(2.5)
        pygame.mixer.music.play(-1)

    def get_ending(self):
        
        pygame.mixer.music.load('audio/sonic.mp3')
        pygame.mixer.music.set_volume(0.5)
        pygame.mixer.music.play(-1)


      