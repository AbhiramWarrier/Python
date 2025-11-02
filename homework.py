import pygame
pygame.init()
SCREEN_WIDTH, SCREEN_HEIGHT = 500, 500

display_surface = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption('my first game screen')
background_image = pygame.transform.scale(pygame.image.load('background.png').convert(), (SCREEN_WIDTH, SCREEN_HEIGHT))

#tiger_image = pygame.transform.scale(pygame.image.load('hello tiger.png') .convert_alpha(), (300,300))
backgrond_color = (58,158,158)
display_surface.fill(backgrond_color)
pygame.display.flip()
