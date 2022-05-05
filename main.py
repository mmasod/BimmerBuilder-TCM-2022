# import the pygame module
import pygame

background_colour = (255, 255, 255)
screen = pygame.display.set_mode((1280, 720))
pygame.display.set_caption('Bimmer Builder')
screen.fill(background_colour)
pygame.display.flip()

running = True

#Game Loop
while running:

    for event in pygame.event.get():

        # Check for Quit event
        if event.type == pygame.QUIT:
            running = False
