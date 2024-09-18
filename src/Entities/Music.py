import pygame
import time

class Music:
    def __init__(self):
        pygame.init()
        pygame.mixer.init()
        

    def get_ost(self):
        pygame.mixer.music.load('audio/song.mp3')
        pygame.mixer.music.play(-1)

    def get_ending(self):
        time.sleep(0.1)
        pygame.mixer.music.stop()
        
        pygame.mixer.music.load('audio/sonic.mp3')
        pygame.mixer.music.set_volume(1.0)
        pygame.mixer.music.play(-1)


      