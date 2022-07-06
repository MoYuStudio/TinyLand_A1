
import pygame

import moyu_engine

class GameBackground:
    def __init__(self):
        self.json_manager = moyu_engine.json_manager.JsonManager('tinyland/data/json')
        self.data = self.json_manager.read_data
        self.config = self.data['config']
        self.pixal_level = self.config['window']['pixal_level']
        
        self.background = pygame.image.load('tinyland/assets/background/background1.png')
        self.background_ract = self.background.get_rect()
    
    def renderer(self,surface):
        window_width, window_height = pygame.display.get_surface().get_size()
        surface = pygame.Surface((window_width/self.pixal_level,window_height/self.pixal_level)).convert_alpha()
        surface.fill((0,0,0,0))
        
        surface.blit(self.background,(0,0))
        self.surface = pygame.transform.scale(surface,(window_width, window_height))