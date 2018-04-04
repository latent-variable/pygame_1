# Allow pygame_sdl2 to be imported as pygame.
# config:python android.py configure ~/Documents/hobby/pygame/race_to_the_moon
# Build:python android.py --launch build ~/Documents/hobby/pygame/race_to_the_moon release
import pygame

import game


if __name__=='__main__':
    game.init()
    game.loop()
    pygame.quit()
    quit()
