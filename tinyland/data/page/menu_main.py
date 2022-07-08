
import pygame

import moyu_engine

class MenuMain:
    def __init__(self):
        self.json_manager = moyu_engine.json_manager.JsonManager('tinyland/data/json')
        self.data = self.json_manager.read_data
        self.config = self.data['config']
        self.pixal_level = self.config['window']['pixal_level']
        
        self.window_size = pygame.display.get_surface().get_size()
        
        self.background1 = pygame.image.load('tinyland/assets/background/background3.png')
        self.background1_ract = self.background1.get_rect()
        
        self.tile0_small = pygame.image.load('tinyland/assets/tile/tile0.png')
        self.tile1_small = pygame.image.load('tinyland/assets/tile/tile1.png')
        self.tile0 = pygame.transform.scale(self.tile0_small,(16*self.pixal_level*2, 16*self.pixal_level*2))
        self.tile1 = pygame.transform.scale(self.tile1_small,(16*self.pixal_level*2, 16*self.pixal_level*2))
        self.tile1_rect = self.tile1.get_rect()
        
        self.timer = 0
        
        self.tile1_ui = moyu_engine.module.ui.UI()
        
        self.switch = None
        
        
    def background(self):
        surface = pygame.Surface((self.background1_ract.width,self.background1_ract.height)).convert_alpha()
        surface.fill((0,0,0,0))
        surface.blit(self.background1,(100,100))
        surface = pygame.transform.scale(surface,(self.background1_ract.width*self.pixal_level, self.background1_ract.height*self.pixal_level))
        
        return surface
    
    def renderer(self):
        
        page = pygame.Surface((self.window_size[0],self.window_size[1])).convert_alpha()
        page.fill((0,0,0,0))
        page.blit(self.background(),(0,0))
        
        self.timer += 1
        if self.timer//360>=1:
            self.timer = 0
        rot_rect = pygame.transform.rotate(self.tile1,self.timer)
        page.blit(rot_rect,(self.window_size[0]/2-self.tile1_rect.width/2,self.window_size[1]/2-self.tile1_rect.height/2))
        self.tile1_ui.image_button_renderer(page,self.tile0,pos=[self.window_size[0]/2-self.tile1_rect.width/2,self.window_size[1]/2-self.tile1_rect.height/2])
        
        return page
    
    def page_event(self,event):
        self.event = event
        
        if self.event.type == pygame.MOUSEBUTTONDOWN:
            try:
                if self.tile1_ui.touch() == True:
                    print('start')
                    self.switch = 'game_main_page'
            except:
                pass
            
    def page_switch(self):
        return self.switch
        