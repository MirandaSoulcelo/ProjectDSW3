import pygame
from random import randint

class Enemie:
    def __init__(self):
        self.enemie_surface()
        self.timer()
        self.obstacle_rect_list = []
        self.min_distance = 300  # Ajuste conforme necessário

    def enemie_surface(self):
        self.enemie_surf = pygame.image.load('graphics/shadow1.png').convert_alpha()

    def get_surface(self):
        return self.enemie_surf

    def timer(self):
        self.obstacle_timer = pygame.USEREVENT + 1
        pygame.time.set_timer(self.obstacle_timer, 800)  # Intervalo para criar novos inimigos

    def update_obstacles(self):
        for obstacle_rect in self.obstacle_rect_list:
            obstacle_rect.x -= 4  # Velocidade dos inimigos
        self.obstacle_rect_list = [obstacle_rect for obstacle_rect in self.obstacle_rect_list if obstacle_rect.right > 0]