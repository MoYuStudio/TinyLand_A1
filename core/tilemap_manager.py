
import random
import noise

import pygame

class TilemapManager:
    def __init__(self,map):
        self.map = map
        
        self.tile_width = 64
        
        self.assets = {
            'land':[pygame.image.load('assets/land/land'+str(i)+'.png')for i in range(0,(4+1),1)],
            'building':[pygame.image.load('assets/building/building'+str(i)+'.png')for i in range(0,(8+1),1)]
        }
        
        self.pos = [0,0]
        
        self.touch_rect_map = [[[]for x in range(len(self.map['land']))] for y in range(len(self.map['land'][0]))]
        
    def noise(self):
        boarder = 32
        seed = random.randint(100000, 999999)
        octaves = 2
        freq = 12
        
        tilemap = [[int(noise.pnoise2((x/freq)+seed,(y/freq)+seed,octaves)*100+50) for x in range(0,boarder,1)] for y in range(0,boarder,1)]

    def renderer(self,surface):
        for tile_list in self.assets:
            for row in range(len(self.map['land'])): # 行
                for column in range(len(self.map['land'][row])):
                    tile_rect = self.assets[tile_list][self.map[tile_list][row][column]].get_rect()
                    tile_rect.x = column*(self.tile_width/2)-row*(self.tile_width/2)+self.pos[0]
                    if tile_list == 'land':
                        tile_rect.y = row*(self.tile_width/4)+column*(self.tile_width/4)+self.pos[1]
                        self.touch_rect_map[row][column]  = tile_rect
                    if tile_list == 'building':
                        tile_rect.y = row*(self.tile_width/4)+column*(self.tile_width/4)+self.pos[1]-self.tile_width/2
                    surface.blit(self.assets[tile_list][self.map[tile_list][row][column]], tile_rect)
                
    def timer(self):
        pass
    
    def touch(self):
        pass
    
if __name__ == '__main__':
    pass