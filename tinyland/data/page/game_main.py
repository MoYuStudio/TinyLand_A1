
from matplotlib.pyplot import cla
import pygame

import moyu_engine

class GameMain:
    def __init__(self):
        self.json_manager = moyu_engine.json_manager.JsonManager('tinyland/data/json')
        self.data = self.json_manager.read_data
        self.config = self.data['config']
        self.pixal_level = self.config['window']['pixal_level']
        
        self.tilemap_manager = moyu_engine.tilemap_manager.TilemapManager(self.data['map_1'],self.data['tile'])
        
        self.window_size = pygame.display.get_surface().get_size()
        
        self.ui1 = pygame.image.load('tinyland/assets/ui/ui1.png')
        self.ui1_ract = self.ui1.get_rect()
        
        self.background1 = pygame.image.load('tinyland/assets/background/background1.png')
        self.background1_ract = self.background1.get_rect()
        
        self.tilemap_offset = [0,0]
        
        self.move_up = False
        self.move_down = False
        self.move_left = False
        self.move_right = False
        
    def background(self):
        surface = pygame.Surface((self.background1_ract.width,self.background1_ract.height)).convert_alpha()
        surface.fill((0,0,0,0))
        surface.blit(self.background1,(0,0))
        surface = pygame.transform.scale(surface,(self.background1_ract.width*self.pixal_level, self.background1_ract.height*self.pixal_level))
        
        return surface
    
    def tilemap(self):
        surface = pygame.Surface((self.window_size[0]/self.pixal_level,self.window_size[1]/self.pixal_level)).convert_alpha()
        surface.fill((0,0,0,0))
        self.tilemap_manager.renderer(surface,self.tilemap_offset)
        surface = pygame.transform.scale(surface,(self.window_size[0], self.window_size[1]))
        
        return surface
    
    def ui(self):
        surface = pygame.Surface((self.window_size[0]/self.pixal_level,self.window_size[1]/self.pixal_level)).convert_alpha()
        surface.fill((0,0,0,0))
        pygame.draw.rect(surface, (255,202,40,150), pygame.Rect(0, 0, self.window_size[0], 16))
        surface.blit(self.ui1,(self.window_size[0]/self.pixal_level-self.ui1_ract.width,self.window_size[1]/self.pixal_level-self.ui1_ract.height))
        surface = pygame.transform.scale(surface,(self.window_size[0], self.window_size[1]))
        
        return surface
    
    def renderer(self):

        if self.move_up == True:
            self.tilemap_offset[1] -= 1
        elif self.move_down == True:
            self.tilemap_offset[1] += 1
        elif self.move_left == True:
            self.tilemap_offset[0] -= 1
        elif self.move_right == True:
            self.tilemap_offset[0] += 1
        
        page = pygame.Surface((self.window_size[0],self.window_size[1])).convert_alpha()
        page.fill((0,0,0,0))

        page.blit(self.background(),(-self.background1_ract.width/2-self.tilemap_offset[0],-self.background1_ract.height/2-self.tilemap_offset[1]))
        page.blit(self.tilemap(),(0,0))
        page.blit(self.ui(),(0,0))
        
        # page = pygame.transform.scale(page,(self.window_size[0], self.window_size[1]))
        
        return page
    
    def page_event(self,event):
        self.event = event
                
        # if event.type == pygame.MOUSEMOTION:
        #     tm.touch(12)
        if self.event.type == pygame.MOUSEBUTTONDOWN:
            self.tilemap_manager.touch(6,self.tilemap_offset)
            
        if self.event.type == pygame.KEYDOWN:
            if self.event.key == pygame.K_UP or self.event.key == pygame.K_w:
                self.move_up = True
            if self.event.key == pygame.K_DOWN or self.event.key == pygame.K_s:
                self.move_down = True
            if self.event.key == pygame.K_LEFT or self.event.key == pygame.K_a:
                self.move_left = True
            if self.event.key == pygame.K_RIGHT or self.event.key == pygame.K_d:
                self.move_right = True
                
        if self.event.type == pygame.KEYUP:
            if self.event.key == pygame.K_UP or self.event.key == pygame.K_w:
                self.move_up = False
            if self.event.key == pygame.K_DOWN or self.event.key == pygame.K_s:
                self.move_down = False
            if self.event.key == pygame.K_LEFT or self.event.key == pygame.K_a:
                self.move_left = False
            if self.event.key == pygame.K_RIGHT or self.event.key == pygame.K_d:
                self.move_right = False
                    
        
        