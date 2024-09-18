import pygame

from Entities.Player import *
from Entities.Enemie import *
from Entities.Score import *
from sys import exit 


class Surface:
    def __init__(self):
        self.screenWindow()
        self.test_surface()
        self.setup_fonts()


    def screenWindow(self):
        pygame.display.set_caption('JumpBro')
        self.screen = pygame.display.set_mode((800, 400))




    def test_surface(self):
        self.sky_surface = pygame.image.load('graphics/NightSky3.png').convert()
        self.ground_surface = pygame.image.load('graphics/ground.png').convert()

 

    def draw(self, player, enemie, score):
        self.screen.blit(self.sky_surface, (0, 0))
        self.screen.blit(self.ground_surface, (0, 300))
        #pygame.draw.rect(self.screen, 'black', score.score_rect)
        #pygame.draw.rect(self.screen, 'black', score.score_rect, 30, 1)
        self.screen.blit(score.get_surface(), score.score_rect)
        
        enemie.update_position()
        self.screen.blit(enemie.get_surface(), enemie.enemie_rect)
        self.screen.blit(player.get_surface(), player.player_rect)

    def setup_fonts(self):
            self.font = pygame.font.Font('font/Pixeltype.ttf', 74)  # Fonte padrão e tamanho 74
            self.font2 = pygame.font.Font('font/Pixeltype.ttf', 50)  # Fonte padrão e tamanho 
            self.game_over_text = self.font.render('GAME OVER', True, (255, 255, 255))
            self.restart = self.font2.render('Press Space to start', True, (255, 255, 255))
            self.title = self.font2.render('JumpBro', True, (255, 255, 255))
        


        
    
    def show_game_over(self, final_score, game_state):
        self.screen.fill('Black')
        if final_score == 0 and game_state == False:
            self.screen.blit(self.restart, 
                (self.screen.get_width() // 2 - self.restart.get_width() // 2,
                self.screen.get_height() // 2 + self.restart.get_height() // 2 - 70))
            self.screen.blit(self.title, 
                (self.screen.get_width() // 2 - self.title.get_width() // 2,
                self.screen.get_height() // 2 + self.title.get_height() // 2 - 150))
        else:
            self.screen.blit(self.game_over_text, 
                (self.screen.get_width() // 2 - self.game_over_text.get_width() // 2,
                self.screen.get_height() // 2 - self.game_over_text.get_height() // 2 - 150))
            
            final_S = self.font.render(f'Your Score: {final_score}', True, (255, 255, 255))
            self.screen.blit(final_S, 
                (self.screen.get_width() // 2 - final_S.get_width() // 2,
                self.screen.get_height() // 2 + final_S.get_height() // 2 - 150))
            
        


      
