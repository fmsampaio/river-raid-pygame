import pygame
import pytmx

from Settings import *

class MapLoader:
    def __init__(self, file):
        tm = pytmx.load_pygame(file, pixelalpha=True)
        self.width = tm.width * tm.tilewidth * TILESCALE
        self.height = tm.height * tm.tileheight * TILESCALE
        
        self.tmdata = tm
    
    def render(self, surface, game):
        ti = self.tmdata.get_tile_image_by_gid
        #tempSurface2 = pygame.Surface(surface.get_size(), pygame.SRCALPHA)
        tempSurface = pygame.Surface(surface.get_size())
        for layers in self.tmdata.visible_layers:
            if layers.name == 'terrains' and isinstance(layers, pytmx.TiledTileLayer):
                    for x, y, gid in layers:
                        tile = ti(gid)
                        if tile:
                            if gid == 0:
                                pass
                            else:
                                tempSurface.blit(pygame.transform.scale(tile, (self.tmdata.tilewidth * TILESCALE, self.tmdata.tileheight * TILESCALE)), (x * self.tmdata.tilewidth * TILESCALE, y * self.tmdata.tileheight * TILESCALE))
                    self.terrainLayer = tempSurface
                    
    
    def makeMap(self, game):
        tempSurface = pygame.Surface((self.width, self.height))
        self.render(tempSurface, game)
        return tempSurface

    def getProportions(self):
        return (self.height, self.width)