
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
        
        self.ui1 = pygame.image.load('tinyland/assets/ui/ui1.png')
        self.ui1_ract = self.ui1.get_rect()
        
        self.background1 = pygame.image.load('tinyland/assets/background/background1.png')
        self.background1_ract = self.background1.get_rect()
        
        self.window_size = pygame.display.get_surface().get_size()
        
    def background(self):
        surface = pygame.Surface((self.window_size[0]/self.pixal_level,self.window_size[1]/self.pixal_level)).convert_alpha()
        surface.fill((0,0,0,0))
        surface.blit(self.background1,(0,0))
        surface = pygame.transform.scale(surface,(self.window_size[0], self.window_size[1]))
        
        return surface
    
    def tilemap(self):
        surface = pygame.Surface((self.window_size[0]/self.pixal_level,self.window_size[1]/self.pixal_level)).convert_alpha()
        surface.fill((0,0,0,0))
        self.tilemap_manager.renderer(surface)
        surface = pygame.transform.scale(surface,(self.window_size[0], self.window_size[1]))
        
        return surface
    
    def ui(self):
        surface = pygame.Surface((self.window_size[0]/self.pixal_level,self.window_size[1]/self.pixal_level)).convert_alpha()
        surface.fill((0,0,0,0))
        pygame.draw.rect(surface, (255,202,40), pygame.Rect(0, 0, self.window_size[0], 16))
        surface.blit(self.ui1,(self.window_size[0]/self.pixal_level-self.ui1_ract.width,self.window_size[1]/self.pixal_level-self.ui1_ract.height))
        surface = pygame.transform.scale(surface,(self.window_size[0], self.window_size[1]))
        
        return surface
    
    def renderer(self):
        page = pygame.Surface((self.window_size[0],self.window_size[1])).convert_alpha()
        page.fill((0,0,0,0))
        surface_list = [self.background(),self.tilemap(),self.ui()]
        for surface in surface_list:
            page.blit(surface,(0,0))
        # page = pygame.transform.scale(page,(self.window_size[0], self.window_size[1]))
        
        return page
        
        