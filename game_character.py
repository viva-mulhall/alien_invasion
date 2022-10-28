import pygame
import time

from settings import Settings
#initializa the game and create a screen object

pygame.init()
ai_settings= Settings()
screen = pygame.display.set_mode((ai_settings.screen_width, ai_settings.screen_height))
pygame.display.set_caption('Alien Invasion')

#make a ship
#load
# Load the ship image and get its rect.

image = pygame.image.load('ship.bmp')
rect = image.get_rect()
screen_rect = screen.get_rect()


#start each new ship at the center of the screen
rect.centerx = screen_rect.centerx
rect.bottom = screen_rect.centery

#draw the screen
screen.fill(ai_settings.bg_color)

#draw ship at the location
screen.blit(image, rect)

#make most recently drawn screen visible
pygame.display.flip()

time.sleep(2)

