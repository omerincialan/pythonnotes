##
#
#

from ezgraphics import GraphicsImage

## Creates and returns a new image that is the negative of the original. 
#  @param image the source image
#  @return the new negative image 
#
def createNegative(image) :
   width = image.width()
   height = image.height()
  
   # Create a new image that is the same size as the original.
   newImage = GraphicsImage(width, height)
   for row in range(height) :
      for col in range(width) :

         # Get the color of the pixel in the original image.
         red = image.getRed(row, col)
         green = image.getGreen(row, col)
         blue = image.getBlue(row, col)
      
         # Filter the pixel.
         newRed = 255 - red
         newGreen = 255 - green
         newBlue = 255 - blue
  
         # Set the pixel in the new image to the new color.
         newImage.setPixel(row, col, newRed, newGreen, newBlue)

   return newImage

## Creates and returns a new image in which the brightness levels of
#  all three color components are adjusted by a given percentage.
#  @param image the source image
#  @param amount the percentage by which to adjust the brightness
#  @return the new image
#
def adjustBrightness(image, amount) :
   width = image.width()
   height = image.height()
  
   # Create a new image that is the same size as the original.
   newImage = GraphicsImage(width, height)
   for row in range(height) :
      for col in range(width) :

         # Get the color of the pixel in the original image.
         red = image.getRed(row, col)
         green = image.getGreen(row, col)
         blue = image.getBlue(row, col)
      
         # Adjust the brightness and cap the colors.
         newRed = int(red + red * amount)
         if newRed > 255 :
            newRed = 255
         elif newRed < 0 :
            newRed = 0
         newGreen = int(green + green * amount)
         if newGreen > 255 :
            newGreen = 255
         elif newGreen < 0 :
            newGreen = 0
         newBlue = int(blue + blue * amount)
         if newBlue > 255 :
            newBlue = 255
         elif newBlue < 0 :
            newBlue = 0
      
         # Set the pixel in the new image to the new color.
         newImage.setPixel(row, col, newRed, newGreen, newBlue)

   return newImage


## Creates and returns a new image that results from flipping an original 
#  image vertically.
#  @param image the source image
#  @return the new vertically flipped image
#
def flipVertically(image) :  
   # Create a new image that is the same size as the original.
   width = image.width()
   height = image.height()
   newImage = GraphicsImage(width, height)
  
   # Flip the image vertically.
   newRow = height - 1
   for row in range(height) :
      for col in range(width) :
         newCol = col
         pixel = image.getPixel(row, col)
         newImage.setPixel(newRow, newCol, pixel)
        
      newRow = newRow - 1      

   return newImage

## Rotates the image 90 degrees to the left.
#  @param image the image to be rotated
#  @return the new rotated image
# 
def rotateLeft(image) :
   # Create a new image whose dimensions are the opposite of the original.
   width = image.width()
   height = image.height()
   newImage = GraphicsImage(height, width)
  
   # Rotate the image.
   for row in range(height) :
      newCol = row
      for col in range(width) :
         newRow = col
         pixel = image.getPixel(row, col)
         newImage.setPixel(newRow, newCol, pixel)
        
   return newImage


## Compares two images to determine if they are identical.
#  @param image1, image2 the two images to be compared
#  @return True if the images are identical, False otherwise
# 
def sameImage(image1, image2) :
   # Make sure the images are the same size.
   width = image1.width()
   height = image1.height()
   if width != image2.width() or height != image2.height() :
      return False
    
   # Compare the two images, pixel by pixel.
   for row in range(height) :
      for col in range(width) :
         pixel1 = image1.getPixel(row, col)
         pixel2 = image2.getPixel(row, col)
      
         # Compare the color components of corresponding pixels.
         for i in range(3) :
            if pixel1[i] != pixel2[i] :
               return False
   
   # Indicate the images are identical.
   return True

