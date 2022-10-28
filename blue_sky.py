import pygame

#initializa the game and create a screen object

pygame.init()
screen = pygame.display.set_mode((400,300))
pygame.display.set_caption('alien invasion')

#make color background

bg_color = (0,0,255)

screen.fill(bg_color)

#make the most recently drawn screen visible

pygame.display.flip()
time.sleep(2)