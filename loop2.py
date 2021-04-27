import board
import neopixel
import time

pixels = neopixel.NeoPixel(board.D18, 20)

for i in range (10,18,2):
	pixels[i] = (180,32,220)
	time.sleep(.2)
