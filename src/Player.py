import pygame
from Settings import *
from Camera import *

class Player:
    def __init__(self, xInit, yInit, display):
        self.rect = pygame.Rect(xInit, yInit, 32 * TILESCALE, 32 * TILESCALE)
        self.display = display

        self.moveRight = False
        self.moveLeft = False
        self.moveAhead = False

        self.tmpPlayerColor = (255,255,255)

    def draw(self, camera):
        pygame.draw.rect(self.display, self.tmpPlayerColor, camera.apply_rect(self.rect))

    def update(self):
        if self.moveRight and self.rect.right < SCREEN_SIZE[0]*TILESCALE:
            self.rect.centerx += PLAYER_SPEED
        elif self.moveLeft and self.rect.left > 0:
            self.rect.centerx -= PLAYER_SPEED
        
        if self.moveAhead:
            self.rect.centery -= CAMERA_SPEED