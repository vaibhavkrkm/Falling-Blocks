import pygame
from config import game_display
import colors

def mainloop():
	# filling the screen with the grey color
	game_display.fill(colors.earth_green)

	# updating the game display surface
	pygame.display.update()
