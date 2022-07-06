
import pygame

from . import module

class MusicManager:
    def __init__(self):
        self.max_channels = 10
        
        pygame.mixer.init()
        pygame.mixer.pre_init(44100, -16, self.max_channels, 2048)
        
        self.bgm()
        
    def bgm(self):
        self.bgm_sound = module.sound.Sound()
        
    def play(self):
        self.bgm_sound.play()