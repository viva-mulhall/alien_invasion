import pygame
import time
from settings import Settings

#initializa the game and create a screen object

pygame.init()
ai_settings= Settings()
screen = pygame.display.set_mode((ai_settings.screen_width, ai_settings.screen_height))



screen.fill(ai_settings.bg_color)

#make the most recently drawn screen visible

pygame.display.flip()
time.sleep(2)