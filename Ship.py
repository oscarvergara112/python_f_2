import pygame


class Ship():
    def __init__(self, screen):
        """Initialize the ship and set its starting position."""
        self.screen = screen

        # Load the ship image and get its rect.
        self.image = pygame.image.load('images/ship.png')

        # Start each new ship at the bottom center of the screen.
        self.rect = self.image.get_rect()
        self.rect.centerx = screen.get_rect().centerx
        self.rect.bottom = screen.get_rect().bottom

        self.movingRight = False
        self.movingLeft = False

    def moveRight(self, movement):
        self.movingRight = movement
        self.movingLeft = False

    def moveLeft(self, movement):
        self.movingRight = False
        self.movingLeft = movement

    def update(self):
        if self.movingRight:
            if self.rect.centerx < self.screen.get_rect().width:
                self.rect.centerx += 1
        elif self.movingLeft:
            if self.rect.centerx > 0:
                self.rect.centerx -= 1


    def draw(self):
        """Draw the ship at its current location."""
        self.screen.blit(self.image, self.rect)  # draws the Ship image into the screen
