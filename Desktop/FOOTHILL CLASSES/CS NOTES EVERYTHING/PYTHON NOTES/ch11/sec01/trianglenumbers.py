##
#  This program computes a triangle number using recursion.
#

def main() :
   area = triangleArea(10)      
   print("Area:", area)
   print("Expected: 55")

## Computes the area of a triangle with a given side length.
#  @param sideLength the side length of the triangle base
#  @return the area
#
def triangleArea(sideLength) :
   if sideLength <= 0 :
      return 0
   if sideLength == 1 :
      return 1
   smallerSideLength = sideLength - 1
   smallerArea = triangleArea(smallerSideLength)
   area = smallerArea + sideLength
   return area
         
# Start the program.
main()

