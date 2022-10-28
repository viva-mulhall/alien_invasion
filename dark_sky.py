import pygame

#initializa the game and create a screen object

pygame.init()
screen = pygame.display.set_mode((400,300))
pygame.display.set_caption('alien invasion')

#make the most recently drawn screen visible

pygame.display.flip()