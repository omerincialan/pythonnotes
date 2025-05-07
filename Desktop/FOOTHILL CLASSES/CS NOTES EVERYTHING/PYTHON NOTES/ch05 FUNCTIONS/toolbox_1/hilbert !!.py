##
# This program draws a Hilbert curve using Python’s turtle graphics package.
#
import turtle

def main() :
   turtle.reset()
   turtle.penup()
   n = 6
   turtle.goto(-n ** 2 * 10 / 2, n ** 2 * 10 / 2)
   turtle.pendown()
   hilbert(n, 90, 10)
   response = input("Press ENTER to quit.")
   
##  Draws one generation of the Hilbert curve using Turtle graphics.
#  @param n an integer indicating the generation of the curve 
#  @param turn the angle by which to turn the turtle 
#  @param distance the number of pixels to move the turtle forwards
#
def hilbert(n, turn, distance) :
   if n == 1 :
      turtle.forward(distance)
      turtle.right(turn)
      turtle.forward(distance)
      turtle.right(turn)
      turtle.forward(distance)
      # Or, more elegantly,
      # turtle.right(2 * turn)
   else :
      turtle.right(turn)
      hilbert(n - 1, -turn, distance)
      turtle.right(turn)
      turtle.forward(distance)
      hilbert(n - 1, turn, distance)
      turtle.left(turn)
      turtle.forward(distance)
      turtle.left(turn)
      hilbert(n - 1, turn, distance)
      turtle.forward(distance)
      turtle.right(turn)
      hilbert(n - 1, -turn, distance)
      turtle.right(turn)
      
main()      

