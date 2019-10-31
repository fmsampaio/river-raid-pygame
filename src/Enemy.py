import pygame

from Settings import *

class Enemy(pygame.sprite.Sprite):
    def __init__(self, x, y, display):
        super().__init__()
        self.rect = pygame.Rect(x, y, 32 * TILESCALE, 32 * TILESCALE)
        self.tmpEnemyColor = (255, 100, 100)
        self.display = display
        self.direction = 1
    
    def draw(self, camera):
        pygame.draw.rect(self.display, self.tmpEnemyColor, camera.apply_rect(self.rect))

    def update(self, grounds):
        if (self.rect.right >= (SCREEN_SIZE[0] * TILESCALE) or self.rect.left <= 0) or pygame.sprite.spritecollide(self, grounds, False):
            self.direction *= -1

        self.rect.x += (ENEMY1_SPEED * self.direction)
