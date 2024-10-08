from Entities.Player import *
from Entities.Enemie import *
from Entities.Score import *
from Entities.Surface import *
from Entities.Music import *
import pygame
from sys import exit  # finaliza qualquer código quando chamado


class Game:
    def __init__(self):
        pygame.init()
        pygame.mixer.init()
        self.game_state()
        self.surface = Surface()

        self.music = Music()
        self.player = Player()
        self.enemie = Enemie()
        self.score = Score()
        self.music_playing = False
        self.ending_playing = False
        self.clock()

    def game_state(self):
        self.game_active = False

    def clock(self):
        self.clocktime = pygame.time.Clock()

    def colisions(self):
        for obstacle_rect in self.enemie.obstacle_rect_list:
            if obstacle_rect.colliderect(self.player.player_rect):
                self.game_active = False
                print('colision')

    def loop_event(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
            if self.game_active:
                if event.type == pygame.MOUSEBUTTONDOWN:
                    self.player.mouse_jump(event.pos)
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_SPACE:
                        self.player.player_jump()
                if event.type == self.enemie.obstacle_timer:
                    new_obstacle_x = randint(900, 1000)
                    new_obstacle_rect = self.enemie.get_surface().get_rect(midbottom=(new_obstacle_x, 300))

                   
                    if all(abs(new_obstacle_rect.x - existing_obstacle.x) > self.enemie.min_distance for existing_obstacle in self.enemie.obstacle_rect_list):
                        self.enemie.obstacle_rect_list.append(new_obstacle_rect)

            else:
                if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
                    self.game_active = True
                    self.enemie.obstacle_rect_list = []  
                    self.score.reset_score()
                    self.ending_playing = False  
                    self.music_playing = False   
                    self.surface.update_joke() 

    def run(self):
        while True:
            self.loop_event()
            
    
            if self.game_active:
                self.player.player_gravity()
                self.player.animate()
                self.enemie.animate()

                if not self.music_playing: 
                    self.music.get_ost()
                    self.music_playing = True
                    self.ending_playing = False  

                self.enemie.update_obstacles()  
                self.colisions()  
                self.score.score_surface()  
                self.surface.draw(self.player, self.enemie, self.score)  

            else:
                if not self.ending_playing and self.score.current_time != 0:
                    pygame.mixer.music.stop() 
                    self.music.get_ending()  
                    self.ending_playing = True

                self.surface.show_game_over(self.score.current_time, self.game_active)

            pygame.display.update()  
            self.clocktime.tick(60)  # Mantém 60 FPS