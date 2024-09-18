import pygame

class Enemie:
    def __init__(self):
        self.enemie_surface()
        self.enemie_position()
        self.enemie_rectangle()
        self.timer()

    def enemie_surface(self):
        self.enemie_surf = pygame.image.load('graphics/shadow1.png').convert_alpha()

    def get_surface(self):
        return self.enemie_surf
    
    def enemie_position(self):
        self.enemie_x_pos = 600
        self.enemie_y_pos = 300

    def enemie_rectangle(self):
        self.enemie_rect = self.enemie_surf.get_rect(bottomright=(self.enemie_x_pos, self.enemie_y_pos))
        return self.enemie_rect

    def update_position(self):
        self.enemie_rect.x -= 4
        if self.enemie_rect.right <= 0:
            self.enemie_rect.left = 800

    def timer(self):
        # Lembre-se de configurar o timer onde for necessário
        self.obstacle_timer = pygame.USEREVENT + 1