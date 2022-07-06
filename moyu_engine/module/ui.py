
import time
import pygame

class ui:
    def __init__(self):
        pass
    
    def renderer(self):
        pass
    
    def touch(self):
        if pygame.Rect.collidepoint(self.MenuSetting_text3_rect,self.event.pos):
            pygame.mixer.Channel(1).play(pygame.mixer.Sound("assets/sound/effect/switch_001.ogg"))
            time.sleep(0.1)
    