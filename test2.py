import board
import neopixel
import time

pixels = neopixel.NeoPixel(board.D18, 20)

pixels[8] = (0,0,255)

for i in range (10,18,2):
	pixels[i] = (0,0,255)
	time.sleep(.2)

