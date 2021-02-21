import pygame
import time
from pygame.locals import *
clock = pygame.time.Clock()
pygame.init()
WHITE = (255, 255, 255)
WIDTH = 1024
HEIGHT = 600
windowSurface = pygame.display.set_mode((WIDTH, HEIGHT), 0, 32)
originalImg = pygame.image.load("Map over Hyrule (3).png")
img = pygame.transform.scale(originalImg,(WIDTH,HEIGHT))

while True:
        events = pygame.event.get()
        button_down = pygame.mouse.get_pressed()
        if button_down == (0,1,0):
            #print("Clicked")
            WIDTH = WIDTH+10
            HEIGHT = HEIGHT+10
            img = pygame.transform.scale(originalImg, (WIDTH, HEIGHT))
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        windowSurface.fill(WHITE)
        windowSurface.blit(img, (0, 0))
        clock.tick(60)
        pygame.display.flip()