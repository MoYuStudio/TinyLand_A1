
import pygame

import moyu_engine
import tinyland.data.page

LocalsVar = locals()

jm = moyu_engine.json_manager.JsonManager('tinyland/data/json')
config = jm.read_data['config']

music_manager = moyu_engine.music_manager.MusicManager()

pygame.init()
pygame.display.init()
pygame.font.init()


window = pygame.display.set_mode(config['window']['size']) # pygame.RESIZABLE
window_title = pygame.display.set_caption('TinyLand')
window_icon = pygame.display.set_icon(pygame.image.load('tinyland/assets/tile/tile1.png'))
window_clock = pygame.time.Clock()

RUN = True

# font_list = [pygame.font.Font('assets/font/LockClock.ttf', size)for size in range(0,(64+1),1)]

page = 'game_main_page'
page_list = {'game_main_page':tinyland.data.page.game_main.GameMain()}

music_manager.play()
    
while RUN == True:
    time_delta = window_clock.tick(60)/1000.0
    window.fill((0,0,0,0))
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            RUN = False
        if page == 'game_main_page':
            page_list['game_main_page'].page_event(event)
        
    if page == 'game_main_page':
        window.blit(page_list['game_main_page'].renderer(), (0,0))
    
    pygame.display.update()
    window_clock.tick(60)