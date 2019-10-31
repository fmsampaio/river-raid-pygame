import pygame
import random
import os.path

from MapLoader import mapLoader
from Settings import *
from Ground import Ground
from Camera import Camera
from Player import Player

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
        self.mapImg = self.map.makeMap()
        self.mapRect = self.mapImg.get_rect()

        self.grounds = pygame.sprite.Group()

        self.cameraCenter = (0, (- self.mapRect.height + SCREEN_SIZE[1]) * TILESCALE)
        self.camera = Camera(self.mapRect.width, self.mapRect.height, self.cameraCenter)

        for obj in self.map.tmdata.objects:
            if obj.name == 'ground':
                self.grounds.add(Ground(obj.x * TILESCALE, obj.y * TILESCALE, obj.width * TILESCALE, obj.height * TILESCALE))
            elif obj.name == 'goal':
                self.goal = (obj.x, obj.y)
            elif obj.name == 'player': 
                self.player = Player(obj.x, obj.y, self.screen)
                self.player.moveAhead = True
           
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
            
        key = pygame.key.get_pressed()
        
        """
        if key[pygame.K_w]:
            if self.cameraCenter[1] < -(CAMERA_SPEED * 2):
                self.cameraCenter = (self.cameraCenter[0], self.cameraCenter[1] + CAMERA_SPEED)
        elif key[pygame.K_s]:
            if self.cameraCenter[1] > (-self.mapRect.height + SCREEN_SIZE[1]):
                self.cameraCenter = (self.cameraCenter[0], self.cameraCenter[1] - CAMERA_SPEED)
        """

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
        self.camera.moveAhead()
        
    def draw(self):
        self.screen.fill((0, 0, 0))
        self.screen.blit(self.map.terrainLayer, self.camera.apply_rect(self.mapRect))
        self.player.draw(self.camera)
        pygame.display.flip()

if __name__ == '__main__':
    a = game()
    a.gameRun()