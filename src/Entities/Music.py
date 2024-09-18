import pygame
import time

class Music:
    def __init__(self):

        pygame.mixer.init()
        self.get_ost()
        

    def get_ost(self):
        pygame.mixer.music.load('audio/song.mp3')
        pygame.mixer.music.play(-1)

    def get_ending(self):
        time.sleep(0.1)
        
        pygame.mixer.music.load('audio/sonic.mp3')
        pygame.mixer.music.play(-1)


      