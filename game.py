import pygame
import config
from mainloop import mainloop
import sys

def QUIT():
	pygame.quit()
	sys.exit()

# run variable for controling the main while loop
run = True
while run:
	# event section start
	for event in pygame.event.get():
		if(event.type == pygame.QUIT):
			QUIT()

	# event section end

	# mainloop function for the main game loop (in another .py file)
	mainloop()
