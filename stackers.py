from sense_hat import SenseHat
from pygame.locals import *
import pygame
import time
sense = SenseHat()

sense.clear()
yellow=(255,255,0)
blue=(0,0,255)
speed=0.05


class stack():
	def __init__(self):
		pygame.init()
		pygame.display.set_mode((200,480))
		self.gaming =True

	def startGame(self):
		counter_place =0
		counter=0
		y=7
		pygame.time.set_timer(USEREVENT +1, 400)
		while self.gaming:
			
			for event in pygame.event.get():
					if event.type ==KEYDOWN:
							sense.set_pixel(counter,y,(255,0,0))
							
							if y==7:
								counter_place = counter
							if y<=7:
								if counter_place ==counter:
									message ='WINNER!'
								else:
									message ='LOSER!'
									y=-1
							y=y-1		
							if y<0:		
								sense.show_message(message, speed, text_colour=yellow, back_colour=blue)
								self.gaming = False
								sense.clear()
								
							
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
