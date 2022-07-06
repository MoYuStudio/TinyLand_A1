
import pygame

import moyu_engine

class GameTilemap:
    def __init__(self):
        self.json_manager = moyu_engine.json_manager.JsonManager('tinyland/data/json')
        self.data = self.json_manager.read_data
        self.config = self.data['config']
        self.pixal_level = self.config['window']['pixal_level']
        self.tilemap_manager = moyu_engine.tilemap_manager.TilemapManager(self.data['map_1'],self.data['tile'])
    def renderer(self,surface):
        window_width, window_height = pygame.display.get_surface().get_size()
        surface = pygame.Surface((window_width/self.pixal_level,window_height/self.pixal_level)).convert_alpha()
        surface.fill((0,0,0,0))
        
        self.tilemap_manager.renderer(surface)
        
        self.surface = pygame.transform.scale(surface,(window_width, window_height))
