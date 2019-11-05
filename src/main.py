import pygame
import random
import os.path

from MapLoader import mapLoader
from Settings import *
from Ground import Ground
from Camera import Camera
from Player import Player
from Enemy import Enemy
from Bullet import Bullet

class game():

    def __init__(self):
        pygame.init()
        pygame.font.init()
        pygame.mixer.init()
        self.screenSize = SCREEN_SIZE
        self.fps = FPS
        self.screen = pygame.display.set_mode(self.screenSize)
        self.screen.set_alpha(128)
        pygame.display.set_caption(SCREEN_TITLE + " " + str(SCREEN_SIZE))
        self.clock = pygame.time.Clock()

    def new(self):
        try:
            self.mapPath = os.path.join("../assets/", "stage1.tmx")
            self.map = mapLoader(self.mapPath)
        except:
            self.mapPath = os.path.join("assets/", "stage1.tmx")
            self.map = mapLoader(self.mapPath)
        
        self.map.makeMap()
        self.mapRect = self.map.terrainLayer.get_rect()

        self.grounds = pygame.sprite.Group()
        self.enemies = pygame.sprite.Group()
        self.bullets = pygame.sprite.Group()

        self.cameraCenter = (0, (- self.mapRect.height + SCREEN_SIZE[1]) * TILESCALE)
        self.camera = Camera(self.mapRect.width, self.mapRect.height, self.cameraCenter)

        for obj in self.map.tmdata.objects:
            if obj.name == 'ground':
                self.grounds.add(Ground(obj.x * TILESCALE, obj.y * TILESCALE, obj.width * TILESCALE, obj.height * TILESCALE))
            elif obj.name == 'goal':
                self.goal = (obj.x * TILESCALE, obj.y * TILESCALE)
            elif obj.name == 'player': 
                self.player = Player(obj.x * TILESCALE, obj.y*TILESCALE, self.screen)
                self.player.moveAhead = True
            elif obj.name == 'enemy1':
                self.enemies.add(Enemy(obj.x * TILESCALE, obj.y * TILESCALE, self.screen))

           
    def gameRun(self):
        self.new()
        
        while True:
            self.events()
            self.update()
            self.draw()

    def events(self):
        for e in pygame.event.get():
            if e.type == pygame.QUIT:
                pygame.quit()
                exit()
            if e.type == pygame.KEYDOWN:
                if e.key == pygame.K_SPACE:
                    self.bullets.add(Bullet(self.player, self.screen))
            
        key = pygame.key.get_pressed()
        
        if key[pygame.K_RIGHT]:
            self.player.moveRight = True
        else:
            self.player.moveRight = False
        
        if key[pygame.K_LEFT]:
            self.player.moveLeft = True
        else:
            self.player.moveLeft = False

               
    def update(self):
        self.clock.tick(self.fps)
        self.player.update()
        self.player.checkCollisionWithGround(self.grounds)
        self.camera.moveAhead()
        for enemy in self.enemies:
            enemy.update(self.grounds)
        for bullet in self.bullets:
            bullet.update(self.enemies)
        self.checkCollisionsBulletsWithEnemies()
        self.checkCollisionsPlayerWithEnemies()
        
    def draw(self):
        self.screen.fill((0, 0, 0))
        self.screen.blit(self.map.terrainLayer, self.camera.apply_rect(self.mapRect))
        self.player.draw(self.camera)
        for enemy in self.enemies:
            enemy.draw(self.camera)
        for bullet in self.bullets:
            bullet.draw(self.camera)
        pygame.display.flip()

    def checkCollisionsBulletsWithEnemies(self):
        for bullet in self.bullets:
            for enemy in self.enemies:
                if bullet.rect.colliderect(enemy.rect):
                    self.bullets.remove(bullet)
                    self.enemies.remove(enemy)
    
    def checkCollisionsPlayerWithEnemies(self):
        for enemy in self.enemies:
            if self.player.rect.colliderect(enemy.rect):
                print('Game over!')
                pygame.quit()
                exit()

if __name__ == '__main__':
    a = game()
    a.gameRun()