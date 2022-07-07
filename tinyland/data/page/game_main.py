
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
        
        self.tile_assets_small = [pygame.image.load('tinyland/assets/tile/tile'+str(i)+'.png')for i in range(0,(15+1),1)]
        self.tile_assets = [pygame.transform.scale(self.tile_assets_small[i],(64, 64))for i in range(0,(15+1),1)]
        
        self.background1 = pygame.image.load('tinyland/assets/background/background3.png')
        self.background1_ract = self.background1.get_rect()
        
        self.tilemap_offset = [self.window_size[0]/self.pixal_level/2,self.window_size[1]/self.pixal_level/2]
        
        self.move_up = False
        self.move_down = False
        self.move_left = False
        self.move_right = False
        
        self.text_button = moyu_engine.module.ui.UI()
        self.image_button_list = {}
        for i in range(0,16,1):
            self.image_button_list['tile'+str(i)] = moyu_engine.module.ui.UI()
        
        self.tile_pick_menu_active = False
        
        self.tile_pick = 6
        
    def background(self):
        surface = pygame.Surface((self.background1_ract.width,self.background1_ract.height)).convert_alpha()
        surface.fill((0,0,0,0))
        surface.blit(self.background1,(-self.tilemap_offset[0],-self.tilemap_offset[1]))
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

        surface = pygame.transform.scale(surface,(self.window_size[0], self.window_size[1]))
        
        self.text_button.text_button_renderer(surface,text='menu',pos=[self.window_size[0]-200,self.window_size[1]-100],font_size=64)
        
        return surface
    
    def tile_pick_menu(self):
        surface = pygame.Surface((self.window_size[0]/self.pixal_level,self.window_size[1]/self.pixal_level)).convert_alpha()
        surface.fill((0,0,0,0))
        
        surface.fill((0,0,0,150))
        
        surface = pygame.transform.scale(surface,(self.window_size[0], self.window_size[1]))
        
        x,y = 0,0
        for i in range(0,16,1):
            self.image_button_list['tile'+str(i)].image_button_renderer(surface,self.tile_assets[i],pos=[100+x*(64+64),100+y*(64+32)])
            if x == 7:
                x = 0
            x+=1
            y=i//7
            
            
            
            
            # surface.blit(self.tile_assets[i],(i*16,100))
                
        
        
        
        return surface
    
    def renderer(self):

        if self.move_up == True:
            self.tilemap_offset[1] -= 1
        if self.move_down == True:
            self.tilemap_offset[1] += 1
        if self.move_left == True:
            self.tilemap_offset[0] -= 1
        if self.move_right == True:
            self.tilemap_offset[0] += 1
        
        page = pygame.Surface((self.window_size[0],self.window_size[1])).convert_alpha()
        page.fill((0,0,0,0))
        
        page.blit(self.background(),(0,0))
        page.blit(self.tilemap(),(0,0))
        page.blit(self.ui(),(0,0))
        
        if self.tile_pick_menu_active == True:
            page.blit(self.tile_pick_menu(),(0,0))
        
        # page = pygame.transform.scale(page,(self.window_size[0], self.window_size[1]))
        
        return page
    
    def page_event(self,event):
        self.event = event
         
        # if event.type == pygame.MOUSEMOTION:
        #     tm.touch(12)
        
        if self.tile_pick_menu_active == False:
            if self.event.type == pygame.MOUSEBUTTONDOWN:
                
                self.tilemap_manager.touch(self.tile_pick, self.tilemap_offset)
                
                if self.text_button.touch() == True:
                    self.tile_pick_menu_active = True
                
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
                    
        if self.tile_pick_menu_active == True:
            if self.event.type == pygame.MOUSEBUTTONDOWN:
                try:
                    for i in range(0,16,1):
                        if self.image_button_list['tile'+str(i)].touch() == True:
                            self.tile_pick = i
                except:
                    pass
                            
            if self.event.type == pygame.KEYDOWN:
                if self.event.key == pygame.K_ESCAPE:
                    self.tile_pick_menu_active = False
        