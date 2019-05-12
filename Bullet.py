import pygame


class Bullet(pygame.sprite.Sprite):
    def __init__(self, settings, screen, ship):
        super(Bullet, self).__init__()
        self.screen = screen
        self.rect = pygame.Rect(ship.rect.centerx - settings.bullet_width / 2, ship.rect.top - settings.bullet_height,

                                settings.bullet_width, settings.bullet_height)
        self.speed = 5

    def update(self):
        self.rect.top -= self.speed

    def draw(self):
        pygame.draw.rect(self.screen, (255, 0, 0), self.rect)
