
import pygame

class Tile:
    def __init__(self,pos,code):
        self.pos = pos
        self.code = code
        
        self.tile_assets = [pygame.image.load('assets/tile/tile'+str(i)+'.png')for i in range(0,(14+1),1)]
        
    def renderer(self,surface):
        tile_rect = self.tile_assets[self.code].get_rect() # 获取图片的矩形
        tile_rect.x = self.pos['z']*(self.tile_width/2)-self.pos['x']*(self.tile_width/2)+self.pos[0] # 设置矩形的x坐标
        tile_rect.y = self.pos['x']*(self.tile_width/4)+self.pos['z']*(self.tile_width/4)+self.pos[1]+(-self.tile_width/2)*int(self.pos['y']) # 设置矩形的y坐标
        
        if self.pos['y'] == '0':
            pass