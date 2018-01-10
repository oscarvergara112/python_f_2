import sys
import pygame
from Game import Game


def run_game():

    pygame.init()
    pygame.display.set_caption("Alien Invasion")

    # Initialize game
    game = Game()

    # Start the main loop for the game.
    while True:
        _update(game)
        _draw(game)


#------------------


def _update(game):
    # CheckEvents
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        elif event.type == pygame.KEYDOWN :
            game.processKeyDown(event.key)
        elif event.type == pygame.KEYUP:
            game.processKeyUp(event.key)

    # Update game (Missing check if update is needed according Game step time)
    game.update()


def _draw(game):
    # Redraw the screen during each pass through the loop. # Update game (Missing check if draw is needed according the desired Game FPS )
    game.draw()




#------------------

run_game()
print("Game exit")

