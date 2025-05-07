from ezgraphics import GraphicsWindow, GraphicsImage

GAP = 10
NUM_PICTURES = 5  # Temporarily set to 5 for testing step 6.
MAX_WIDTH = 720

win = GraphicsWindow(750, 350)
canvas = win.canvas()

pic = GraphicsImage("picture1.gif")
canvas.drawImage(0, 0, pic)

x = 0
maxY = 0
for i in range(2, NUM_PICTURES + 1) :
   maxY = max(maxY, pic.height())
   previous = pic
   filename = "picture%d.gif" % i
   pic = GraphicsImage(filename)
   x = x + previous.width() + GAP
   if x + pic.width() < MAX_WIDTH :
      canvas.drawImage(x, 0, pic)
   else :
      canvas.drawImage(0, maxY + GAP, pic)

win.wait()

