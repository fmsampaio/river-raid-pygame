import pygame
import pytmx
from Settings import *


class mapLoader:

    def __init__(self, file):
        tm = pytmx.load_pygame(file, pixelalpha=True)
        self.width = tm.width * tm.tilewidth * TILESCALE
        self.height = tm.height * tm.tileheight * TILESCALE
        self.tmdata = tm


    def makeMap(self):
        ti = self.tmdata.get_tile_image_by_gid
        tmpSurface = pygame.Surface((self.width, self.height))
        for layers in self.tmdata.visible_layers:
            if isinstance(layers, pytmx.TiledTileLayer):
                for x, y, gid in layers:
                    tile = ti(gid)
                    if tile:
                        #tmpSurface.blit(pygame.transform.scale(tile, (self.tmdata.tilewidth, self.tmdata.tileheight)), (x * self.tmdata.tilewidth, y * self.tmdata.tileheight))
                        tmpSurface.blit(pygame.transform.scale(tile, (self.tmdata.tilewidth * TILESCALE, self.tmdata.tileheight * TILESCALE)), (x * self.tmdata.tilewidth * TILESCALE, y * self.tmdata.tileheight * TILESCALE))
                self.terrainLayer = tmpSurface


    def getProportions(self):
        return (self.height, self.width)
