
import math
import pygame

import map

tile_list = [pygame.image.load('assets/tile/tile'+str(i)+'.png')for i in range(0,4,1)]
building_list = [pygame.image.load('assets/building/building'+str(i)+'.png')for i in range(0,8,1)]

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
animation1_time = 25
animation1_fix = True

# animation2 y = sin(ax+b)*c
animation2_time = 0

pygame.init()
pygame.display.flip()

def draw_tile(surface):

    for row in range(len(map.tile_map)):
        for column in range(len(map.tile_map[row])):

            for tile in range(len(tile_list)):
                if map.tile_map[row][column] == tile:
                    tile_rect = tile_list[tile].get_rect()
                    tile_rect.x = column*(tile_width/2)-row*(tile_width/2)+move_x
                    tile_rect.y = row*(tile_width/4)+column*(tile_width/4)+move_y
                    tile_rect_map[row][column]  = tile_rect
                    surface.blit(tile_list[tile], tile_rect)
            for tile in range(len(building_list)):
                if map.building_map[row][column] == tile:
                    tile_rect = building_list[tile].get_rect()
                    tile_rect.x = column*(tile_width/2)-row*(tile_width/2)+move_x
                    tile_rect.y = row*(tile_width/4)+column*(tile_width/4)+move_y-tile_width/2
                    surface.blit(building_list[tile], tile_rect)

def touch_tile(type):
    for row in range(len(tile_rect_map)):
        for column in range(len(tile_rect_map[row])):
            touch_rect = tile_rect_map[row][column]
            touch_rect.x = tile_rect_map[row][column].x + tile_rect_map[row][column].width/6
            touch_rect.y = tile_rect_map[row][column].y + tile_rect_map[row][column].height/6
            touch_rect.width = tile_rect_map[row][column].width/2
            touch_rect.height = tile_rect_map[row][column].height/4
            if pygame.Rect.collidepoint(touch_rect, pygame.mouse.get_pos()):
                if type == 'mouse_motion':
                    pass
                if type == 'mouse_button_down':
                    map.building_map[row][column] = 1

def time_set():
    for row in range(len(time_map)):
        for column in range(len(time_map[row])):

            if map.building_map == 5:
                time_map[row][column] = 0
            for i in range(1,5,1):
                if map.building_map[row][column] == i:
                    time_map[row][column] += 1
                if map.building_map[row][column] == i and time_map[row][column] == 10:
                    map.building_map[row][column] = i+1
                    time_map[row][column] = 0

while RUN == True:
    time_set()
    window.fill((0,0,0,0))

    tilemap_surface = pygame.Surface(window_size).convert_alpha()
    tilemap_surface.fill((0,0,0,0))
    draw_tile(tilemap_surface)

    if animation2_time == 1000:
        animation2_time = -300
    if animation1_time > 0:
        animation1_time-=0.2
        animation_y = -(-1*animation1_time**2 + 9*animation1_time)
    if animation1_time <= 0 and animation1_fix == True:
        animation_y-=0.5
        if animation_y <= (math.sin(math.degrees(15)+animation2_time))*10:
            animation_y = (math.sin(math.degrees(15)+animation2_time))*10
            animation1_fix = False

    if animation1_time <= 0 and animation1_fix == False:
        animation2_time+=0.05
        animation_y = (math.sin(math.degrees(15)+animation2_time))*10

    window.blit(tilemap_surface, (0,animation_y))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            RUN = False
        if event.type == pygame.MOUSEMOTION:
            touch_tile(type='mouse_motion')
        if event.type == pygame.MOUSEBUTTONDOWN:
            touch_tile(type='mouse_button_down')
    
    pygame.display.update()
    window_clock.tick(60)