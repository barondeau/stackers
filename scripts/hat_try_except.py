from sense_hat import SenseHat
sense =SenseHat()
import time
sense.clear()
def loop():
	while True:
		sense.set_pixel(1,6,(255,0,0))
		time.sleep(0.01)
		sense.set_pixel(1,6,(0,0,0))

if __name__ == '__main__':
	try:
		loop()
	except KeyboardInterrupt:
		sense.clear()
