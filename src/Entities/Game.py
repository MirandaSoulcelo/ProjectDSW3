
from Entities.Player import *
from Entities.Enemie import *
from Entities.Score import *
from Entities.Surface import *
import pygame
from sys import exit  # finaliza qualquer código quando chamado

class Game:
    def __init__(self):
        pygame.init()
        self.game_state()
        self.surface = Surface()
        self.player = Player()
        self.enemie = Enemie()
        self.score = Score()
       
        self.clock()
      
        

    
    def game_state(self):
        self.game_active = False

    
   
    def clock(self):
        self.clocktime = pygame.time.Clock()

   

    def colisions(self):#com esse método eu vou conseguir aplicar a lógica de derrota
        #rect1.collidepoint((x,y)) ele verifica se um determinado retangulo colidiu com determinada posição
        if self.enemie.enemie_rect.colliderect(self.player.player_rect) == 1:#me entrega 0 ou 1 como resultado(true or false)
            self.game_active = False
            print('colision')
        #self.mouse_pos = pygame.mouse.get_pos()
        #if self.player.player_rect.collidepoint((self.mouse_pos)):
         #   print(pygame.mouse.get_pressed())

    def loop_event(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
            if self.game_active == True:     
                if event.type == pygame.MOUSEBUTTONDOWN:
                    self.player.mouse_jump(event.pos)
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_SPACE:
                       self.player.player_jump()
                if event.type == self.enemie.obstacle_timer:
                    print('teste')
                
            else:
                if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
                        self.game_active = True
                        self.enemie.enemie_rect.left = 800
                        self.score.reset_score()


            
                        

    def run(self):
        while True:
            self.loop_event()
            

            self.player.player_gravity()
            if self.game_active == True:
                self.score.score_surface()
                self.surface.draw(self.player, self.enemie, self.score)
            
                self.enemie.update_position()  # Atualiza a posição dos inimigos
                self.colisions()
            else: 
              self.surface.show_game_over(self.score.current_time, self.game_active)
              

            pygame.display.update()
            self.clocktime.tick(60)  # isso vai obrigar o while a rodar 60 vezes por segundo pra fixar a taxa de quadros







