import pygame

from Settings import *

class Bullet(pygame.sprite.Sprite):
    def __init__(self, player, display):
        super().__init__()
        x = player.rect.centerx
        y = player.rect.top

        self.rect = pygame.Rect(x, y, BULLET_SIZE[0] * TILESCALE, BULLET_SIZE[1] * TILESCALE)
        self.display = display
    
    def draw(self, camera):
        pygame.draw.rect(self.display, BULLET_COLOR, camera.apply_rect(self.rect))

    def update(self, enemies):
        self.rect.y -= BULLET_SPEED

        