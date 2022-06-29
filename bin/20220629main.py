
import math
import pygame

import map

pygame.init()
pygame.display.init()
pygame.font.init()
pygame.mixer.init()

tile_list = [pygame.image.load('assets/tile/tile'+str(i)+'.png')for i in range(0,(4+1),1)]
building_list = [pygame.image.load('assets/building/building'+str(i)+'.png')for i in range(0,(8+1),1)]

font_list = [pygame.font.Font('assets/font/LockClock.ttf', size)for size in range(0,(64+1),1)]

window_size = (1280,720)
window = pygame.display.set_mode(window_size)#pygame.RESIZABLE
window_title = pygame.display.set_caption('TineLand')
window_icon = pygame.display.set_icon(tile_list[1])
window_clock = pygame.time.Clock()

RUN = True

tile_width = 64

time_map = [[0 for x in range(len(map.tile_map))] for y in range(len(map.tile_map[0]))]
tile_rect_map = [[[]for x in range(len(map.tile_map))] for y in range(len(map.tile_map[0]))]

move_x, move_y = window.get_width()/2, window.get_height()/2

# animation1 y = ax^2 + bx + c
animation1_time, animation1_fix = 25, True

# animation2 y = sin(ax+b)*c
animation2_time = 0

coin = 0

def draw_tile(surface):
    for row in range(len(map.tile_map)):
        for column in range(len(map.tile_map[row])):
            tile_rect_fn(row, column, surface, tile_list, map.tile_map, 'tile')
            tile_rect_fn(row, column, surface, building_list, map.building_map, 'building')

def tile_rect_fn(row, column, surface, list, map, type):
    for tile in range(len(list)):
        if map[row][column] == tile:
            tile_rect = list[tile].get_rect()
            tile_rect.x = column*(tile_width/2)-row*(tile_width/2)+move_x
            if type == 'tile':
                tile_rect.y = row*(tile_width/4)+column*(tile_width/4)+move_y
                tile_rect_map[row][column]  = tile_rect
            if type == 'building':
                tile_rect.y = row*(tile_width/4)+column*(tile_width/4)+move_y-tile_width/2
            surface.blit(list[tile], tile_rect)

def touch_tile():
    global coin
    for row in range(len(tile_rect_map)):
        for column in range(len(tile_rect_map[row])):
            touch_rect = tile_rect_map[row][column]
            touch_rect.x = tile_rect_map[row][column].x + tile_rect_map[row][column].width/5
            touch_rect.y = tile_rect_map[row][column].y + tile_rect_map[row][column].height/11
            touch_rect.width = tile_rect_map[row][column].width/2
            touch_rect.height = tile_rect_map[row][column].height/3
            if pygame.Rect.collidepoint(touch_rect, pygame.mouse.get_pos()):
                if map.tile_map[row][column] == 0 or\
                    map.tile_map[row][column] == 1 and \
                    map.building_map[row][column] == 0 :
                    map.building_map[row][column] = 1

                if map.building_map[row][column] == 5:
                    map.building_map[row][column] = 1
                    coin += 1

def time_set():
    for row in range(len(time_map)):
        for column in range(len(time_map[row])):
            if map.building_map == 5:
                time_map[row][column] = 0
            for i in range(1,5,1):
                if map.building_map[row][column] == i:
                    time_map[row][column] += 1
                if map.building_map[row][column] == i and time_map[row][column] == 100:
                    map.building_map[row][column] = i+1
                    time_map[row][column] = 0

while RUN == True:
    time_set()
    window.fill((0,0,0,0))

    ui_surface = pygame.Surface(window_size).convert_alpha()
    ui_surface.fill((0,0,0,0))

    def draw_ui_text(info, pos, color, size, surface):
        text = font_list[size].render(info, True, color)
        surface.blit(text, pos)
    def draw_ui_tilebar(num, icon, price, surface):
        icon_rect = icon.get_rect()
        icon_rect.x = 0
        icon_rect.y = 64*num
        surface.blit(icon, icon_rect)
        draw_ui_text(str(price), (60,64*(num+1)), (255,255,255), 16, surface)
    
    draw_ui_text('TinyLand a2022061701', (0,0), (255,255,255), 16, ui_surface)
    draw_ui_text('Coin '+str(coin), (window_size[0]-250,0), (255,255,255), 32, ui_surface)

    draw_ui_tilebar(0, building_list[1], 0, ui_surface)
    draw_ui_tilebar(1, building_list[6], 10, ui_surface)
    draw_ui_tilebar(2, building_list[7], 10, ui_surface)
    draw_ui_tilebar(3, building_list[8], 30, ui_surface)

    window.blit(ui_surface, (0,0))

    tilemap_surface = pygame.Surface(window_size).convert_alpha()
    tilemap_surface.fill((0,0,0,0))
    draw_tile(tilemap_surface)

    if animation2_time == 100:
        animation2_time = 0
    if animation1_time > 0:
        animation1_time-=0.2
        animation_y = -(-1*animation1_time**2 + 9*animation1_time)
    if animation1_time <= 0 and animation1_fix == True:
        animation_y-=0.1
        if animation_y <= (math.sin(math.degrees(10)+animation2_time))*3:
            animation_y = (math.sin(math.degrees(10)+animation2_time))*3
            animation1_fix = False
    if animation1_time <= 0 and animation1_fix == False:
        animation2_time+=0.05
        animation_y = (math.sin(math.degrees(10)+animation2_time))*3

    window.blit(tilemap_surface, (0,animation_y))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            RUN = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            touch_tile()
    
    pygame.display.update()
    window_clock.tick(60)