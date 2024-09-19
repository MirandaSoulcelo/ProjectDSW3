
import pygame

class Score:
    def __init__(self):
        self.text_font()
        self.start_score = pygame.time.get_ticks() // 100
        self.score_surface()
        self.score_rectangle()



    
    def text_font(self):
        self.text = pygame.font.Font('font/Pixeltype.ttf', 60)

    def score_surface(self):
        self.current_time = (pygame.time.get_ticks() // 100) - self.start_score
        self.score_surf = self.text.render(f'Score: {self.current_time}', False, (30, 0, 0))


    def get_surface(self):
        return self.score_surf
    


    
    def score_rectangle(self):
                self.score_rect = self.score_surf.get_rect(center = (400, 50) )


      


    def reset_score(self):
         self.start_score = pygame.time.get_ticks() // 100


  

