## 
#  This program arranges a collection of pictures into rows by lining 
#  them up along the top edges and separating them with small gaps.
#

from ezgraphics import GraphicsImage, GraphicsWindow

GAP = 10
NUM_PICTURES = 20
MAX_WIDTH = 720

win = GraphicsWindow(750, 750)  # Taller window to show all pictures
canvas = win.canvas()

pic = GraphicsImage("picture1.gif")
canvas.drawImage(0, 0, pic)

x = 0
y = 0
maxY = 0
for i in range(2, NUM_PICTURES + 1) :
   maxY = max(maxY, pic.height())
   previous = pic
   filename = "picture%d.gif" % i
   pic = GraphicsImage(filename)
   x = x + previous.width() + GAP
   if x + pic.width() < MAX_WIDTH :
      canvas.drawImage(x, y, pic)
   else :
      x = 0
      y = y + maxY + GAP
      canvas.drawImage(x, y, pic)
    
win.wait()

