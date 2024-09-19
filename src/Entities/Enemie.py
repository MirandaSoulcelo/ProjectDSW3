import pygame
from random import randint

class Enemie:
    def __init__(self):
        self.frame_index = 0
        self.enemie_surface()
        self.timer()
        self.obstacle_rect_list = []
        self.min_distance = 250  # Ajuste conforme necessário
        self.animation_speed = 0.2

    def enemie_surface(self):
        
        self.run_frames =[
        pygame.image.load('graphics/Shadow/shadow1.png').convert_alpha(),
        pygame.image.load('graphics/Shadow/shadow2.png').convert_alpha(),
        pygame.image.load('graphics/Shadow/shadow3.png').convert_alpha(),
        pygame.image.load('graphics/Shadow/shadow4.png').convert_alpha(),
        pygame.image.load('graphics/Shadow/shadow5.png').convert_alpha(),
        pygame.image.load('graphics/Shadow/shadow6.png').convert_alpha(),
        pygame.image.load('graphics/Shadow/shadow7.png').convert_alpha(),
        pygame.image.load('graphics/Shadow/shadow8.png').convert_alpha(),
        
        
        
        ]
        self.enemie_surf = self.run_frames[self.frame_index]

    def get_surface(self):
        return self.enemie_surf

    def timer(self):
        self.obstacle_timer = pygame.USEREVENT + 1
        pygame.time.set_timer(self.obstacle_timer, 700)  # Intervalo para criar novos inimigos
    
    def animate(self):
        
        self.frame_index += self.animation_speed
        if self.frame_index >= len(self.run_frames):
            self.frame_index = 0
     
        self.enemie_surf = self.run_frames[int(self.frame_index)]

    def update_obstacles(self):
        for obstacle_rect in self.obstacle_rect_list:
            obstacle_rect.x -= randint(4, 13) 
        self.obstacle_rect_list = [obstacle_rect for obstacle_rect in self.obstacle_rect_list if obstacle_rect.right > 0]