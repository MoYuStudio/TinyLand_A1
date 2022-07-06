
from . import module

class TilemapManager:
    def __init__(self,map,tile_data,pixal_level=4):
        self.map = map
        self.tile_data = tile_data
        
        self.tile_list = {}
        
        for y in self.map:
            for x in range(len(self.map[y])):
                for z in range(len(self.map[y][x])):
                    tile_pos = {'x':x,'y':y,'z':z}
                    tile_code = self.map[y][x][z]
                    self.tile_list[str(x)+'_'+str(y)+'_'+str(z)] = module.tile.Tile(tile_pos,tile_code,self.tile_data,pixal_level)
                
    def renderer(self,surface,pos_offset=[0,0]):
        self.surface = surface
        for tile in self.tile_list:
            self.tile_list[tile].offset = pos_offset
            self.tile_list[tile].renderer(self.surface)
            
    def touch(self,change_tile,pos_offset=[0,0]):
        for tile in self.tile_list:
            self.tile_list[tile].offset = pos_offset
            self.tile_list[tile].touch(change_tile)