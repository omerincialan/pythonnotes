## 
#  This program defines a function for calculating a pyramid's volume and
#  provides a unit test for the function.
#

def main() :
   print("Volume:", pyramidVolume(9, 10))
   print("Expected: 300")
   print("Volume:", pyramidVolume(0, 10))
   print("Expected: 0")

## Computes the volume of a pyramid whose base is a square.
#  @param height a float indicating the height of the pyramid
#  @param baseLength a float indicating the length of one side of 
#  the pyramid's base
#  @return the volume of the pyramid as a float
#
def pyramidVolume(height, baseLength) :
   baseArea = baseLength * baseLength
   return height * baseArea / 3

# Start the program.
main()

