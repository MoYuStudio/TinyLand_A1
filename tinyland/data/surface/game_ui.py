
import pygame

import moyu_engine

class GameUI:
    def __init__(self):
        self.json_manager = moyu_engine.json_manager.JsonManager('tinyland/data/json')
        self.data = self.json_manager.read_data
        self.config = self.data['config']
        self.pixal_level = self.config['window']['pixal_level']
        
        self.ui = pygame.image.load('tinyland/assets/ui/ui1.png')
        self.ui_ract = self.ui.get_rect()
    
    def renderer(self,surface):
        window_width, window_height = pygame.display.get_surface().get_size()
        surface = pygame.Surface((window_width/self.pixal_level,window_height/self.pixal_level)).convert_alpha()
        surface.fill((0,0,0,0))
        
        pygame.draw.rect(surface, (255,202,40), pygame.Rect(0, 0, window_width, 16))
        
        surface.blit(self.ui,(window_width/self.pixal_level-self.ui_ract.width,window_height/self.pixal_level-self.ui_ract.height))
        
        
        self.surface = pygame.transform.scale(surface,(window_width, window_height))