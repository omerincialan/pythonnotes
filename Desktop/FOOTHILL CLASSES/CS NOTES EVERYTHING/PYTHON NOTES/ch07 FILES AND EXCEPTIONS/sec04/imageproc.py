##
#  This program processes a digital image by creating a negative of a BMP image.
#

from io import SEEK_CUR
from sys import exit

def main() :
   filename = input("Please enter the file name: ")

   # Open as a binary file for reading and writing.
   imgFile = open(filename, "rb+") 
   
   # Extract the image information.
   fileSize = readInt(imgFile, 2)
   start = readInt(imgFile, 10)
   width = readInt(imgFile, 18)
   height = readInt(imgFile, 22)

   # Scan lines must occupy multiples of four bytes.
   scanlineSize = width * 3
   if scanlineSize % 4 == 0 :
      padding = 0
   else :
      padding = 4 - scanlineSize % 4
      
   # Make sure this is a valid image.      
   if fileSize != (start + (scanlineSize + padding) * height) :
      sys.exit("Not a 24-bit true color image file.")

   # Move to the first pixel in the image.
   imgFile.seek(start)
   
   # Process the individual pixels.
   for row in range(height) :  # For each scan line
      for col in range(width) :  # For each pixel in the line
         processPixel(imgFile)         

      # Skip the padding at the end
      imgFile.seek(padding, SEEK_CUR)
      
   imgFile.close()   

## Processes an individual pixel.
#  @param imgFile the binary file containing the BMP image
#
def processPixel(imgFile) :
   # Read the pixel as individual bytes.
   theBytes = imgFile.read(3)
   blue = theBytes[0]
   green = theBytes[1]
   red = theBytes[2]

   # Process the pixel.
   newBlue = 255 - blue
   newGreen = 255 - green
   newRed = 255 - red
   
   # Write the pixel.
   imgFile.seek(-3, SEEK_CUR)   # Go back 3 bytes to the start of the pixel
   imgFile.write(bytes([newBlue, newGreen, newRed])) 
           
## Gets an integer from a binary file.
#  @param imgFile the file
#  @param offset the offset at which to read the integer
#  @return the integer starting at the given offset
#
def readInt(imgFile, offset) :
   # Move the file pointer to the given byte within the file.
   imgFile.seek(offset)
      
   # Read the 4 individual bytes and build an integer.
   theBytes = imgFile.read(4)   
   result = 0
   base = 1
   for i in range(4) :
      result = result + theBytes[i] * base 
      base = base * 256
      
   return result

# Start the program.
main()

