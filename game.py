import pygame 
import random 
from grid import Grid
from patterns import Patterns
from colors import Colors
class Game: 

    def __init__(self):
        pygame.init()
        self.runing, self.playing, self.paused = True, False, False 
        self.WIDTH, self.HEIGHT = 800, 800
        self.grid = Grid(20, self.WIDTH, self.HEIGHT)
        self.FPS = 60 
        self.screen = pygame.display.set_mode((self.WIDTH, self.HEIGHT))
        self.display = pygame.Surface((self.WIDTH, self.HEIGHT))
        self.clock = pygame.time.Clock()
        self.patterns = Patterns()
        self.positions = set()
        self.count = 0
        self.font_name = 'RETROTECH.ttf'
        self.mid_w, self.mid_h = self.WIDTH // 2, self.HEIGHT // 2
    



        
        

    def main(self):
        self.running = True
        self.playing = False 
        self.paused = False
        update_freq = 60



        while self.running:

            self.check_events()
            
            self.clock.tick(self.FPS) 

            if  not self.paused:
                self.count += 1

            if self.count >= update_freq:
                self.count = 0
                self.positions = self.grid.adjust_grid(self.positions)


            if self.playing:
                self.screen.fill(Colors.BLACK)
                self.grid.draw_grid(self.screen, self.positions)
            else: 
                G_of_Lx, G_of_Ly = self.mid_w, self.mid_h
                self.screen.fill(Colors.BLACK)
                self.draw_text("GAME OF LIFE", 100, G_of_Lx, G_of_Ly)
                self.draw_text("press ENTER", 40, G_of_Lx, G_of_Ly + 150)



            
            
            pygame.display.update()

        pygame.quit()



    def gen(self, num):
        return set([(random.randrange(0, self.grid.grid_height), random.randrange(0, self.grid.grid_width)) for _ in range(num)])     


    def check_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False

            if event.type == pygame.MOUSEBUTTONDOWN:
                x, y = pygame.mouse.get_pos()
                col = x // self.grid.tile_size
                row = y // self.grid.tile_size
                pos = (col, row)

                if pos in self.positions:
                    self.positions.remove(pos)
                else:
                    self.positions.add(pos)

            if event.type == pygame.KEYDOWN:

                if event.key == pygame.K_RETURN:
                    self.playing = True
                
                if event.key == pygame.K_SPACE:
                    self.paused = not self.paused 



                if event.key == pygame.K_c:
                    self.positions = set()
                    self.paused = True 
                    self.count = 0
 
                if event.key == pygame.K_r:
                    self.positions = self.gen(random.randrange(4, 10) * self.grid.grid_width)

                if event.key == pygame.K_g:
                    self.positions = self.patterns.load_pattern(self.patterns.glider)

                if event.key == pygame.K_u:
                    self.positions = self.patterns.load_pattern(self.patterns.gosper_glider_gun)

                if event.key == pygame.K_p:
                    self.positions = self.patterns.load_pattern(self.patterns.pulsar)



    def draw_text(self, text, size, x, y):
        font = pygame.font.Font(self.font_name, size)
        text_surface = font.render(text, True, Colors.WHITE)
        text_rec = text_surface.get_rect()
        text_rec.center = (x,y)
        self.screen.blit(text_surface, text_rec)


