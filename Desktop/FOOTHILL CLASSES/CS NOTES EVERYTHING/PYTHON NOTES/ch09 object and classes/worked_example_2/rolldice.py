##
#  Simulates the rolling and drawing of 5 dice using a Die class.
#

from die import Die
from ezgraphics import GraphicsWindow

# Define a constant for die size.
DIE_SIZE = 60

def main() :  
   canvas = configureWindow(DIE_SIZE * 7)
   dice = createDice(DIE_SIZE)   
   rollDice(canvas, dice)  
   while rollAgain() :
      rollDice(canvas, dice)

## Creates the five dice and sets their position on the canvas in two rows 
#  with 3 dice in the first row and 2 in the second row.
#  @param size an integer indicating the dimensions of a single die
#  @return a list containing the five Die objects
#
def createDice(size) :  
   # Store the dice in a list.   
   dice = []
   
   # Set the initial die offset from the upper-left corner of the canvas. 
   xOffset = size
   yOffset = size

   for i in range(5) :
      dice.append(Die(xOffset, yOffset, size))      
      if i == 2 :
         xOffset = size * 2
         yOffset = size * 3
      else :
         xOffset = xOffset + size * 2
         
   return dice      

## Prompt the user as to whether they want to roll again or quit.
#  @return True if the user wants to roll again
#
def rollAgain() :
   userInput = input("Press the Enter key to roll again or enter Q to quit: ")
   if userInput.upper() == "Q" :
      return False
   else :
      return True

## Create and configure the graphics window.
#  @param winSize the vertical and horizontal size of the window
#  @return the canvas used for drawing
#
def configureWindow(winSize) :
   win = GraphicsWindow(winSize, winSize)
   canvas = win.canvas()
   canvas.setBackground(0, 128, 0)
   return canvas
  
## Simulates the rolling of 5 dice and draws the face of each die on the canvas.
#  @param canvas the graphical canvas on which to draw the dice
#  @param dice the list of Die objects
#
def rollDice(canvas, dice) :
   # Clear the canvas of all objects.
   canvas.clear()
      
   # Roll and draw each of 5 dice.
   for die in dice :
      die.roll()
      die.draw(canvas)
      
# Start the program.
main()

