import pygame

class Player:
    def __init__(self):
        self.frame_index = 0 
        self.player_surfaces()  
        self.player_rectangle()
        self.is_jumping = False
        self.gravity = 0
        self.jump_strength = -16

        self.animation_speed = 0.25  

    def player_surfaces(self):
   
        self.run_frames = [
            pygame.image.load('graphics/PlayerSoraJump/runningsora8.png').convert_alpha(),
            pygame.image.load('graphics/PlayerSoraJump/runningsora7.png').convert_alpha(),
            pygame.image.load('graphics/PlayerSoraJump/runningsora6.png').convert_alpha(),
            pygame.image.load('graphics/PlayerSoraJump/runningsora5.png').convert_alpha(),
            pygame.image.load('graphics/PlayerSoraJump/runningsora4.png').convert_alpha(),
            pygame.image.load('graphics/PlayerSoraJump/runningsora3.png').convert_alpha(),
            pygame.image.load('graphics/PlayerSoraJump/runningsora2.png').convert_alpha(),
            pygame.image.load('graphics/PlayerSoraJump/runningsora1.png').convert_alpha(),
        ]
        self.player_surf = self.run_frames[self.frame_index]

    def get_surface(self):
        return self.player_surf
    
    def player_rectangle(self):
        self.player_rect = self.player_surf.get_rect(midbottom=(50, 300))
        return self.player_rect

    def animate(self):
        
        self.frame_index += self.animation_speed
        if self.frame_index >= len(self.run_frames):
            self.frame_index = 0
        # Atualiza a superfície do jogador
        self.player_surf = self.run_frames[int(self.frame_index)]

    def player_gravity(self):
        if self.is_jumping:
            self.gravity += 1  

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