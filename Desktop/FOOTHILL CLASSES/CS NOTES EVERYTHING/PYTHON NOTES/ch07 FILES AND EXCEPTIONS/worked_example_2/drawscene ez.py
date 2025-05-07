##
#  Draws simple figures on the canvas based on data in a text file.
#

from ezgraphics import GraphicsWindow

def main() :
   infile = open("lamppost.fig", "r")
   
   win = configureWindow(infile)
   canvas = win.canvas()

   objData = extractNextLine(infile)
   while objData != "" :
      drawObject(objData, canvas)
      objData = extractNextLine(infile)
      
   win.wait()

## Configures the graphics window based on the canvas parameters from 
#  the scene file.
#  @param infile the text file containing the scene description
#
def configureWindow(infile) :
   # Extract the window size.
   width = int(extractNextLine(infile))
   height = int(extractNextLine(infile))
   
   # Extract the background color.
   color = extractNextLine(infile)
   color = color.strip()
   
   # Create the window and set the background color.
   win = GraphicsWindow(width, height)
   canvas = win.canvas()
   canvas.setBackground(color)   
   
   # Return the window object.
   return win
      
## Extracts a single non-comment line from the text file.
#  @param infile the text file containing the scene description
#  @return the next non-comment line as a string or the empty string if the
#  end of file was reached
#
def extractNextLine(infile) :
   line = infile.readline()
   while line != "" and line[0] == "#" :
      line = infile.readline()
      
   return line
   
## Draws a single object on the canvas based on the description extracted 
#  from a scene file.
#  @param objData a string containing the description of an object
#  @param canvas the canvas on which to draw
#
def drawObject(objData, canvas) :
   # Extract the object data. All objects share the first 4 fields.
   parts = objData.split(",", 4)   # Split into 5 parts. 
   objType = parts[0].strip()
   x = int(parts[1])
   y = int(parts[2])
   outline = parts[3].strip()
   params = parts[4].strip()

   # Set the object color. All objects have an outline color.
   canvas.setOutline(outline)
   
   # The last substring from the split contains the parameters for the
   # given object, which depends on the type of the object.
   if objType == "text" :   
      canvas.drawText(x, y, params)
   else :  
      values = params.split(",")              
      if objType == "line" :  
         endX = int(values[0])
         endY = int(values[1])
         canvas.drawLine(x, y, endX, endY)
      else :  
         # Extract the fill color and set the canvas to use it.
         fill = values[0].strip()
         canvas.setFill(fill)
         
         # Extract the width and height and use them to draw the object.
         width = int(values[1])
         height = int(values[2])
         if objType == "rect" :
            canvas.drawRect(x, y, width, height)
         elif objType == "oval" :
            canvas.drawOval(x, y, width, height)
      
# Start the program.
main()

