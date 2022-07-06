
import pygame

import moyu_engine
import tinyland.data.page

LocalsVar = locals()

jm = moyu_engine.json_manager.JsonManager('tinyland/data/json')
config = jm.read_data['config']

pygame.init()
pygame.display.init()
pygame.font.init()
pygame.mixer.init()

window = pygame.display.set_mode(config['window']['size']) # pygame.RESIZABLE
window_title = pygame.display.set_caption('TinyLand')
window_icon = pygame.display.set_icon(pygame.image.load('tinyland/assets/tile/tile1.png'))
window_clock = pygame.time.Clock()

RUN = True

# font_list = [pygame.font.Font('assets/font/LockClock.ttf', size)for size in range(0,(64+1),1)]

game_main_page = tinyland.data.page.game_main.GameMain()
    
while RUN == True:
            window.fill((0,0,0,0))
            
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    RUN = False
                # if event.type == pygame.MOUSEMOTION:
                #     tm.touch(12)
                if event.type == pygame.MOUSEBUTTONDOWN:
                    game_main_page.tilemap_manager.touch(6)
            
            window.blit(game_main_page.renderer(), (0,0))
            
            pygame.display.update()
            window_clock.tick(60)