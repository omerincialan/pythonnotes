## This program illustrates the use of the tools   
#  in the image processing toolkit.
#

from ezgraphics import GraphicsImage, GraphicsWindow
from imgproctools import *

# Read the name of the file to be processed.
filename = input("Enter the name of the image file to be processed: ")

# Load the image from the file and display it in a window.
image = GraphicsImage(filename)

win = GraphicsWindow()
canvas = win.canvas()
canvas.drawImage(image)
done = False

while not done :
   # Prompt the user for the type of processing.
   print("How should the image be processed?")
   print("1 - create image negative")
   print("2 - adjust brightness")
   print("3 - flip vertically")
   print("4 - rotate to the left")
   print("5 - save and quit")

   response = int(input("Enter your choice: "))
         
# Process the image and display the new image in the window.
   if response == 1 : 
      newImage = createNegative(image)
   elif response == 2 :
      amount = float(input("Adjustment between -1.0 and 1.0: "))
      newImage = adjustBrightness(image, amount)
   elif response == 3 :
      newImage = flipVertically(image)
   elif response == 4 :
      newImage = rotateLeft(image) 

   if response == 5 :
      newImage.save("output.gif")
      done = True
   else :
      canvas.drawImage(newImage)
      image = newImage
         

