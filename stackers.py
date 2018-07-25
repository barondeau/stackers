from sense_hat import SenseHat
from pygame.locals import *
import pygame
import time
sense = SenseHat()

sense.clear()

class stack():
	def __init__(self):
		pygame.init()
		pygame.display.set_mode((640,480))
		self.gaming =True

	def startGame(self):
		pygame.time.set_timer(USEREVENT +1,99900)
		while self.gaming:
			counter=0
			for event in pygame.event.get():
					while counter<=7:
						sense.set_pixel(counter,7,(165,42,42))
						time.sleep(0.1)
						sense.clear()
						counter=counter+1
						if counter>7:
							counter=0

if __name__=='__main__':
	try:
		game = stack()
		game.startGame()
	except KeyboardInterrupt:
		sense.clear()
