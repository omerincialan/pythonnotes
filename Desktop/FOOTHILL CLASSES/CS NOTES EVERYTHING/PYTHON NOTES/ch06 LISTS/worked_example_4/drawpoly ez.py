## 
#  This program draws a regular polygon as a sequence of line segments.
#

from ezgraphics import GraphicsWindow
from math import sin, cos, radians

WIN_SIZE = 400
POLY_RADIUS = 150
POLY_OFFSET = WIN_SIZE // 2 - POLY_RADIUS

def main() :
   win = GraphicsWindow(WIN_SIZE, WIN_SIZE)
   canvas = win.canvas()
   canvas.setOutline("blue")
   numSides = getNumberSides()   
   polygon = buildRegularPolygon(POLY_OFFSET, POLY_OFFSET, numSides, 
      POLY_RADIUS)
   drawPolygon(polygon, canvas)
   win.wait()

## Obtain from the user the number of sides for the polygon.
#  @return the number of sides >= 3 
#
def getNumberSides() :
   numSides = int(input("Enter number of polygon sides (>= 3): "))
   while numSides < 3 :
      print("Error!! the number of sides must be 3 or greater.")
      numSides = int(input("Enter number of polygon sides (>= 3): "))

   return numSides

## Draws a polygon on a canvas.
#  @param vertexList a list of points of the polygon, each of which
#  is a list containing the x- and y-coordinates
#  @param canvas the canvas on which the polygon is drawn
#
def drawPolygon(vertexList, canvas) :
   last = len(vertexList) - 1
   for i in range(last) :
      start = vertexList[i]
      end = vertexList[i + 1]
      canvas.drawLine(start[0], start[1], end[0], end[1])
      
   start = vertexList[last]
   end = vertexList[0]
   canvas.drawLine(start[0], start[1], end[0], end[1])    

## Computes and builds a list of vertices for a regular convex polygon as
#  defined within a bounding square.
#  @param x the x-coordinate of the upper-left corner of the bounding square
#  @param y the y-coordinate of the upper-left corner of the bounding square
#  @param sides the number of sides for the polygon
#  @param radius the radius of regular polygon
#  @return the list of vertices stored in the format [[x1, y1], ... [xn, yn]] 
#
def buildRegularPolygon(x, y, sides, radius) :
   xOffset = x + radius
   yOffset = y + radius
   angle = 0.0
   angleInc = radians(360 / sides)
   vertexList = []
   for i in range(sides) :
      xVertex = xOffset + radius * cos(angle)
      yVertex = yOffset + radius * sin(angle)
      vertexList.append([round(xVertex), round(yVertex)])
      angle = angle + angleInc
      
   return vertexList

# Start the program.
main()

