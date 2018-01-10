import pygame

from Settings import Settings
from Ship import Ship

class Game():
    def __init__(self):
        """Initialize game."""

        self.settings = Settings()
        self.initScreen()

        self.ship = Ship(self.screen)

        # Startup app sound
        pygame.mixer.music.load('sounds/start.mp3')
        pygame.mixer.music.play(0)

    def draw(self):
        # Draw Background & a rectangle
        self.screen.fill(self.settings.bg_color)
        pygame.draw.rect(self.screen, (60, 60, 180), self.small_screen_rect )

        # Draw Ship
        self.ship.draw()


        # Make the most recently Drawn screen visible.
        pygame.display.flip()

    def update(self):
        # Draw Background
        self.ship.update()

    def processKeyDown(self, key):
        if key == pygame.K_RIGHT:
            self.ship.moveRight(True)
        elif key == pygame.K_LEFT:
            self.ship.moveLeft(True)

    def processKeyUp(self, key):
        if key == pygame.K_RIGHT:
            self.ship.moveRight(False)
        elif key == pygame.K_LEFT:
            self.ship.moveLeft(False)


    def initScreen(self):
        self.screen = pygame.display.set_mode((self.settings.screen_width, self.settings.screen_height))
        self.screen_rect = self.screen.get_rect()
        self.small_screen_rect = pygame.Rect(30, 30, self.settings.screen_width - 60, self.settings.screen_height - 60 )