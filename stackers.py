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
		y=7
		pygame.time.set_timer(USEREVENT +1, 800)
		while self.gaming:
			
			for event in pygame.event.get():
					if event.type ==KEYDOWN:
							sense.set_pixel(counter,y,(255,0,0))
							y=y-1
							if y<0:					
								self.gaming = False
							
					else:					
							sense.set_pixel(counter,y,(165,42,42))
							time.sleep(0.1)
							sense.set_pixel(counter,y,(0,0,0))
							counter=counter+1
							if counter>7:
								counter=0
						

if __name__=='__main__':
	try:
		game = stack()
		game.startGame()
	except KeyboardInterrupt:
		sense.clear()
