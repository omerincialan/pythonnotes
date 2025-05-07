## A triangular shape composed of stacked unit squares like this:
#  []
#  [][]
#  [][][]
#   . . .
class Triangle :
   ## Constructs a triangular shape.
   #  @param sideLength the side length of the triangle
   #
   def __init__(self, sideLength) :
      self._sideLength = sideLength
      
   ## Computes the area of the triangle.
   #  @return the area
   #      
   def getArea(self) :
      if self._sideLength <= 0 : 
         return 0
      elif self._sideLength == 1 :
         return 1
      else :
         smallerTriangle = Triangle(self._sideLength - 1)
         smallerArea = smallerTriangle.getArea()
         area = smallerArea + self._sideLength
         return area

