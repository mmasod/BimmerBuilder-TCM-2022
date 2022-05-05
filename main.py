# import the pygame module
import pygame
from util import runtime
from scene import main_screen

pygame.init()
background_colour = (255, 255, 255)
screen = pygame.display.set_mode((1280, 720))
pygame.display.set_caption('Bimmer Builder')
screen.fill(background_colour)
pygame.display.flip()

main_screen.display_main_scene()

#Game Loop
while runtime.running:

    for event in pygame.event.get():

        # Check for Quit event
        if event.type == pygame.QUIT:
            runtime.running = False
            pygame.quit()
            quit()

    pygame.display.update()