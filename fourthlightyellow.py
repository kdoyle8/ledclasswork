import board
import neopixel

pixels = neopixel.NeoPixel(board.D18, 20)

pixels[3] = (255,255,0)

