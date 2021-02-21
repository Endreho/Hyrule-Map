import pygame, time, random
from pygame.locals import *
from pytmx.util_pygame import  load_pygame


def blit_all_tiles(window, tmxdata, world_offset):
	for layer in tmxdata:
		for tile in layer.tiles():
			x_pixel = tile[0] * 750 + world_offset[0]
			y_pixel = tile[1] * 625 + world_offset[1]
			window.blit(tile[2], (x_pixel, y_pixel))

def main():
    # ********** Game variables **********
    quit = False
    tmxdata = load_pygame('1X.tmx')
    world_offset = [0,0]
    # ********** Start game loop **********
    while not quit:
        window.fill((0,0,0))                            # Reset screen to black
        blit_all_tiles(window, tmxdata, world_offset)
        # ********** Process events **********
        keyspressed = pygame.key.get_pressed()
        for event in pygame.event.get():
            if event.type == QUIT:
                quit = True

        # ********** Your game logic here **********

        # ********** Update screen **********
        pygame.display.update()                         # Actually does the screen update
        clock.tick(60)                                  # Run the game at 25 frames per second

# ********** Initialise & run the game **********
if __name__ == "__main__":
    width, height = 1024, 600                            # Set screen width,height
    pygame.init()                                       # Start graphics system
    pygame.mixer.init()                                 # Start audio system
    window = pygame.display.set_mode((width, height))   # Create window
    pygame
    clock = pygame.time.Clock()                         # Create game clock
    main()
    pygame.quit()
