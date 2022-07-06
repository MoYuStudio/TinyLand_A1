
import pygame

class Sound:
    def __init__(self):
        self.assets = 'tinyland/assets/music/Sakuya2.mp3'
        self.volume = 0.15
        self.channel = 0
        self.loop = True
    
    def play(self):
        sound = pygame.mixer.Sound(self.assets)
        sound.set_volume(self.volume)
        if self.loop == True:
            pygame.mixer.Channel(self.channel).play(sound,loops=0)
        if self.loop == False:
            pygame.mixer.Channel(self.channel).play(sound,loops=1)