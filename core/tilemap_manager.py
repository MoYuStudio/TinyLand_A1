
import random

import noise
import pygame

class TilemapManager:
    def __init__(self,map,tile_land,tile_building):
        self.map = map
        self.tile_land = tile_land
        self.tile_building = tile_building
        
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
        for tile_list in self.assets: # land, building
            for row in range(len(self.map['land'])): # row行
                for column in range(len(self.map['land'][row])): # column列
                    tile_rect = self.assets[tile_list][self.map[tile_list][row][column]].get_rect() # 获取图片的矩形
                    tile_rect.x = column*(self.tile_width/2)-row*(self.tile_width/2)+self.pos[0] # 设置矩形的x坐标
                    if tile_list == 'land': # 如果是地面
                        tile_rect.y = row*(self.tile_width/4)+column*(self.tile_width/4)+self.pos[1] # 设置矩形的y坐标
                        self.touch_rect_map[row][column]  = tile_rect # 设置矩形的y坐标
                    if tile_list == 'building': # 如果是建筑
                        tile_rect.y = row*(self.tile_width/4)+column*(self.tile_width/4)+self.pos[1]-self.tile_width/2 # 设置矩形的y坐标
                    surface.blit(self.assets[tile_list][self.map[tile_list][row][column]], tile_rect) # 绘制图片
    
    def timer(self):
        # for key in self.tile_building:
        #     print(self.tile_building[key]['timer'])
        
        for row in range(len(self.map['building'])): # row行
            for column in range(len(self.map['building'][row])): # column列
            
                # timer
                if self.tile_building[str(self.map['building'][row][column])]['timer'] >= 0:
                    self.map['timer'][row][column] += 1
                if self.map['timer'][row][column] == self.tile_building[str(self.map['building'][row][column])]['timer']:
                    self.map['building'][row][column] += 1
                    self.map['timer'][row][column] = 0
        
        # return self.map
        
    def touch(self):
        pass
    
if __name__ == '__main__':
    pass