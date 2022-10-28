import sys

import pygame
import time
from settings import Settings
from ship import Ship


#initializa the game and create a screen object

pygame.init()
ai_settings= Settings()
screen = pygame.display.set_mode((ai_settings.screen_width, ai_settings.screen_height))
pygame.display.set_caption('Alien Invasion')

ship = Ship(screen)



#draw the screen
screen.fill(ai_settings.bg_color)
ship.blitme()
#draw ship at the location
screen.blit(image, rect)
sys.exit()


#make most recently drawn screen visible
pygame.display.flip()

time.sleep(2)
