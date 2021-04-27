import board
import neopixel

pixels = neopixel.NeoPixel(board.D18, 20)

for i in range (18):
	pixels[i] = (127,0,255)
