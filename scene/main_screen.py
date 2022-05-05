
import pygame
from scene import scene_manager

def display_main_scene():
    bg_color = (0, 0, 0)

    X = 1280
    Y = 720

    display_surface = pygame.display.set_mode((X, Y))

    pygame.display.set_caption('main_screen_m_logo')

    image = pygame.image.load('assets/pics/bmw-m-logo.png')

    pygame.draw.rect(display_surface, bg_color, [590, 315, 80 , 30])

    while True:

        if scene_manager.current_scene == 0:
            display_surface.fill(bg_color)

            # copying the image surface object
            # to the display surface object at
            # (0, 0) coordinate.
            display_surface.blit(image, (200, 0))

            # Draws the surface object to the screen.
            pygame.display.update()



