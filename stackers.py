from sense_hat import SenseHat
from pygame.locals import *
import pygame
import time
sense = SenseHat()

sense.clear()

class stack():
	def __init__(self):
		pygame.init()
		pygame.display.set_mode((200,480))
		self.gaming =True

	def startGame(self):
		counter=0
		pygame.time.set_timer(USEREVENT +1, 800)
		while self.gaming:
			
			for event in pygame.event.get():
					if event.type ==KEYDOWN:
							sense.set_pixel(counter,7,(255,0,0))
							self.gaming = False
					else:					
							sense.set_pixel(counter,7,(165,42,42))
							time.sleep(0.1)
							sense.clear()
							counter=counter+1
							x=counter
							if counter>7:
								counter=0
						

if __name__=='__main__':
	try:
		game = stack()
		game.startGame()
	except KeyboardInterrupt:
		sense.clear()
