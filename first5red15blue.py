import board
import neopixel

pixels = neopixel.NeoPixel(board.D18, 20)

for i in range (5):
	pixels[i] = (100,0,0)
for i in range(6,20):
	pixels[i] = (0,0,100)
