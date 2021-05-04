import board
import neopixel

pixels = neopixel.NeoPixel(board.D18, 20)

pixels[4] = (100,0,0)

