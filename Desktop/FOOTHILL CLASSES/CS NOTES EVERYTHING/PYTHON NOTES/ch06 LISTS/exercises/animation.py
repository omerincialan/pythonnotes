##
#  This program draws a moving block.
#

from graphics import GraphicsWindow
from time import sleep

def main() :
   # Do not look at the code in the main function.
   # Your code will go into the draw function below.
   
   WIN_WIDTH = 400
   WIN_HEIGHT = 400   
   
   win = GraphicsWindow(WIN_WIDTH, WIN_HEIGHT)
   canvas = win.canvas()
   canvas.setFill("black")
   canvas.clear()
   
   DELAY = 0.01   # 10 milliseconds between frames

   for frame in range(WIN_WIDTH + 1) :
      draw(canvas, frame)
      sleep(DELAY)
   
   win.wait()
   
## Draws a frame on the canvas.
#  @param canvas the canvas on which to draw the frame
#  @param frame which frame as a number
#
def draw(canvas, frame) :
   BLOCK_WIDTH = 20
   BLOCK_HEIGHT = 20
   
   canvas.clear()
   canvas.drawRect(frame, 0, BLOCK_WIDTH, BLOCK_HEIGHT)


# Start the program.
main()

