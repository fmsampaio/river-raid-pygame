class Game:
    def __init__(self):
        pygame.init()
        self.screenSize = SCREEN_SIZE
        self.fps = FPS
        self.screen = pygame.display.set_mode(self.screenSize)
        self.screen.set_alpha(128)
        pygame.display.set_caption(SCREEN_TITLE)
        self.clock = pygame.time.Clock()
        