
import random

import noise
import pygame

class TilemapManager:
    def __init__(self,map,tile_data,pixal_level=4):
        self.map = map
        self.tile_data = tile_data
        self.pixal_level = pixal_level
        
        self.tile_width = 16
        
        self.tile_assets = [pygame.image.load('assets/tile/tile'+str(i)+'.png')for i in range(0,(14+1),1)]
        self.landtile_mask = pygame.image.load('assets/mask/landtile_mask.png').convert_alpha()
        self.landtile_mask = pygame.transform.scale(self.landtile_mask,((self.tile_width*self.pixal_level),(self.tile_width*self.pixal_level)))
        
            
        self.pos = [100,50]
        
        self.touch_rect_map = [[[]for x in range(len(self.map['0']))] for y in range(len(self.map['0'][0]))]
        
    def noise(self):
        boarder = 32
        seed = random.randint(100000, 999999)
        octaves = 2
        freq = 12
        
        tilemap = [[int(noise.pnoise2((x/freq)+seed,(y/freq)+seed,octaves)*100+50) for x in range(0,boarder,1)] for y in range(0,boarder,1)]

    def renderer(self,surface):
        for level in self.map: # land, building
            for row in range(len(self.map['0'])): # row行
                for column in range(len(self.map['0'][row])): # column列
                    
                    the_tile_assets = self.tile_assets[self.map[level][row][column]]
                    
                    tile_rect = the_tile_assets.get_rect() # 获取图片的矩形
                    tile_rect.x = column*(self.tile_width/2)-row*(self.tile_width/2)+self.pos[0] # 设置矩形的x坐标
                    tile_rect.y = row*(self.tile_width/4)+column*(self.tile_width/4)+self.pos[1]+(-self.tile_width/2)*int(level) # 设置矩形的y坐标
                    
                    if level == '0':
                        self.touch_rect_map[row][column] = tile_rect

                    surface.blit(the_tile_assets, tile_rect) # 绘制图片
    
    def timer(self):
        for row in range(len(self.map['building'])): # row行
            for column in range(len(self.map['building'][row])): # column列
                if self.tile_building[str(self.map['building'][row][column])]['timer'] >= 0:
                    self.map['timer'][row][column] += 1
                if self.map['timer'][row][column] == self.tile_building[str(self.map['building'][row][column])]['timer']:
                    self.map['building'][row][column] += 1
                    self.map['timer'][row][column] = 0
    
    def touch(self,build_tile):
        try:
            for row in range(len(self.touch_rect_map)):
                for column in range(len(self.touch_rect_map[row])):
                    touch_rect = self.touch_rect_map[row][column]
                    
                    touch_rect.x = self.touch_rect_map[row][column].x*self.pixal_level
                    touch_rect.y = self.touch_rect_map[row][column].y*self.pixal_level
                    touch_rect.width = self.touch_rect_map[row][column].width*self.pixal_level
                    touch_rect.height = self.touch_rect_map[row][column].height*self.pixal_level
                    
                    pos = pygame.mouse.get_pos()
                    tile_mask = pygame.mask.from_surface(self.landtile_mask)
                    pos_in_mask = (pos[0]-touch_rect.x),(pos[1]-touch_rect.y)
                    touching = touch_rect.collidepoint(*pos) and tile_mask.get_at(pos_in_mask)
                    
                    # self.map['1'][row][column] = 14
                    
                    if pygame.mouse.get_pressed()[0] == True:
                        if touching == True:
                            if self.map['1'][row][column] == 0:
                                for buildable_tile in self.tile_data[str(build_tile)]['buildable']:
                                    if self.map['0'][row][column] == buildable_tile:
                                        self.map['1'][row][column] = build_tile
                                        
        except:
            pass
                    
if __name__ == '__main__':
    pass