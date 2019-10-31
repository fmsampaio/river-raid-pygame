import pygame
from Settings import *

class Camera():

    def __init__(self, height, width, initPosition):
        self.width = width
        self.height = height
        self.camera = pygame.Rect(initPosition[0], initPosition[1], self.width, self.height)
        self.position = initPosition
        self.update()

    def apply(self, entity):
        return entity.rect.move(self.camera.topleft)

    def update(self):       
        x = self.position[0]
        y = self.position[1]
        self.camera = pygame.Rect(x, y, self.width, self.height)

    def apply_rect(self, rect):
        return rect.move(self.camera.topleft)

    def moveAhead(self):
        if self.position[1] <= - CAMERA_SPEED * TILESCALE:
            self.position = (self.position[0], self.position[1] + CAMERA_SPEED)
            self.update()
        print(self.position)

    