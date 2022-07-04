
import pygame

class Tile:
    def __init__(self,pos,code,tile_data,pixal_level):
        self.pos = pos
        self.code = code
        self.tile_data = tile_data
        self.pixal_level = pixal_level
        
        self.offset = [100,50]
        
        self.assets = [pygame.image.load('assets/tile/tile'+str(i)+'.png')for i in range(0,(14+1),1)]
        
        self.rect = self.assets[self.code].get_rect()
        self.width = self.rect.width
        
        self.mask = pygame.image.load('assets/mask/landtile_mask.png').convert_alpha()
        self.mask = pygame.transform.scale(self.mask,((self.width*self.pixal_level),(self.width*self.pixal_level)))
        
        self.grow_timer_time = 0
        
    def renderer(self,surface):
        self.timer()
        self.rect.x = self.pos['z']*(self.width/2)-self.pos['x']*(self.width/2)+self.offset[0]
        self.rect.y = self.pos['x']*(self.width/4)+self.pos['z']*(self.width/4)+self.offset[1]+(-self.width/2)*int(self.pos['y'])
        
        surface.blit(self.assets[self.code], self.rect)
        
    def timer(self):
        try:
            grow_timer = self.tile_data[str(self.code)]['grow_timer']
            grow_nextfps = self.tile_data[str(self.code)]['grow_nextfps']
            if grow_timer >= 0:
                self.grow_timer_time += 1
            if self.grow_timer_time == grow_timer:
                self.code = grow_nextfps
                self.grow_timer_time = 0
        except:
            pass
        
    def touch(self):
        if self.pos['y'] == '1':
            touch_rect = self.rect.copy()
            touch_rect.width *= self.pixal_level
            touch_rect.height *= self.pixal_level 
            touch_rect.x *= self.pixal_level
            touch_rect.y = touch_rect.y*self.pixal_level + touch_rect.height/2
            
            pos = pygame.mouse.get_pos()
            tile_mask = pygame.mask.from_surface(self.mask)
            pos_in_mask = (pos[0]-touch_rect.x),(pos[1]-touch_rect.y)
            touching = touch_rect.collidepoint(*pos) and tile_mask.get_at(pos_in_mask)
            
            if pygame.mouse.get_pressed()[0] == True:
                if touching == True:
                    if self.code == 0:
                        self.code = 12
