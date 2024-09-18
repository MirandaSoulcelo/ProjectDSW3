import pygame

class Player:
    def __init__(self):
        self.player_surface()
        self.player_rectangle()
        self.is_jumping = False
        self.gravity = 0
        self.jump_strength = -20


    def player_surface(self):
        self.player_surf = pygame.image.load('graphics/Runningsora2.png').convert_alpha()

    def get_surface(self):
        return self.player_surf
    
    def player_rectangle(self):
        self.player_rect = self.player_surf.get_rect(midbottom=(50, 300))
        return self.player_rect

    def update_position(self, p):
        # self.player_rect.left += p
        self.teste = print(self.player_rect)
        return self.teste

    def player_gravity(self):
        if self.is_jumping:
            self.gravity += 1  # Simula a aceleração da gravidade

        self.player_rect.y += self.gravity

        if self.player_rect.bottom >= 300:
            self.player_rect.bottom = 300
            self.gravity = 0
            self.is_jumping = False

    def player_jump(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_SPACE] and not self.is_jumping and self.player_rect.bottom == 300:
            self.is_jumping = True
            self.gravity = self.jump_strength

    def mouse_jump(self, mouse_pos):
        if self.player_rect.collidepoint(mouse_pos):
            if not self.is_jumping:
                self.is_jumping = True
                self.gravity = self.jump_strength

