
import math
import pygame

import core

LocalsVar = locals()

jm = core.json_manager.JsonManager('json',LocalsVar)

tile_list = {}

pygame.init()
pygame.display.init()
pygame.font.init()
pygame.mixer.init()

# font_list = [pygame.font.Font('assets/font/LockClock.ttf', size)for size in range(0,(64+1),1)]

window_size = (1280,720)
window = pygame.display.set_mode(window_size) # pygame.RESIZABLE
window_title = pygame.display.set_caption('TinyLand')
window_icon = pygame.display.set_icon(pygame.image.load('assets/tile/tile1.png'))
window_clock = pygame.time.Clock()

RUN = True

tm = core.tilemap_manager.TilemapManager(map_1,tile)

while RUN == True:
    window.fill((0,0,0,0))
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            RUN = False
        # if event.type == pygame.MOUSEMOTION:
        #     tm.touch(12)
        if event.type == pygame.MOUSEBUTTONDOWN:
            tm.touch(6)
            
    tilemap_surface = pygame.Surface((window_size[0]/4,window_size[1]/4)).convert_alpha()
    tilemap_surface.fill((0,0,0,0))
    
    tm.renderer(tilemap_surface)
    
    tilemap_surface = pygame.transform.scale(tilemap_surface,window_size)
    window.blit(tilemap_surface, (0,0))
    
    pygame.display.update()
    window_clock.tick(60)
    
