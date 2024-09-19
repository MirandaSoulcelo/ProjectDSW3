import pygame
from random import randint

from sys import exit

from Api import get_defeat_joke 

class Surface:
    def __init__(self):
        self.screenWindow()
        self.test_surface()
        self.setup_fonts()
        self.update_joke()  # A cada instância vou atualizando a piada


    def screenWindow(self):
        pygame.display.set_caption('JumpBro')
        self.screen = pygame.display.set_mode((800, 400))

    def test_surface(self):
        self.sky_surface = pygame.image.load('graphics/NightSky3.png').convert()
        self.ground_surface = pygame.image.load('graphics/ground.png').convert()

    def draw(self, player, enemie, score):
        self.screen.blit(self.sky_surface, (0, 0))
        self.screen.blit(self.ground_surface, (0, 300))
        self.screen.blit(score.get_surface(), score.score_rect)

        # Desenha os inimigos
        for rect in enemie.obstacle_rect_list:
            self.screen.blit(enemie.get_surface(), rect)

        self.screen.blit(player.get_surface(), player.player_rect)

    def setup_fonts(self):
        self.font = pygame.font.Font('font/Pixeltype.ttf', 74)
        self.font2 = pygame.font.Font('font/Pixeltype.ttf', 50)
        self.font3 = pygame.font.Font('font/Pixeltype.ttf', 25)
        self.game_over_text = self.font.render('GAME OVER', True, (255, 255, 255))
        self.restart = self.font2.render('Press Space to start', True, (255, 255, 255))
        self.title = self.font2.render('JumpBro', True, (255, 255, 255))

    def update_joke(self):
        self.joke = get_defeat_joke()  # Atualiza a piada

    def show_game_over(self, final_score, game_state):
        self.screen.fill('Black')
        if final_score == 0 and not game_state:
            self.screen.blit(self.restart, (self.screen.get_width() // 2 - self.restart.get_width() // 2,
                                           self.screen.get_height() // 2 + self.restart.get_height() // 2 - 70))
            self.screen.blit(self.title, (self.screen.get_width() // 2 - self.title.get_width() // 2,
                                          self.screen.get_height() // 2 + self.title.get_height() // 2 - 150))
        else:
            self.screen.blit(self.game_over_text, (self.screen.get_width() // 2 - self.game_over_text.get_width() // 2,
                                                   self.screen.get_height() // 2 - self.game_over_text.get_height() // 2 - 150))
            final_S = self.font.render(f'Your Score: {final_score}', True, (255, 255, 255))
            self.screen.blit(final_S, (self.screen.get_width() // 2 - final_S.get_width() // 2,
                                       self.screen.get_height() // 2 + final_S.get_height() // 2 - 150))
         
            joke_text = self.font3.render(self.joke, True, (255, 255, 255))
            self.screen.blit(joke_text, (self.screen.get_width() // 2 - joke_text.get_width() // 2,
                                         self.screen.get_height() // 2 + joke_text.get_height() // 2))