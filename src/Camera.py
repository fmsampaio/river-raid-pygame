import pygame
from Settings import *

class Camera():

    def __init__(self, height, width):
        self.width = width
        self.height = height
        self.camera = pygame.Rect(0,0, self.width, self.height)

    def apply(self, entity):
        return entity.rect.move(self.camera.topleft)

    def update(self, cameraCenter):       
        #TODO check map boundaries (- self.mapRect.height + SCREEN_SIZE[1])
        
        x = cameraCenter[0]
        y = cameraCenter[1]
        self.camera = pygame.Rect(x, y, self.width, self.height)

    def apply_rect(self, rect):
        return rect.move(self.camera.topleft)
